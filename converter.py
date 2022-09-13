import json
import csv
import sys

json_file = sys.argv[1]
csv_file = sys.argv[2]

with open(json_file) as f:
    data = json.load(f)

project = data["projet"]

with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Source", "Target"])
    for task in data["tache"]:
        parent = task["nom"]
        writer.writerow([project, parent])
        for subtask in task["sous_tache"]:
            child = subtask
            writer.writerow([parent, child])
