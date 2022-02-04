# echo-name-python
Simple echo name AWS Lambda function in Python

## Description
This AWS Lambda function is a very simple "echo" type service where it'll echo your input object back to you in its response.

## Pre-requisites
* Python 3.7 runtime environment with `pip` installed
* Access to the internet to be able to pre-install `jsonschema` module (`pip install jsonschema`)

## Invokation and Response
The expected input object is a simple JSON object with one field:
```
{
  "name": "somename"
}
```
The response is a JSON object consisting of the following fields:
* name: The same value for the `name` field in your input object (echo'd back to you)
* requestId: The value of the `LambdaContext.aws_request_id` property when the function runs on AWS
* timestamp: A UTC timestamp in string format

Example response for the above input object:
```
{
  "name": "somename",
  "requestId": "2a35681d-5a58-4406-8137-4220aee9057f",
  "timestamp": "2022-02-03T23:14:19.705862"
}
```
## Testing
To test the `lambda_function.py` file simply run:
```
./run_tests.sh
```
This script assumes you're running this on a host (or Docker container) that has Python 3 (at least 3.7) installed and `pip` available.
