import json

student= {
    "name": 'venkat',
    'age': 34,
    'sex':'male',
    'address':'andhra pradesh'
}
s = json.load(student)
print('name {student.name}'.format(s.name))