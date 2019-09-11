import RPi.GPIO as GPIO
from time import sleep, strftime, time
import datetime


PIR    = 13


GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
#ts=time.time()
#st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')




 



with open("/home/pi/detections.csv", "a") as log:
	while True:
		i=GPIO.input(PIR)
		log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(i)))
		if i == 1:
			print i
			
		else:
			print i
			
