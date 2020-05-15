#!/usr/bin/env python3
import csv
import datetime
import time
import sys

def string2timestamp(strValue):
    try:
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S,%f")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000
        return timeStamp
    except ValueError as e:
       print(f"ERROR {str(e)}")

filename=sys.argv[1]
r = csv.reader(open(f'{filename}')) # Here your csv file
lines=[]
for line in r:
    datetime_str = f"{line[0]}.{line[1]}"
    lines.append([datetime_str,line[2],line[3],line[4]])

writer = csv.writer(open(f'{filename}_statics.csv', 'w'))
writer.writerows(lines)