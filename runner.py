import csv
import json

data = []
with open('files/sample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        # descr = rows['Description']
        temp = {}
        temp['description'] = {}
        temp['description']['name'] = rows['Description']
        temp['description']['class_event'] = rows['class']
        temp['description']['event_label'] = rows['event-label']
        data.append(temp)

with open('files/translation.json', 'w') as fout:
    json.dump(data, fout)
            