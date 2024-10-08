# -*- coding: utf-8 -*-
"""TS - AI in Cybersecurity.ipynb

Automatically generated by Colab.

# Setup

Please run the following code and do **NOT** modify.
"""

import urllib.request

# Upload files
requirements_url = "https://raw.githubusercontent.com/IBM/taxinomitis/master/resources/mlforkids-numbers-requirements.txt"
urllib.request.urlretrieve(requirements_url, "requirements.txt")

MLforKidsNumbers_url = "https://raw.githubusercontent.com/IBM/taxinomitis/master/resources/mlforkidsnumbers.py"
urllib.request.urlretrieve(MLforKidsNumbers_url, "MLforKidsNumbers.py")

# Install packages using pip
!pip install -r requirements.txt

# Import module from uploaded Python file
from MLforKidsNumbers import MLforKidsNumbers

"""# Your Code

The cell block below is where we will be adding our code.
"""

# Your code goes here
project = MLforKidsNumbers(
    key="518f74c0-7844-11ef-8003-7f5aefbb53b6d801a89e-2f05-4b88-8cff-1626ffe2372a",
    modelurl="https://mlforkids-newnumbers.j8ahcaxwtd1.au-syd.codeengine.appdomain.cloud/saved-models/f3c0a230-7841-11ef-bcfc-1d7d35bf12ac/status"
)

addrType = input("Address type -- IP addr or DNS name : ")
urlLength = input("URL length -- <54 chars or is 54-75 or >75 chars : ")
shortening = input("Shortening -- yes or no : ")
includesA = input("Includes @ -- yes or no : ")
portNumber = input("Port number -- standard or non-standard : ")
domaninAge = input("Domain Age -- < 6 month or older : ")
redirects = input("Redirects -- <= 4 or > 4 : ")
domainReg = input("Expiring -- expiring or not : ")


# CHANGE THIS to something you want your
# machine learning model to classify
testvalue = {
    "address type" : addrType,
    "url length" : urlLength,
    "shortening" : shortening,
    "includes @" : includesA,
    "port number" : portNumber,
    "domain age" : domaninAge,
    "redirects" : redirects,
    "domain reg" : domainReg,
}

response = project.classify(testvalue)
top_match = response[0]

label = top_match["class_name"]
confidence = top_match["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))
