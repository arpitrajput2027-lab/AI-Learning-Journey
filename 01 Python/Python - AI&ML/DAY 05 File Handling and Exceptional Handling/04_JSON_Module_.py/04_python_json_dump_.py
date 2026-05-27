import json

data = {
    "name": "Arpit",
    "active": True,
    "murder_attempts" : None
}

with open("JS_DATA.json" , 'w') as f:
   json.dump(data , f , indent=4 , sort_keys=True)