import json

with open('data.json', 'r') as file:
    data = json.load(file)

list = [key for key in data.keys()]

print(list)