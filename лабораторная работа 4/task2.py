# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_name, json_name) -> None:
    csvfile = open(csv_name, 'r')
    jsonfile = open(json_name, 'w+')
    conv = csv.DictReader(csvfile)
    json.dump([row for row in conv], jsonfile, indent=4)
    # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end='')
