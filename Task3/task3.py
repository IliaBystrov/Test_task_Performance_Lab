import json

def set_res(item):
    for i in item:
        if 'values' not in i:
            for k in values['values']:
                if i['id'] == k['id']:
                    i['value'] = k['value']
                    break
        else:
            for k in values['values']:
                if i['id'] == k['id']:
                    i['value'] = k['value']
                    break
            set_res(i['values'])


#Входные данные
tests_path = 'tests.json'
values_path = 'values.json'
report_path = 'report.json'

with open(tests_path) as tests_file:
    tests=json.load(tests_file)

with open(values_path) as values_file:
    values=json.load(values_file)

set_res(tests['tests'])

with open('report.json', 'w') as report:
    json.dump(tests, report)