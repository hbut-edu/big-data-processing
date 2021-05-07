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

current_word = None
current_count = 0
word = None
for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)
    count=int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            sys.stdout.write("%s\t%s" % (current_word, current_count))

    current_count = count
    current_word = word

if word == current_word:
        sys.stdout.write("%s\t%s" % (current_word, current_count))