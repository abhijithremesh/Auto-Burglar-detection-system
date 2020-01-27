from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
import sys
import datetime
import json


#print(len(sys.argv))
#print(sys.argv[1])
a = sys.argv[1]
#print(a)
b = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')

time = b.time()
day = b.date().weekday()
if day ==6:
        day = day - 5
else:
        day = day + 2
#print (day)
#print(time)
h = time.hour
m = time.minute
Time_index = h*60 + m
Time_index = Time_index/5
#print ( Time_index)
Time_index_min = Time_index - 2
Time_index_max = Time_index + 2
#print(Time_index_min)
#print(Time_index_max)


client = InfluxDBClient(host='192.168.0.36', port=8086)

params ={"day":day,"Time_index_min" : Time_index_min, "Time_index_max":Time_index_max}


#Result = client.query('SELECT MEAN("PIR") FROM "motionsensor5min"."autogen"."sensor" WHERE "WDay" = $day  AND "Time_index" >= $Time_index_min  AND "Time_index" <= $Time_index_max ')
Result = client.query('select mean(PIR) from "motionsensor5min"."autogen"."sensor" ' 'where WDay=$day ' 'and Time_index >=$Time_index_min ' 'and Time_index<=$Time_index_max ', params={"params":json.dumps(params)})
points = Result.get_points()
for point in points:
        print(point['mean'])
#        kopp = point['mean']
#print(kopp)



