import json

student= {
    "name": 'venkat',
    'age': 34
}
s = json.load(student)
print('name {student.name}'.format(s.name))