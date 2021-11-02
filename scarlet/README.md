# Setup
## Install requisites

```
pip3 install boto3 
pip3 install python-dotenv
```

## Create dot file `.env`

```
# Staging
WEBHOOK_SECRET=

# SQS setting
AWS_SQS_ACCESS_KEY_ID=
AWS_SQS_ACCESS_KEY_SECRET=
```

# Usage

## 1. Catalog server
```
python3 catalog_server.py -p <port>
```

## 2. Send message to webhook
```
python3 send_message_to_webhook.py <host-url>
```
