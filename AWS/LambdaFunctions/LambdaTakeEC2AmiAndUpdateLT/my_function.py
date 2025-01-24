import json
import urllib3
from datetime import datetime, timezone, timedelta


def getInstanceIdByTag(resource, event):

    tagName = event["tagName"]
    tagValue = event["tagValue"]

    instances = resource.instances.filter(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [tagValue]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ])

    if len(list(instances)) == 0:
        return ""

    for instance in instances:
        return instance.id


def createImageByInstanceId(resource, instanceId, event):

    amiName = str(event["amiName"])
    description = event["description"]
    amiTagValue = "(P) " + str(event["tagValue"])

    instance = resource.Instance(instanceId)

    image=instance.create_image(
        Name= amiName ,
        Description=description,
        NoReboot=True,
        TagSpecifications=[
        {
            'ResourceType': 'image',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': amiTagValue
                },
                {
                    'Key': str(event["tagName"]),
                    'Value': str(event["tagValue"])
                },
            ],
        },
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': amiTagValue
                },
                {
                    'Key': str(event["tagName"]),
                    'Value': str(event["tagValue"])
                },
            ],
        },
    ]
    )

    return image

def updateCurrentLaunchTemplateVersion(resource, ami, event):

    tagName = event["tagName"]
    tagValue = event["tagValue"]
    ltDescription = event["description"]

    lt = resource.meta.client.describe_launch_templates(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }]).get('LaunchTemplates')[0]

    resource.meta.client.modify_launch_template(
        LaunchTemplateId=lt['LaunchTemplateId'],
        DefaultVersion=str(lt['LatestVersionNumber'])
    )

    resource.meta.client.create_launch_template_version(
            LaunchTemplateId=lt['LaunchTemplateId'],
            SourceVersion= "$Default",
            VersionDescription=ltDescription,
            LaunchTemplateData={
                "ImageId": ami
            }
        )

    return lt

def deleteLaunchTemplateOldVersions(resource, event):

    tagName = event["tagName"]
    tagValue = event["tagValue"]

    lt = resource.meta.client.describe_launch_templates(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }]).get("LaunchTemplates")[0]

    ltVersions = resource.meta.client.describe_launch_template_versions(
            LaunchTemplateId=lt['LaunchTemplateId']
        ).get("LaunchTemplateVersions")

    for ltVersion in ltVersions:
        if ltVersion['VersionNumber'] != lt["LatestVersionNumber"] and ltVersion['VersionNumber'] != lt["DefaultVersionNumber"]:
            resource.meta.client.delete_launch_template_versions(
                LaunchTemplateId=lt['LaunchTemplateId'],
                Versions=[str(ltVersion['VersionNumber'])]
            )

def deregisterAmiByTag(resource, event):

    tagName = event["tagName"]
    tagValue = event["tagValue"]

    keepLastAmisCount = event["keepAmiCount"]

    images = resource.meta.client.describe_images(Filters=[
        {
            'Name': 'tag:' + tagName,
            'Values': [
                tagValue,
            ]
        }])
    amisList = []
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

    if len(amisList) > keepLastAmisCount:
        def getlistDate(date):
            return date.get('creationDate')
        amisList.sort(key=getlistDate)
        del amisList[-keepLastAmisCount:]

        for ami in amisList:
            resource.meta.client.deregister_image(ImageId=ami['imageId'])
            for snapshotId in ami['snapshotIds']:
                resource.meta.client.delete_snapshot(SnapshotId=snapshotId)
    else:
        return [{'imageName': "",
            'description': "Nothing to delete",
            'imageId': "",
            'snapshotIds': []}]

    return amisList

def sendNotificationsToSlack(msgHeader, msgStatus, msg):

    slackUrl = "https://hooks.slack.com/services/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"
    dateTimeStr = datetime.now().astimezone(timezone(timedelta(hours = 4, minutes = 0), "Europe/Paris")).strftime("%Y-%m-%d %H:%M:%S")

    if msgStatus == "faild":
        msgStatus = ":x: "
        msgCode = str(msg['code'])
        msg = str(msg['message'])

        messange = {
            "channel": "#aws-notifications",
            "username": "lambda",
            "icon_emoji": ":aws:",
            "text": msgStatus + msgHeader,
            "blocks": [
        		{
        			"type": "section",
        			"text": {
        				"type": "mrkdwn",
        				"text": msgStatus +"*" + msgHeader + "*",
        			}
        		},
        		{
                "type": "divider"
                },
        		{
        			"type": "section",
        			"fields": [
        				{
        					"type": "mrkdwn",
        					"text": "*Code:*\n" + msgCode
        				},
        				{
        					"type": "mrkdwn",
        					"text": "*Message:*\n" + msg
        				}
        			]
        		},
        		{
        			"type": "section",
        			"fields": [
        				{
        					"type": "mrkdwn",
        					"text": "*Time:*\n" + dateTimeStr
        				}
        			]
        		},
        		{
                "type": "divider"
                }
    	    ]
        }
    else:
        msgStatus = ":heavy_check_mark:"

        messange = {
            "channel": "#aws-notifications",
            "username": "lambda",
            "icon_emoji": ":aws:",
            "text": msgStatus + msgHeader,
            "blocks": [
        		{
        			"type": "section",
        			"text": {
        				"type": "mrkdwn",
        				"text": msgStatus +"*" + msgHeader + "*",
        			}
        		},
        		{
                    "type": "divider"
                },
        		{
        			"type": "section",
        			"fields": [
        				{
        					"type": "mrkdwn",
        					"text": "*ID:*\n" + str(msg["id"])
        				},
        				{
        					"type": "mrkdwn",
        					"text": "*Name:*\n" + str(msg["name"])
        				}
        			]
        		},
        		{
        			"type": "section",
        			"fields": [
        				{
        					"type": "mrkdwn",
        					"text": "*Description:*\n" + str(msg["description"])
        				},
        				{
        					"type": "mrkdwn",
        					"text": "*Time:*\n" + dateTimeStr
        				}
        			]
        		},
        		{
                "type": "divider"
                }
    	    ]
        }


    encoded_msg = json.dumps(messange).encode("utf-8")

    http = urllib3.PoolManager()
    http.request("POST", slackUrl, body=encoded_msg)