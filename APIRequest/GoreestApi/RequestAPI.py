import requests
import random
import json
import string
base_url= "https://petstore.swagger.io"

def get():
    url = base_url + "/v2/store/inventory"
    headers = {"accept" : "application/json"}
    res = requests.get(url, headers=headers)
    assert  res.status_code == 200
    json_data = res.json()
    json_str = json.dumps(json_data, indent=4)
    print("data is : ", json_str)

get()