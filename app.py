import json
import Ext.openai as openai
import os
import Ext.boto3 as boto3

AWS_BUCKET = "aws-sam-cli-managed-default-samclisourcebucket-ipgxtoe8d3vw"

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
                           
    s3 = boto3.client('s3')
    #print("event is: {}".format(event), "/n")

    paramsys = {"role": "system", "content": "you are a profeessional programmer and you are showing me what a good resume looks like. "}
    param_user = {"role": "user", "content": event['text']}
    mod = "gpt-4"
    max_tok = 4000
    response = client.chat.completions.create(messages=[paramsys,param_user], model=mod, max_tokens=max_tok, stop=None, temperature=0.7, top_p=1 )

    output_stream = response.choices[0].message.content
    s3.put_object(Bucket=AWS_BUCKET, Key='Ansers_response.txt', Body=output_stream)

#    print("response is: {}".format(response))
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,OPTIONS',  # Allow POST and OPTIONS methods
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',  # Allow necessary headers
            'Access-Control-Allow-Credentials': True
        },
        'body': response.choices[0].message.content
}