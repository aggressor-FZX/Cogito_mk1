import base64
import json
import openai
import boto3

epub_file_path = '/path/to/your/ebook.epub'
base64_string = convert_epub_to_base64(epub_file_path)
def get_secret():
    secret_name = "openai"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    return get_secret_value_response['SecretString']

def convert_epub_to_base64(file_path):
    with open(file_path, 'rb') as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return encoded_string

# Example usage
print(base64_string)
def lambda_handler(event, context):
    
    key = json.loads(get_secret()).get("OPENAI_KEY")
    client = openai.OpenAI(api_key=key)
    #To do - get the image from the event
    #Send image to OpenAI and get response
    response = "response from openai not implemented"                      

    # Fix syntax error in print statement
    print("response is: {}".format(response))

    return {
        'statusCode': 200,
        'body': response.choices[0].message.content
    }
