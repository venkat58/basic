import json

student= {
    "name": 'venkat',
    'age': 34,
    'sex':'male',
    'address':'ylm'
}
s = json.load(student)
print('name {student.name}'.format(s.name))