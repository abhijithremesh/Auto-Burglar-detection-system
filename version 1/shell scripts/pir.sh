#!/bin/bash

python3 csv_influx.py
python3 csv_to_line.py
#python3 motion_csvtoline.py
#python3 detection_csvtoline.py
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE motionsensor5min"
#curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE sensordetectiondb"
curl -i -XPOST 'http://localhost:8086/write?db=motionsensor5min' --data-binary @data_fivemins_line.txt
#curl -i -XPOST 'http://localhost:8086/write?db=sensordetectiondb' --data-binary @detectionfile.txt
