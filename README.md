# Cogito_mk1
The first Cogito AWS Lambda build. 
This is an AWS application made to run in the VS code enviornment. It uses a Docker image to reproduce the AWS enviornment for running locally and testing functionality. It requires a AWS profile and an S3 bucket. Two lambda functios were created here for test. Eventually they will be envokeed by another aws service which can be accesses from the internet. 

I have app.py lambda function readinging in a file my_even.json which openAI responds to. At the time of this writing it creates a resume for me. This was done for testing. I gave it a large file of information about me and other with a job posting. It works well, but I will have the same question sent to different chat versions for comparisons. 

The other lambda imageScan_lambda takes an image and answers questions about it. It will be used to summerize text pdf books. I want it to tell me what the chapters are and the important points of each chapter. This file needes to be turned into a byte stream for openAI vision preview to work. Haven't had much luck with this as the size limit "message window" prevents me from sending proper text books.

Example Resume output:

Jeff Calderon

Professional Summary:
Research Physicist with 3 years of experience in performing studies related to radiation detection units for border and law enforcement.
 Skilled in presenting results from computer models and statistical analysis to validate software. Effective officer with technical 
 problem-solving skills and proficiency in Python tools development for hydrographic data processing. Experienced Aerospace Equipment Mechanic 
 with analytical ability to interpret schematics, diagrams, and technical documents. Excellent communicator with expertise in modern computing 
 practices such as Python, Linux, AWS, C++, Docker, and network security.

Experience:
National Oceanic & Atmospheric Administration (NOAA) - Commissioned Officer - Jan 2016 - May 2023
- Acquired hydrographic data for the Office of Coast Survey, utilizing GIS software and Python-based automations for data processing.
- Configured the Science Computing System and managed sensor connections for data analysis and system validation.
- Implemented Python programming for shipboard problem-solving and workflow automation initiatives using Smartsheet.

Praxis, Inc. - Research Physicist - Jan 2014 - Jan 2016
- Conducted studies on radiation detection units, presenting results to validate software and secure funding.
- Supported simulations to predict active interrogation procedures and passive detection of WMD/radiological devices.
- Led the transformation of technical information into digestible formats for non-physicists and facilitated communication.

University of Maryland - Faculty Assistant Researcher - Jan 2013 - Apr 2015
- Designed software for data analysis and publication quality plots in particle physics experiments.
- Co-authored publications on experiments conducted at the Large Hadron Collider, contributing to scientific knowledge.
- Developed simulations for calorimetry studies and efficiency quantifications with programming skills in C++ and ROOT.

United States Air Force - Aerospace Ground Equipment Mechanic - May 2002 - Jan 2010
- Administered equipment databases, supervised maintenance operations, and ensured aircraft data availability.
- Maintained aircraft maintenance records supporting F-16 fighter jets and presented readiness statistics to base leadership.

Education & Certifications:
- Bachelor of Science in Professional Physics, University of Maryland
- Cyber Security Analyst Certificate, Everett Community College
- Digital Forensics, SCADA, Network Defense, Ethical Hacking
- AWS, C++, Python, Linux, Cloud Computing, Network Security

Skills:
- Python, C++, Linux, AWS, Docker, Network Security, Git, REST APIs, Version Control
- Analytical thinking, growth mindset, strong interpersonal and communication skills
- Proficient in Microsoft Office, sonar acquisition hardware/software, and AWS Lambda

LinkedIn: linkedin.com/in/jeffdcalderon
Contact: jeff.d.calderon@gmail.com
