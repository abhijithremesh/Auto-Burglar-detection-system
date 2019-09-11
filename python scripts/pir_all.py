#!/usr/bin/env python3
import os
import RPi.GPIO as GPIO
from time import sleep, strftime, time
from datetime import datetime


PIR    = 13

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
#ts=time.time()
#st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

file = open("/home/pi/data_log.csv", "a")

if os.stat("/home/pi/data_log.csv").st_size == 0:
        file.write("Time,Event\n")


while True:
    i=GPIO.input(PIR)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if i==1:
        file.write(str(now)+","+str(i)+"\n")
        file.flush()
        sleep(8)
    elif i==0:
        file.write(str(now)+","+str(i)+"\n")
        file.flush()
        sleep(1)
