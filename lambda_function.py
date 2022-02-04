import json
import datetime

print('Loading function')

def lambda_handler(event, context):
    timestamp = datetime.datetime.utcnow() # current UTC tz date and time object
    resp = { "name":event['name'], "requestId":context.aws_request_id, "timestamp":timestamp.isoformat()}
    print("name = ", event['name'])
    return resp  # Echo back the name from the event object in a JSON response object
