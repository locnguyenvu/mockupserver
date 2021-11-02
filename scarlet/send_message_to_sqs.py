import boto3
import os
from os import path
from dotenv import load_dotenv

load_dotenv()

access_key_id=str(os.getenv("AWS_SQS_ACCESS_KEY_ID"))
access_key_secret=str(os.getenv("AWS_SQS_ACCESS_KEY_SECRET"))

sqs = boto3.client(
    'sqs',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=access_key_secret,
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

