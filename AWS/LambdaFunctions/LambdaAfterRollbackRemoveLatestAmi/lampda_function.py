import json
import boto3
import time

def lambda_handler(event, context):

    tagName = event["tagName"]
    tagValue = event["tagValue"]
    amisList = []

    asgClient = boto3.client('autoscaling')
    ec2Client = boto3.client('ec2')
    resource = boto3.resource('ec2')

    cwClient = boto3.resource('cloudwatch')
    alarms = cwClient.alarms.all()

    # Find Current Project AutoScalingGroup And Set Template Version To Default
    asgResponse = asgClient.describe_auto_scaling_groups(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }]).get('AutoScalingGroups')[0]

    asgClient.update_auto_scaling_group(
        AutoScalingGroupName=asgResponse['AutoScalingGroupName'],
        LaunchTemplate={
            'LaunchTemplateId': asgResponse['LaunchTemplate']['LaunchTemplateId'],
                    'Version': '$Default'
        }
    )

    # Find Current Project Images And Sort
    images = resource.meta.client.describe_images(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }])

    for image in images['Images']:
        ami = {'imageName': image['Name'],
                     'description': image['Description'] if 'Description' in image else "",
                     'imageId': image['ImageId'],
                     'creationDate': image['CreationDate'],
                     'snapshotIds': []}
        for BlockDeviceMapping in image["BlockDeviceMappings"]:
            if 'Ebs' in BlockDeviceMapping:
                ami['snapshotIds'].append(BlockDeviceMapping['Ebs']['SnapshotId'])
        amisList.append(ami)

    def getlistDate(date):
            return date.get('creationDate')

    amisList.sort(key=getlistDate)

    # Delete Latest Image And Snepshots
    resource.meta.client.deregister_image(ImageId=amisList[-1]['imageId'])
    for snapshotId in amisList[-1]['snapshotIds']:
        resource.meta.client.delete_snapshot(SnapshotId=snapshotId)

    # Find Current Project Launch Template And Delete Latest Version Number
    lt = resource.meta.client.describe_launch_templates(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }]).get("LaunchTemplates")[0]

    resource.meta.client.delete_launch_template_versions(
        LaunchTemplateId=lt['LaunchTemplateId'],
        Versions=[str(lt["LatestVersionNumber"])]
    )

    # Enable Current Project Alarms
    for alarm in alarms:
        if tagValue in alarm.name:
            alarm.enable_actions()

    return tagValue + ": Latest image removed and asg group set to default."