# coding=utf-8

import sys

prev_key = 0
day_data = []

for data in sys.stdin:

    data = data.strip()
    record = data.split("\t")

    current_key = record[0]

    if prev_key != current_key:

        if len(day_data) != 0:
            sys.stdout.write(current_key + " " + str(max(day_data)) + "\n")

        day_data = []

    day_data.append(float(record[1]))
    prev_key = current_key
