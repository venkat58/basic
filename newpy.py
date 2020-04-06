import json  
import pandas as pd
# Key:value mapping  

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}

with open('data.json' , 'w') as savef:
     json.dump( person_dict , savef)

try:
    with open('data.json') as f:
        data = json.load(f)
except FileNotFoundError as a:
    data = a

print(data)


person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)