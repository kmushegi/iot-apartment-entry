import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='doorunlockstatus', Key='status.txt')
    content = response['Body'].read().decode('utf-8')
    content = json.loads(content)
    doUnlock = content['doUnlock']
    if doUnlock:
        content['doUnlock'] = False
        response = s3.put_object(Body=json.dumps(content), Bucket='doorunlockstatus', Key='status.txt')

    return {
        "statusCode": 200,
        "unlockStatus": doUnlock
    }
