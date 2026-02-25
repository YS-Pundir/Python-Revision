import json


response='''{

  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }

}'''

data=json.loads(response)

print("Request ID : ",data["id"])
print("Status : ",data["status"])
print("Text Result : ",data["result"]["text"])
print("Confidence Score : ",data["result"]["confidence"])

if data["result"]["confidence"]<0.9:
    print("Warning !!! :  Your confidnece score is below the minimum amount")