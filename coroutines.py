import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20  
}  

print(type(student))   # prints <class dict>
# dictionary to string
b = json.dumps(student)   # Serializing 
print(type(b))  # print <class str>
c = json.loads(b) # Deserializing 
print(type(c))   # prints < class dict>
print(c)

person = '{"Name": "Andrew","City":"English", "Number":90014,"Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
  
per_dict = json.loads(person)  
  
print(json.dumps(per_dict, indent = 5, sort_keys= True))  

print(3.14 , int(3.14))