import json

student= {
    "name": 'venkat',
    'age': 34,
    'sex':'male'
}
s = json.load(student)
print('name {student.name}'.format(s.name))
print('hi')