import hashlib
import hmac
import hashlib
import base64
import requests
import sys
import os

if len(sys.argv) == 1:
    print("Host is missing")
    sys.exit(2)

host = sys.argv[1]
webhook_secret = ""


def sign_x(payload):
    dig = hmac.new(bytes(webhook_secret, 'utf8'), msg=bytes(payload, "utf8"), digestmod=hashlib.sha256)
    return dig.hexdigest()

payload='{"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductStatusName":"Todo","ProductStatusId":2000,"PayloadId":"b6d737ab-3033-490d-b956-a1bed98499e1","EventGroupName":"product","EventDatetimeUtc":1629789316604,"Action":"PropertiesUpdated","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": "Reset"}, data=payload)
print(r)

###

payload = '{"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","ProductStatusName":"Todo","ProductStatusId":2000,"PayloadId":"54658cfe-c282-49d1-bf68-b465815a52e6","EventGroupName":"product","EventDatetimeUtc":1629789316594,"Action":"StyleGuideChanged","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": "StyleGuideChanged"}, data=payload)
print(r)

###
payload = '{"TaskId":"21b0ba96-82d6-4a90-9bb6-98cdea8a97ec","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"12f6751c-2aeb-4d69-a67a-e704b127a70a","EventGroupName":"task","EventDatetimeUtc":1629789335530,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"21b0ba96-82d6-4a90-9bb6-98cdea8a97ec","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"3485dc33-c8ea-4553-89d5-e10011d23a44","EventGroupName":"task","EventDatetimeUtc":1629789341620,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","ProductStatusName":"Todo","ProductStatusId":2000,"PayloadId":"f315b210-ba45-46d0-b5fe-32529e734a96","EventGroupName":"product","EventDatetimeUtc":1629789341673,"Action":"StatusChanged","Actor":{"UserId":"00000000-0000-0000-0000-000000000000"}}'
event = 'StatusChanged'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)


###

payload = '{"TaskId":"21b0ba96-82d6-4a90-9bb6-98cdea8a97ec","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"39818478-f1a4-4fe2-bac5-2cb6565e5e63","EventGroupName":"task","EventDatetimeUtc":1629789345205,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"05743934-e655-4bb9-bd79-b5f98802d5f2","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":4,"StepName":"Final Selection","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"da4b72ba-b7d1-4944-97ad-9404e3475d7d","EventGroupName":"task","EventDatetimeUtc":1629789345313,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"21b0ba96-82d6-4a90-9bb6-98cdea8a97ec","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"f8b68218-ed98-4e25-89bd-6944ed0f9c58","EventGroupName":"task","EventDatetimeUtc":1629789345158,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"05743934-e655-4bb9-bd79-b5f98802d5f2","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":4,"StepName":"Final Selection","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"a1cc69da-2d92-4877-9104-31fc5cbf486c","EventGroupName":"task","EventDatetimeUtc":1629789345340,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"2a1e3c07-c0a3-4007-87be-fcadbf9c73c7","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":15,"StepName":"Photo Review","StepStatusId":8000,"StepStatusName":"Bypassed","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"dd510b2d-f233-4c44-82ee-5d4ec12e1401","EventGroupName":"task","EventDatetimeUtc":1629789345613,"Action":"Bypassed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Bypassed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"ab87388a-06c1-4681-b486-e2515b5bab44","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":2000,"StepStatusName":"To Do","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"ec2f1432-e000-480b-98d7-4090aee2c340","EventGroupName":"task","EventDatetimeUtc":1629789346096,"Action":"ReadyToWork","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'ReadyToWork'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"82e0ad1f-2404-4023-a2de-d9cf715befde","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"ad30e873-bf75-4427-bac7-ec01e5631d39","EventGroupName":"task","EventDatetimeUtc":1629789347598,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"82e0ad1f-2404-4023-a2de-d9cf715befde","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"814402d4-121a-4029-8c79-440ec73a636c","EventGroupName":"task","EventDatetimeUtc":1629789351573,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"82e0ad1f-2404-4023-a2de-d9cf715befde","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"23feab67-b9b1-4a1c-90cb-943acac7504f","EventGroupName":"task","EventDatetimeUtc":1629789356698,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"82e0ad1f-2404-4023-a2de-d9cf715befde","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":3,"StepName":"Photography","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"8dabb633-7b68-4194-b529-4c5b571e62cd","EventGroupName":"task","EventDatetimeUtc":1629789356727,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"fd09fb1b-85a7-455b-b79b-70b479a25ae9","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":4,"StepName":"Final Selection","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"56919cc7-f088-42ed-8bae-0033955884ac","EventGroupName":"task","EventDatetimeUtc":1629789356795,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"a218ebe9-d74f-4b3f-a438-3e72ab51ea0f","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":15,"StepName":"Photo Review","StepStatusId":8000,"StepStatusName":"Bypassed","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"7058eaeb-b7af-43dd-8984-903ab06ca8dc","EventGroupName":"task","EventDatetimeUtc":1629789356886,"Action":"Bypassed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Bypassed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"6d9934d2-e09b-4a20-ad26-bf681cedfd85","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":2000,"StepStatusName":"To Do","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"4c755b60-8453-4140-b8e7-9a58e510e4bc","EventGroupName":"task","EventDatetimeUtc":1629789358091,"Action":"ReadyToWork","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'ReadyToWork'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"fd09fb1b-85a7-455b-b79b-70b479a25ae9","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":4,"StepName":"Final Selection","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"05c57513-6863-49ea-99ab-0f93f6a13f2c","EventGroupName":"task","EventDatetimeUtc":1629789356810,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"ab87388a-06c1-4681-b486-e2515b5bab44","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"6bf7012f-d097-4b60-bbcf-69155b9c3883","EventGroupName":"task","EventDatetimeUtc":1629789399953,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"6d9934d2-e09b-4a20-ad26-bf681cedfd85","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":1000,"StepStatusName":"New","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"f0b1196c-9acc-4baf-8016-5bec9264b016","EventGroupName":"task","EventDatetimeUtc":1629789401383,"Action":"Assigned","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Assigned'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"ab87388a-06c1-4681-b486-e2515b5bab44","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"18bc2f42-dce4-4fff-a0fc-0a31a6704a2d","EventGroupName":"task","EventDatetimeUtc":1629789404010,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"ab87388a-06c1-4681-b486-e2515b5bab44","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"87d07966-ac0a-4574-911c-d00132214582","EventGroupName":"task","EventDatetimeUtc":1629789421280,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7c2f2106-4908-4f66-a086-d598475ca058","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":2000,"StepStatusName":"To Do","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"a72cc548-58ea-426e-a0e3-3de5a3ab780b","EventGroupName":"task","EventDatetimeUtc":1629789422237,"Action":"ReadyToWork","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'ReadyToWork'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"6d9934d2-e09b-4a20-ad26-bf681cedfd85","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"147f4af8-3965-45ca-a2f5-091727dc6416","EventGroupName":"task","EventDatetimeUtc":1629789422441,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"6d9934d2-e09b-4a20-ad26-bf681cedfd85","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":10,"StepName":"Internal Post Production","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"70ac1fea-509c-4256-aa9a-8e7f10bacf2e","EventGroupName":"task","EventDatetimeUtc":1629789433021,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7b7905f3-d3cc-43bd-8363-696cc4c8df11","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":2000,"StepStatusName":"To Do","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"60dbe921-a70e-48c5-b986-b5bf13abcbf2","EventGroupName":"task","EventDatetimeUtc":1629789433553,"Action":"ReadyToWork","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'ReadyToWork'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7c2f2106-4908-4f66-a086-d598475ca058","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"26c5b44b-6e17-4bae-82af-334f6fc5bbe8","EventGroupName":"task","EventDatetimeUtc":1629789455886,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7c2f2106-4908-4f66-a086-d598475ca058","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"89330a28-4a12-49b6-a1e5-ff4f4459b55f","EventGroupName":"task","EventDatetimeUtc":1629789461964,"Action":"Approved","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Approved'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7c2f2106-4908-4f66-a086-d598475ca058","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"08b72d9f-81d5-4ef4-bcd5-ea90f7107cc1","EventGroupName":"task","EventDatetimeUtc":1629789461999,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"c4c0e4db-edb3-4560-8323-1132b77197ad","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":2,"StepName":"End","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":1,"ShootingTypeName":"On Model","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"363ed326-3b57-4fe3-af2a-c692f8aba116","EventGroupName":"task","EventDatetimeUtc":1629789462174,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7b7905f3-d3cc-43bd-8363-696cc4c8df11","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":3000,"StepStatusName":"In Progress","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"8a0609a4-4b41-47f3-948d-787ced59b310","EventGroupName":"task","EventDatetimeUtc":1629789462274,"Action":"Started","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Started'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7b7905f3-d3cc-43bd-8363-696cc4c8df11","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"4d2562d8-05bd-4f5d-93bf-e2d6da90d109","EventGroupName":"task","EventDatetimeUtc":1629789465584,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"7b7905f3-d3cc-43bd-8363-696cc4c8df11","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":11,"StepName":"Internal Post Production QC","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"94e28ef2-8d09-4fe9-b70d-951f55ad196a","EventGroupName":"task","EventDatetimeUtc":1629789465597,"Action":"Approved","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Approved'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"TaskId":"6a533a00-669c-4031-95da-238ca085b384","Assignee":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"},"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","StepId":2,"StepName":"End","StepStatusId":9000,"StepStatusName":"Done","ShootingTypeId":2,"ShootingTypeName":"Mannequin","WorkflowId":"a78da5c0-5fc6-4400-8656-6741e5cbb9b7","WorkflowName":"Test workflow staging","StyleGuideId":"6486f11c-c47d-48c2-9ee4-771b8f19356d","StyleGuideName":"Test Style guide","PayloadId":"19b0f787-ede8-476d-b728-bd144cd9fc61","EventGroupName":"task","EventDatetimeUtc":1629789465721,"Action":"Completed","Actor":{"UserId":"9c40064a-05e4-4f1b-8588-90a6a8ae325a"}}'
event = 'Completed'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)

###

payload = '{"JobId":"98da3e3e-73d3-491d-8599-0ee2762f4737","JobCode":"MPDS-M2050201287612","ClientId":"4e23bc49-8eb7-4d72-b6cc-8b70cedea5b4","ClientName":"Zalora Staging","ProductId":"ef10c929-45ce-4cef-a13f-b59ed55a6a44","ProductCode":"QQ026AC13JASMY","ProductStatusName":"Done","ProductStatusId":9000,"PayloadId":"d34f0e53-7b5c-4a6c-9a3c-770d00654ef6","EventGroupName":"product","EventDatetimeUtc":1629789465800,"Action":"StatusChanged","Actor":{"UserId":"00000000-0000-0000-0000-000000000000"}}'
event = 'StatusChanged'
r = requests.post(host, headers={"x-cf-signature": sign_x(payload), "content-type": "application/json; charset=utf-8", "x-cf-event": event}, data=payload)
print(r)
