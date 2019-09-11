#!/bin/bash

python3 fivemins.py
python3 csv_influx.py
python3 csv_to_line.py
curl -i -XPOST 'http://localhost:8086/write?db=motionsensor5min' --data-binary @data_fivemins_line.txt
