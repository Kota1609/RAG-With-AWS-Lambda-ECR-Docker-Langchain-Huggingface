import boto3
import json

print("Imported successfully...")

# Define the prompt
prompt = "Generate a description for a person standing on Mount Everest."

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Prepare the payload
payload = {
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.7,
    "top_p": 0.9,
}

# Serialize payload to JSON
body = json.dumps(payload)

# Use the inference profile ARN for Llama 3.2 11B Vision Instruct
inference_profile_arn = "arn:aws:bedrock:us-east-2:241533121157:inference-profile/us.meta.llama3-2-11b-instruct-v1:0"

# Invoke the model
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
