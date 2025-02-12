import json
import sys

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


if len(sys.argv) == 4:
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(tests_path) as tests_file:
        tests=json.load(tests_file)

    with open(values_path) as values_file:
        values=json.load(values_file)

    set_res(tests['tests'])

    with open(report_path, 'w') as report:
        json.dump(tests, report)
else:
    print('Не указаны пути к файлам!')