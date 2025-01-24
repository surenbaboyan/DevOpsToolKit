import sys
import json
import boto3
import time
from botocore.exceptions import ClientError
from my_functions import *

def lambda_handler(event, context):

    if "enableAlarms" in event:
        cwClient = boto3.resource('cloudwatch')
        alarms = cwClient.alarms.all()

        for alarm in alarms:
                if event["tagValue"] in alarm.name:
                    alarm.enable_actions()

        sys.exit()

    # sleep 1 minute until start to create AMI
    time.sleep(60)

    resource = boto3.resource('ec2')

    instanceId = getInstanceIdByTag(resource, event)

    # Create Image
    try:
        msgHeader = "Success!!!  Project: " + event["tagValue"] + "    |   Task: Create Image"
        image = createImageByInstanceId(resource, instanceId, event)
        message = {"id":image.id, "description": event["description"], "name": event["amiName"]}
        #image.wait_until_exists(Filters=[{'Name': 'state', 'Values': ['available']}])
        waiter = resource.meta.client.get_waiter('image_available')
        waiter.wait(ImageIds=[str(image.id)],
                WaiterConfig={
                    'MaxAttempts': 62
                    }
        )
        sendNotificationsToSlack(msgHeader, "success", message)
    except ClientError as error:
        msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Create Image"
        sendNotificationsToSlack(msgHeader, "faild", {"code":error.response['Error']['Code'], "message":error.response['Error']['Message']})
        sys.exit()
    except Exception as error:
        msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Create Image"
        sendNotificationsToSlack(msgHeader, "faild", {"code":"", "message":error})
        sys.exit()

    # Update Launch Template
    if "scalable" in event:
        try:
            msgHeader = "Success!!!  Project: " + event["tagValue"] + "    |   Task: Update Launch Template Version"
            lt = updateCurrentLaunchTemplateVersion(resource, image.id, event);
            message = {"id":lt['LaunchTemplateId'], "description": event["description"], "name": lt['LaunchTemplateName']}
            sendNotificationsToSlack(msgHeader, "success", message)
        except IndexError as error:
            msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Update Launch Template Version"
            sendNotificationsToSlack(msgHeader, "faild", {"code": "Manual", "message": "Launch Template or tag for Launch Template is missing"})
            sys.exit()
        except ClientError as error:
            msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Update Launch Template Version"
            sendNotificationsToSlack(msgHeader, "faild", {"code":error.response['Error']['Code'], "message":error.response['Error']['Message']})
            sys.exit()
        except Exception as error:
            msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Create Image"
            sendNotificationsToSlack(msgHeader, "faild", {"code":"", "message":error})
            sys.exit()

        # Delete Launch Template Old Versions
        deleteLaunchTemplateOldVersions(resource,event)

    # Delete Old Images and snapshots
    try:
        imageIdStr = ""
        imageNameStr = ""
        imageDescStr = ""
        msgHeader = "Success!!!  Project: " + event["tagValue"] + "    |   Task: Remove Old Images And Snapshots"
        amis = deregisterAmiByTag(resource, event)
        for ami in amis:
            imageIdStr += "Image: " + str(ami['imageId']) + "\n"
            imageNameStr += "Image: " + str(ami['imageName']) + "\n"
            imageDescStr += str(ami['description']) + "\n"

            if not ami['snapshotIds']:
                imageIdStr += "Snapshot: \n"
            else:
                for snapshotId in ami['snapshotIds']:
                    imageIdStr += "Snapshot: " + str(snapshotId) +"\n"
        message = {"id":imageIdStr, "description": imageDescStr, "name": imageNameStr}
        sendNotificationsToSlack(msgHeader, "success", message)
    except ClientError as error:
        msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Remove Old Images And Snapshots"
        sendNotificationsToSlack(msgHeader, "faild", {"code":error.response['Error']['Code'], "message":error.response['Error']['Message']})
        sys.exit()
    except Exception as error:
        msgHeader = "ERROR!!!   Project: " + event["tagValue"] + "    |   Task: Remove Old Images And Snapshots"
        sendNotificationsToSlack(msgHeader, "faild", {"code":"", "message":error})
        sys.exit()

    if "scalable" in event:
        cwClient = boto3.resource('cloudwatch')
        alarms = cwClient.alarms.all()

        for alarm in alarms:
                if event["tagValue"] in alarm.name:
                    alarm.enable_actions()