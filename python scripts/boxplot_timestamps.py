import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

data=pd.read_csv("/home/pi/WeekwithDate.csv")
data['Timestamp'] = data['Day'] + ' ' + data['Time']
data = data[['Timestamp','Day','Time','Detected','Person present']]
data = data.rename(columns={'Detected': 'PIR', 'Person present': 'Switch'})
data= data.drop('Time', 1)
data= data.drop('Day', 1)
data = data.drop_duplicates()
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S')

#Week Summary of Detection Tinestamps through Exploratory Data Analysis
data_detections = data.drop('Switch',1)
weeks = [g for n, g in data_detections.groupby(pd.Grouper(key='Timestamp',freq='W'))]
data_firstweek = weeks[0]
data_secondweek = weeks[1]
data_thirdweek = weeks[2]


data_firstweek['Day'] = data_firstweek['Timestamp'].dt.day_name()
data_firstweek = data_firstweek.set_index('Timestamp')
data_firstweek_detectedtimestamps = data_firstweek[(data_firstweek['PIR']==1)]
data_firstweek_detectedtimestamps = data_firstweek_detectedtimestamps.reset_index(drop=False)
data_firstweek_detectedtimestamps['Timestamp'] = data_firstweek_detectedtimestamps['Timestamp'].astype(str)
data_firstweek_detectedtimestamps['Date'], data_firstweek_detectedtimestamps['Time'] = data_firstweek_detectedtimestamps['Timestamp'].str.split(' ', 1).str
data_firstweek_detectedtimestamps['Time'] = data_firstweek_detectedtimestamps['Time'].map(lambda x: x.replace(":",""))
data_firstweek_detectedtimestamps['Time'] = data_firstweek_detectedtimestamps['Time'].astype(int)

data_secondweek['Day'] = data_secondweek['Timestamp'].dt.day_name()
data_secondweek = data_secondweek.set_index('Timestamp')
data_secondweek_detectedtimestamps = data_secondweek[(data_secondweek['PIR']==1)]
data_secondweek_detectedtimestamps = data_secondweek_detectedtimestamps.reset_index(drop=False)
data_secondweek_detectedtimestamps['Timestamp'] = data_secondweek_detectedtimestamps['Timestamp'].astype(str)
data_secondweek_detectedtimestamps['Date'], data_secondweek_detectedtimestamps['Time'] = data_secondweek_detectedtimestamps['Timestamp'].str.split(' ', 1).str
data_secondweek_detectedtimestamps['Time'] = data_secondweek_detectedtimestamps['Time'].map(lambda x: x.replace(":",""))
data_secondweek_detectedtimestamps['Time'] = data_secondweek_detectedtimestamps['Time'].astype(int)

data_thirdweek['Day'] = data_thirdweek['Timestamp'].dt.day_name()
data_thirdweek = data_thirdweek.set_index('Timestamp')
data_thirdweek_detectedtimestamps = data_thirdweek[(data_thirdweek['PIR']==1)]
data_thirdweek_detectedtimestamps = data_thirdweek_detectedtimestamps.reset_index(drop=False)
data_thirdweek_detectedtimestamps['Timestamp'] = data_thirdweek_detectedtimestamps['Timestamp'].astype(str)
data_thirdweek_detectedtimestamps['Date'], data_thirdweek_detectedtimestamps['Time'] = data_thirdweek_detectedtimestamps['Timestamp'].str.split(' ', 1).str
data_thirdweek_detectedtimestamps['Time'] = data_thirdweek_detectedtimestamps['Time'].map(lambda x: x.replace(":",""))
data_thirdweek_detectedtimestamps['Time'] = data_thirdweek_detectedtimestamps['Time'].astype(int)


fig1 = data_firstweek_detectedtimestamps.boxplot(by="Day", column="Time",showfliers=True)
plt.title("First week detections")
plt.suptitle("")
plt.show()
fig2 = data_secondweek_detectedtimestamps.boxplot(by="Day", column="Time",showfliers=True)
plt.title("Second week detections")
plt.suptitle("")
plt.show()
fig3 = data_thirdweek_detectedtimestamps.boxplot(by="Day", column="Time",showfliers=True)
plt.title("Third week detections")
plt.suptitle("")
plt.show()
fig1.figure.savefig("/home/pi/image/firstweekdetectedtimestamps.png")
fig2.figure.savefig("/home/pi/image/secondweekdetectedtimestamps.png")
fig3.figure.savefig("/home/pi/image/thirdweekdetectedtimestamps.png")
