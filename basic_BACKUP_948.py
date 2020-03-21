<<<<<<< HEAD
import json  
  
person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
  
per_dict = json.loads(person)  
  
print(json.dumps(per_dict, indent = 5, sort_keys= True))  
=======
import json

student= {
    "name": 'venkat',
    'age': 34
}
s = json.load(student)
print('name {student.name}'.format(s.name))
>>>>>>> fea93d95ab555fbccdec4140b76d0b6def8d8b73
