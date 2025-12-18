import os
import sys
import requests

#importing environment and token variables from generic_constants.py
# current_working_directory = os.getcwd()
# rood_dir = os.path.abspath(os.path.join(current_working_directory))
# print(current_working_directory)
# sys.path.insert(0, rood_dir)

# from constants.generic_constants import environment, token

#GET Calls
def api_name():
    head = {
        "Authorization": f"Bearer ey.........",
        "Content-Type": "application/json"
    }
    payload = {
        "start": "2025-11-01",
        "end": "2025-11-26",
        "mode": "MONTH"
    }
    response = requests.get(
        f"api_url",
        json=payload, headers=head, verify=False 
    )
    if response.status_code==200:
        return(response.status_code,response.json())
    else:
        print(f"Failed with status code: {response.status_code}")
        return(response.status_code)
    
#POST Calls
def api_name():
    head = {
        "Authorization": f"Bearer ey.........",
        "Content-Type": "application/json"
    }
    data2 ={
        "page": 0,
        "search": "",
        "month": ""
    }
    payload = {
        "start": "2025-11-01",
        "end": "2025-11-26",
        "mode": "MONTH"
    }
    response = requests.post(
        f"api_url",
        headers=head, json=payload, data=json.dumps(data2), verify=False 
    )
    if response.status_code==200:
        return(response.status_code,response.json())
    else:
        print(f"Failed with status code: {response.status_code}")
        return(response.status_code)