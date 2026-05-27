info = {
    "name":"Arpit Rajput",
    "course":"Python for AI & ML",
    "age":19,
    "city":"CHD",
    "cgpa": [8.5,8.3,7.5],
    3.14: "Pi Value"
}

info_keys = list(info.keys())
print(type(info_keys))  # <class 'list'>

info_values = info.values()
print(type(info_values))  # <class 'dict_values'>

print("Keys:", info_keys) 
print("-----")
print("Values:", info_values)
print("-----")


print(info.items())  # dict_items of key-value pairs
print("-----")

# Difference Between info.get("name") and info["name"] -->>
# info.get("name") returns None if the key doesn't exist,
#  while info["name"] raises a KeyError.
print(info.get("name"))  # Accessing value using get() method
print(info["name"])     # Accessing value using [] operator
print("-----")

print(info.get("xyz"))  # Returns None if key doesn't exist
print(info["xyz"])  # This will raise a KeyError