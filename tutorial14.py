# Reading and Working with JSON Data (JavaScript Object Notation) - Python Advanced Tutorial #14

import json

j_string = '{"name": "Joe", "languages": "Python"}'

y = json.loads(j_string)
print("JSON string = ", y)

f = open("data.json", "r")

data = json.load(f)

for i in data["emp_details"]:
	print(i)

f.close()