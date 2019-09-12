# Intrusion-detection-system
A Smart Home Implementation

Hybrid Smart Motion Detection

The main goal of the project is to detect the presence of Intruder based on the detections from the PIR sensor and to predict if a timestamp detected is a abnormal or normal detection.The main challenge is to obtain a prediction only by considering the input from PIR sensor and without involving the use of camera as installing cameras within home would pose a privacy threat for the user. The project mainly uses the following hardware components - Raspberry Pi, HC-SR501 (PIR sensor).

The input dynamics of the system include the detections from the PIR sensor that is, 0 if no detection and 1 if there is detection and a online switch functionality which is set manually by the user. He may set the switch state to 1 when he is present and 0 when he is absent and a another switch functionality which would be set to 1 when the specific MAC address of the user's mobile is found on the network and would be zero when the MAC address of the mobile is not found on the network. As a result, the decision of a timestamp being detected from a intruder/the user takes into account, three major inputs : one from PIR sensor , one from manual switch, one from MAC switch ; Each of which can have values either 0 or 1.

There are three approaches being considered to decide the type of detection and to decide the status of home.
1.Dynamic Historical data.
2.Interquartile region approach
3.Standard deviation approach.

We use nodered for the data parsing from these three inputs and for small scale visulaisation.
We use InfluxDB for storing the real time data.
We also use Grafana for visualisations.


We have two databases inside InfluxDB
1. one for storing the real time detetcions - motionsensor. 
2. one for implementing the dynamic historical data approach where data is stored in another format suitable for query search on historical data - motionsensor5min.
