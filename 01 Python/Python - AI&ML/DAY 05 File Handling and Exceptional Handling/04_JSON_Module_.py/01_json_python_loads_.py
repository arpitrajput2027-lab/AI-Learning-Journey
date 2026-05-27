# JSON Module , Python objects ↔ JSON data convert karta hai
# JSON vs Python data types
'''
object - Dic
array  - list
string - string
null   - None
true   - True
false  - false
'''
#  JSON string → Python (loads)
import json

json_str = '{"name": "Arpit", "age": 20, "active": true,"murder_attempts" : null }'
data = json.loads(json_str)

print(type(json_str) , type(data))
print(data)


