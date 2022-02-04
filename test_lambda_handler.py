import unittest
from lambda_function import lambda_handler
import json
import jsonschema
from jsonschema import validate

lambdaResponseSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "requestId": {"type": "string"},
        "timestamp": {"type": "string"},
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=lambdaResponseSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

class LambdaInputData:
    def __init__(self, aws_request_id = "", eventName = ""):
        self.aws_request_id = aws_request_id
        self.testEvent = { "name":eventName }

def assertNotEmpty(self, obj):
    self.assertTrue(obj)

class TestLambdaHandler(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inputData = LambdaInputData("1234567890abcdef", "testName")
        self.resp = lambda_handler(self.inputData.testEvent, self.inputData) # LambdaInputData object will act as the LambdaContext object

    def test_response_is_valid_json(self):
        self.assertTrue(validateJson(self.resp))

    def test_response_name_is_correct(self):
        self.assertEqual(self.resp['name'], self.inputData.testEvent['name'])

    def test_response_requestId_is_correct(self):
        self.assertEqual(self.resp['requestId'], self.inputData.aws_request_id)

    def test_response_has_timestamp(self):
        assertNotEmpty(self, self.resp['timestamp'])

if __name__ == '__main__':
    unittest.main()
