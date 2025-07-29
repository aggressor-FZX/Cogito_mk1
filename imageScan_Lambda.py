import json
import Ext.openai as openai
import os
import Ext.boto3 as boto3
import base64
import fitz

ROOT_DIR = 'cogito'
PDF_FILE = "Trim Test PDF.pdf"
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


def pdf_to_base(pdf_file, s3_client):
    try:

        with open(pdf_file, 'rb') as myFile:

            base64_bytes = base64.b64encode(myFile.read()).decode('utf-8')

    except FileNotFoundError:
        print(f"Error: File '{pdf_file}' not found.")

    s3_client.put_object(
        Body=base64_bytes,
        Bucket=AWS_BUCKET,
        Key=PDF_FILE+'base64'
    )
    path_to_64 = f"s3://{AWS_BUCKET}/{PDF_FILE}bas64"

    return path_to_64


def get_s3Client(AWS_BUCKET, pdf_loc):
    #allows for the use of s3 bucket writing 
    s3_client = boto3.client('s3')

    # Get the job status
    response = s3_client.get_object(Bucket=AWS_BUCKET, Key=pdf_loc)
  
    file_content = response['Body'].read()

    #Create a temporary file to store the PDF
    with open('/tmp/tmp.pdf', 'wb') as temp_file:
        temp_file.write(file_content)

    # TO DO : cut the pdf into smaller files

    return s3_client


#entry point of the lambda function
    #To do 
    #get the pdf from the event rather than hard coded path
def lambda_handler(event, context):

    print("event is: {}".format(event)) #print("context is: {}".format(context))

    s3_client = get_s3Client(AWS_BUCKET, ROOT_DIR+"/"+PDF_FILE)
    path_to_64 = pdf_to_base('/tmp/tmp.pdf', s3_client)
   # path_to_64 = "https://aws-sam-cli-managed-default-samclisourcebucket-ipgxtoe8d3vw.s3.amazonaws.com/Trim+Test+PDF.pdfbas64"

    key = json.loads(get_secret()).get("OPENAI_KEY")
    client = openai.OpenAI(api_key=key)

   #input base64 to OpenAI and get response
    response = client.chat.completions.create(
       model="gpt-4-vision-preview",
       messages=[
           {
           "role": "user",
           "content": [
               {"type": "text", "text": "what are the chapter titles and what page are they on? answer in title: page format"},
               { "type": "image_url",
                 "image_url": {
                 "url": f"data:jpeg;base64,{path_to_64}",
                 "detail": "low"
               },
               },
           ],
           }
       ],
       max_tokens=10000,
       )

    print(response.choices[0])
    print("response is: {}".format(response))

    return {
       'statusCode': 200,
        'body': response.choices[0].message.content
    }
