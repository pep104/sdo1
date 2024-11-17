import json

f = open('input.json')


def task(file) -> float:
    file_json = json.load(file)
    count = 0
    for i in file_json:
        count += i['score'] * i['weight']
    return round(count, 3)


print(task(f))

f.close()
