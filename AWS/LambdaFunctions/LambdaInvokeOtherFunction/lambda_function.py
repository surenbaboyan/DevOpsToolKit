import json
import boto3

def lambda_handler(event, context):

    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:111652013027:function:LambdaTakeEC2AmiAndUpdateLT',
        InvocationType = 'Event',
        Payload = json.dumps(event)
    )

    if "enableAlarms" in event:
        return str(event["tagValue"]) + " project alarms in CloudWatch enabled"
    else:
        return str(event["tagValue"]) + " project - Ami Backups started. For more information please see in slack aws_notifications channel"