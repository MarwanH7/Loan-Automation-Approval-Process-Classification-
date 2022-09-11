## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


base_url = 'http://192.168.2.13:5555/' #base url local host

json_data = [
    {"Gender":1, 
    "Married":1, 
    "Education":1, 
    "Self_Employed":0,
    "ApplicantIncome":5849,
    "CoapplicantIncome" :1508.0,
    "LoanAmount":50.0,
    "Loan_Amount_Term":360,
    "Credit_History":1.0,
    "Property_Area":0 }
              
]


# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')

