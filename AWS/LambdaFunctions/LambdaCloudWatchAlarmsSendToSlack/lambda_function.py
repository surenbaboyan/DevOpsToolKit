import json
import urllib3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):

    slackUrl = "https://hooks.slack.com/services/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"
    dateTimeStr = datetime.now().astimezone(timezone(timedelta(hours = 4, minutes = 0))).strftime("%Y-%m-%d %H:%M:%S")

    alarmMessage = json.loads(json.dumps(event))["Records"][0]["Sns"]["Message"]
    alarmMessageDescription = json.loads(alarmMessage)["AlarmDescription"]
    alarmStatus = json.loads(alarmMessage)["NewStateValue"]

    if alarmStatus == "ALARM":
        alarmColor = "#ec0003"
        alarmMsg = json.loads(alarmMessageDescription)["messageAlarm"].format(convert_bytes(json.loads(alarmMessage)["Trigger"]["Threshold"]))
    elif alarmStatus == "OK":
        alarmColor = "#36a64f"
        alarmMsg = json.loads(alarmMessageDescription)["messageOk"].format(convert_bytes(json.loads(alarmMessage)["Trigger"]["Threshold"]))

    metricName = json.loads(alarmMessage)["Trigger"]["MetricName"]
    awsService = json.loads(alarmMessage)["Trigger"]["Namespace"]
    msgHeader = "{} | Project: {}".format(awsService, json.loads(alarmMessage)["AlarmName"].split(" ")[-1])

    match awsService:
        case "AWS/RDS":
            url = "https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#database:id={}".format(json.loads(alarmMessage)["Trigger"]["Dimensions"][0]["value"])
        case "AWS/ElastiCache":
            url = "https://us-east-1.console.aws.amazon.com/elasticache/home?region=us-east-1#/redis/{}".format(json.loads(alarmMessage)["Trigger"]["Dimensions"][0]["value"])
        case "AWS/EC2":
            url = "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#Instances:instanceState=running;instanceId={}".format(json.loads(alarmMessage)["Trigger"]["Dimensions"][0]["value"])
        case _:
            url="https://localhost"

    message = {
        "channel": "#aws-cloudwatch-alarms",
        "username": "CloudWatch",
        "icon_emoji": ":aws:",
        "text": "*<{} | {}>*".format(url, msgHeader),
        "attachments": [
	        {
			    "color": alarmColor,
                "blocks": [
                    {
            			"type": "section",
            			"fields": [
            				{
            					"type": "mrkdwn",
            					"text": "*MetricName:*\n{}".format(metricName)
            				}
            			]
            		},
            		{
                    "type": "divider"
                    },
                    {
            			"type": "section",
            			"fields": [
            				{
            					"type": "mrkdwn",
            					"text": "*Message:*\n{}".format(alarmMsg)
            				},
            				{
            					"type": "mrkdwn",
            					"text": "*Time:*\n{}".format(dateTimeStr)
            				}
            			]
            		},
            		{
                    "type": "divider"
                    }
        	    ]
    	    }
        ]
    }

    encoded_msg = json.dumps(message).encode("utf-8")

    http = urllib3.PoolManager()
    http.request("POST", slackUrl, body=encoded_msg)

def convert_bytes(size):
    if size <= 100:
        return "{:.0f}".format(size)

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1000:
            return "{:.0f} {}".format(size, x)
        size /= 1000

    return int(size)