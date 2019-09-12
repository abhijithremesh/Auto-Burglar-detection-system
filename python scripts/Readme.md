Once the data from the three inputs: PIR, manual switch and MAC switch is parsed via the Nodered.
The data is then transformed in different formats to implement various approaches.

1.The data is first logged via NodeRed on a noderedlog.csv
  Timestamp,PIR,switch,mac 
2.The data is also logged via NodeRed onto the InfluxDB - motionsensor
3.This data is now available for visualisation in Grafana.
4.fivemins.py reads the noderedlog.csv and converts it into five minute format as data_fivemins.csv
  Timestamp,WDay,Time_index,PIR
5.csv_influx.py reads the data_fivemins.csv and converts the dd-mm-yyyy hh:mm:ss format to UNIX time format compatible for InfluxDB as data_fivemins_influx.csv
6.csv_to_line.py reads the data_fivemins_influx.csv and converts it into line format as data_fivemins.txt , ready for InfluxDB upload.
7.A curl command is then executed to write this data onto the InfluxDB , motionsensor5min.
8.weekly_upload.sh needs to be run every weekend which comprises of 4,5,6 and 7 in chronological order so that the data inside the motionsenor5min gets updated weekly.
9.motionsensor5min contains the historical data in the format Timestamp,WDay,Time_index,PIR.


avgdetections10min.py fetches the avg no of detections over 25 mins from the historical data stored in motionsensor5min.
avgdetections5min.py fetches the avg no of detections over 15 mins from the historical data stored in motionsensor5min.
sumdetections10min.py fetches the sum of detections over 25 mins from the historical data stored in motionsensor5min.
sumdetections5min.py fetches the sum of detections over 15 mins from the historical data stored in motionsensor5min.
sumnow5min.py fetches the sum of detections on that 5 min from the historical data stored in motionsensor5min.
meannow5min.py fetches the avg detections on that 5 min from the historical data stored in motionsensor5min.

When a timestamp is detected, all the above python scripts are run and queries these info and these info from the historical data is then compared with the currrent detections to make a prediction.

A statistical method based on the interquartile region and standard deviation approach is also implemented on the historical data stored in motionsensor5min.
boxplotprediction.py corresponds to the boxplot approach.
stdprediction.py corresponds to the standard deviation approach.


weeklysummary_boxplot.py plots the weekly summary of detected timestamps based on the noderedlog.csv
