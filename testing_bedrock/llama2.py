import os
import json
import sys
import boto3

print("imported successfully...")

prompt = """
        You are a cricket expert now just tell me when RCB will win the IPL?
"""

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Prepare the payload
payload = {
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9,
}

# Serialize payload to JSON
body = json.dumps(payload)

# Specify the inference profile ARN
inference_profile_arn = "arn:aws:bedrock:us-east-2:241533121157:inference-profile/us.meta.llama3-2-11b-instruct-v1:0"

# Invoke the model using the inference profile ARN as the modelId
response = bedrock.invoke_model(
    body=body,
    modelId=inference_profile_arn,
    accept="application/json",
    contentType="application/json"
)

# Parse and print the response
response_body = json.loads(response['body'].read())
response_text = response_body.get("generation", "No response generated.")
print(response_text)
