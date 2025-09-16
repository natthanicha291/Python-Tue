import json

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(f"JSON String: {json_str}")

parsed_data = json.loads(json_str)
print(f"Parsed Data: {parsed_data}")
print(f"Name: {parsed_data['name']}, Age: {parsed_data['age']}")