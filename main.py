import random
import csv
import json
import os

MIN_ELEMENT = -1000
MAX_ELEMENT = 1000

def decor_json(func):
    def wrapper(*args, **kwargs):
        if os.path.isfile('file.json'):
            with open ('file.json', 'r', encoding='UTF-8') as file:
                data = json.load(file)
        else:
            data = []
        res = func(*args, **kwargs)
        item = {f'{args}':res}
        data.append(item)
        with open ('file.json', 'w', encoding='UTF-8') as file:
                json.dump(data,file, indent=4, ensure_ascii=False)
        return res
    return wrapper


def decor_csv(func):
    def wrapper():
        with open('file.csv', 'r', encoding='UTF-8', newline='') as file:
            data = csv.reader(file)
            for i, line in enumerate(data):
                if i == 0:
                    continue
                else:
                    a, b, c = map(int, line)
                    res = func(a, b, c)
        return res   
    return wrapper


@decor_csv
@decor_json
def quadr(a, b, c):
    descr = b**2 - 4*a*c
    if descr < 0:
        return 'Нет решений'
    elif descr == 0:
        x = -b/(2*a)
        return x
    else:
        x1 = (-b + descr ** 0.5)/(2*a)
        x2 = (-b - descr ** 0.5)/(2*a)
        return (x1, x2)


def csv_generation():
    list_csv = []
    line_count = random.randint(100, 1000)
    for _ in range(line_count):
        a ,b , c = random.sample(range(MIN_ELEMENT, MAX_ELEMENT), 3)
        list_csv.append({'a': a, 'b': b, 'c': c})
    with open('file.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['a','b','c'])
        writer.writeheader()
        writer.writerows(list_csv)


quadr()