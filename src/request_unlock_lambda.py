import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.dumps({'doUnlock': True})
    response = s3.put_object(Body=body, Bucket='doorunlockstatus', Key='status.txt')

    return {
        "statusCode": 200,
        "body": json.dumps('Set Unlock value to 1')
    }
