import json
import Ext.openai as openai
import os
import Ext.boto3 as boto3
from PIL import Image
import base64

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


def image_to_base64(image_path):

    with open(image_path, "rb") as image_file:

        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        return encoded_string
