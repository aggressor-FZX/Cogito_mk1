# Cogito_mk1
The first Cogito AWS Lambda build. This is an AWS application made to run in the VS code enviornment. It uses a Docker image to reproduce the AWS enviornment for running locally and testing functionality. It requires a AWS profile and an S3 bucket. Two lambda functions were created here for test. Eventually they will be envokeed by another aws service which can be accesses from the internet.

I have app.py lambda function readinging in a file my_even.json which openAI responds to. At the time of this writing it creates a resume for me. This was done for testing. I gave it a large file of information about me and other with a job posting. It works well, but I will have the same question sent to different chat versions for comparisons.

The other lambda imageScan_lambda takes an image and answers questions about it. It will be used to summerize text pdf books. I want it to tell me what the chapters are and the important points of each chapter. This file needes to be turned into a byte stream for openAI vision preview to work. Haven't had much luck with this as the size limit "message window" prevents me from sending proper text books.

Example Resume output:

Jeff Calderon

Professional Summary: Research Physicist with 3 years of experience in performing studies related to radiation detection units for border and law enforcement. Skilled in presenting results from computer models and statistical analysis to validate software. Effective officer with technical problem-solving skills and proficiency in Python tools development for hydrographic data processing. Experienced Aerospace Equipment Mechanic with analytical ability to interpret schematics, diagrams, and technical documents. Excellent communicator with expertise in modern computing practices such as Python, Linux, AWS, C++, Docker, and network security.

Experience: National Oceanic & Atmospheric Administration (NOAA) - Commissioned Officer - Jan 2016 - May 2023

Acquired hydrographic data for the Office of Coast Survey, utilizing GIS software and Python-based automations for data processing.
Configured the Science Computing System and managed sensor connections for data analysis and system validation.
Implemented Python programming for shipboard problem-solving and workflow automation initiatives using Smartsheet.
Praxis, Inc. - Research Physicist - Jan 2014 - Jan 2016

Conducted studies on radiation detection units, presenting results to validate software and secure funding.
Supported simulations to predict active interrogation procedures and passive detection of WMD/radiological devices.
Led the transformation of technical information into digestible formats for non-physicists and facilitated communication.
University of Maryland - Faculty Assistant Researcher - Jan 2013 - Apr 2015

Designed software for data analysis and publication quality plots in particle physics experiments.
Co-authored publications on experiments conducted at the Large Hadron Collider, contributing to scientific knowledge.
Developed simulations for calorimetry studies and efficiency quantifications with programming skills in C++ and ROOT.
United States Air Force - Aerospace Ground Equipment Mechanic - May 2002 - Jan 2010

Administered equipment databases, supervised maintenance operations, and ensured aircraft data availability.
Maintained aircraft maintenance records supporting F-16 fighter jets and presented readiness statistics to base leadership.
Education & Certifications:

Bachelor of Science in Professional Physics, University of Maryland
Cyber Security Analyst Certificate, Everett Community College
Digital Forensics, SCADA, Network Defense, Ethical Hacking
AWS, C++, Python, Linux, Cloud Computing, Network Security
Skills:

Python, C++, Linux, AWS, Docker, Network Security, Git, REST APIs, Version Control
Analytical thinking, growth mindset, strong interpersonal and communication skills
Proficient in Microsoft Office, sonar acquisition hardware/software, and AWS Lambda
LinkedIn: linkedin.com/in/jeffdcalderon Contact: jeff.d.calderon@gmail.com

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```


* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
Cogito_mk1$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
Cogito_mk1$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
Cogito_mk1$ sam local start-api
Cogito_mk1$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
Cogito_mk1$ sam logs -n HelloWorldFunction --stack-name "cogito_mk1" --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
Cogito_mk1$ pip install -r tests/requirements.txt --user
# unit test
Cogito_mk1$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
Cogito_mk1$ AWS_SAM_STACK_NAME="cogito_mk1" python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "cogito_mk1"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
