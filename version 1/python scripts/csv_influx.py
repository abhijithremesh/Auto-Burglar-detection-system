import pandas as pd
import datetime
import numpy as np

nodedata=pd.read_csv("/home/pi/data_fivemins.csv")
nodedata = nodedata[['Timestamp','WDay','Time_index','PIR']]
nodedata['Timestamp'] = pd.to_datetime(nodedata['Timestamp'])
nodedata.Timestamp = nodedata.Timestamp.apply(lambda x : (x-datetime.datetime(1970,1,1)).total_seconds())
nodedata['Timestamp'] = nodedata['Timestamp'].astype(np.int64)
nodedata.Timestamp = nodedata.Timestamp.astype(str)
exportcsv = nodedata.to_csv (r'/home/pi/data_fivemins_influx.csv', index = False, header=True)

