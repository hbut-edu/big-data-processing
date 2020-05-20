# coding=utf-8

import sys

for data in sys.stdin:

    data = data.strip()

    day_data = data.split(',')

    key = hash(data)

    for value in day_data:

        sys.stdout.write("%s\t%s\n" % (key, value))
