import json
import boto3

def lambda_handler(event, context):
    rdsClient = boto3.client('rds')
    response = rdsClient.describe_db_instances().get('DBInstances')

    for dbInstance in response:
        if( len(dbInstance['TagList']) != 0 ):
            for tag in dbInstance['TagList']:
                if tag['Value'] == "Stop":
                    if dbInstance['DBInstanceStatus'] == 'available':
                        rdsClient.stop_db_instance(DBInstanceIdentifier = dbInstance['DBInstanceIdentifier'])
                    elif dbInstance['DBInstanceStatus'] == 'stopped':
                        rdsClient.start_db_instance(DBInstanceIdentifier = dbInstance['DBInstanceIdentifier'])