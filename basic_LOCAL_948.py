import json  
  
person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
  
per_dict = json.loads(person)  
  
print(json.dumps(per_dict, indent = 5, sort_keys= True))  