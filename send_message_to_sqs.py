import boto3
from os import path

sqs = boto3.client(
    'sqs',
    aws_access_key_id='AKIAZEOURIDIOOKRMDR6',
    aws_secret_access_key='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',
)

payload_file = open('./oms_payload.json', 'r')
payload_contents = payload_file.read()

queue_url = 'https://sqs.ap-southeast-1.amazonaws.com/628047823056/scarlet_sku_for_production.fifo'

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=payload_contents,
    MessageGroupId="scarlet"
)
print(response['MessageId'])

