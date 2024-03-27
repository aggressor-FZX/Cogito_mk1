import json
import Ext.openai as openai
import os
import Ext.boto3 as boto3

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
    # Remove unnecessary print statement
    # openai.api_key = get_secret(
    key = json.loads(get_secret()).get("OPENAI_KEY")
    client = openai.OpenAI(api_key=key)
                           
    print("event is: {}".format(event), "/n")
    paramsys = {"role": "system", "content": "you are a helpful assistant"}
    param_user = {"role": "user", "content": event['text']}
    mod = "gpt-3.5-turbo"

    response = client.chat.completions.create(messages=[paramsys,param_user], model=mod)
    # Fix syntax error in print statement
    print("response is: {}".format(response))
    return {
        'statusCode': 200,
        'body': response.choices[0].message.content
    }