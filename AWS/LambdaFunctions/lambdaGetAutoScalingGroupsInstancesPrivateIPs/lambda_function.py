import json
import boto3
import time

def lambda_handler(event, context):

    tagName = event["tagName"]
    tagValue = event["tagValue"]

    cwClient = boto3.resource('cloudwatch')
    alarms = cwClient.alarms.all()

    instanceIds = []
    '''
    alarmDown = cwClient.Alarm('(P) Patio - Scale Down').set_state(
        StateValue='OK',
        StateReason='Test',
    )
    alarmUp = cwClient.Alarm('(P) Patio - Scale Up').set_state(
        StateValue='ALARM',
        StateReason='Test',
    )
    '''
    for alarm in alarms:
        if tagValue in alarm.name:
            alarm.disable_actions()

    time.sleep(17)

    asgClient = boto3.client('autoscaling')
    ec2Client = boto3.client('ec2')

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
                    'Version': '$Latest'
                }
            )

    for instance in asgResponse['Instances']:
        if instance['LifecycleState'] != 'Terminating' and instance['LifecycleState'] != 'Terminated':
            instanceIds.append(instance['InstanceId'])

    privateIp = ""
    if len(instanceIds) != 0:
        ec2Response = ec2Client.describe_instances(InstanceIds = instanceIds)

        for instances in ec2Response['Reservations']:
            for ip in instances['Instances']:
                privateIp += ip['PrivateIpAddress'] + " "

    return privateIp