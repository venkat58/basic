import json
import time

student= '{"name":"venkat","age":34,"sex":"male"}'
s = json.loads(student)
print('name {0}'.format(s['name']))
print(f"function format name {s['name']}")
print(time.localtime(time.time()))  
