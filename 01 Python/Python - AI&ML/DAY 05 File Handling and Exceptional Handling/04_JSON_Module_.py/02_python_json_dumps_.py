import json

data = {
    "name": "Arpit",
    "age": 20,
    "skills": ["Python", "AI"],
    "active": True,
    "murder_attempts" : None
}

json_data = json.dumps(data)
print(type(json_data), json_data)
