# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:53:34 2019

@author: bcubrich
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:02:20 2018

@author: kweber
"""

from netCDF4 import Dataset
#import matplotlib
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np         #didn't even use numpy!!! HA!
#import seaborn as sns
#from tkinter import Tk

#from tkinter.filedialog import askdirectory
import os
#import xarray as xr

#def get_dat():
#    root = Tk()
#    root.withdraw()
#    root.focus_force()
#    root.attributes("-topmost", True)      #makes the dialog appear on top
#    filename = askdirectory()      # Open single file
#    root.destroy()
#    root.quit()
#    return filename

start=pd.datetime.utcnow()
today=pd.datetime.utcnow().strftime("%Y%m%d")
directory='C:/BLViewData'
out_dir='C:/Processed_netCDF'

#i=0

ceil_files=os.listdir(directory)
text_files=os.listdir(out_dir)

ceil_file_names=[x.strip('.nc') for x in ceil_files if '.nc' in x and today not in x and 'L3' in x and 'DEFAULT' in x]
text_file_names=[x.strip('.csv') for x in text_files if '.csv' in x and today not in x and 'L3' in x and 'DEFAULT' in x]

missing_text = np.setdiff1d(ceil_file_names,text_file_names, assume_unique=True)

missing_text_files=[x+'.nc' for x in missing_text]

#%%
for filename in missing_text_files:     #loop through files in user's dir
    print(filename)
    if filename.endswith(".nc"):
#        runstart=pd.datetime.utcnow()
        rootgrp3 = Dataset(directory+'/'+filename, "r", format="NETCDF4")
#        print (rootgrp3.dimensions.keys())
        #print (rootgrp3.data_model)
        
        # this is the variable we want!!
        mlh_2 = rootgrp3.variables['Mean_Layer_Height'][:]
        # time: days since 1970-01-01 00:00:00.000
        ml_time = rootgrp3.variables['time'][:]
        
        # close the file after you've had your way with the data you wanted from it
        rootgrp3.close()
#        runtime=pd.datetime.utcnow()-runstart
        df=pd.DataFrame([mlh_2[:,0],ml_time],index=['mlh2','ml_time']).T
        df['dt']=pd.to_datetime('1970-01-01 00:00:00.000') +pd.to_timedelta(df['ml_time'], unit='S')-pd.Timedelta('5 hours')
        df['dt_trunc']=df['dt'].apply(str).str[:13]
        df=df.drop_duplicates(subset=['dt_trunc','mlh2'])
        output_df=df
#        print("{}. It's working!!! It's working!!! It took {} for this file".format(i,runtime))



        output_df['Site']='HW'
        output_df['Parameter']='61301'
        output_df['Average Interval']='001h'
        output_df['Date']=output_df['dt'].dt.strftime("%m/%d/%Y %H")+':00'
        output_df['Value']=np.around(output_df['mlh2'],2)
        output_df['Raw Value']=output_df['mlh2']
        output_df['AQS Null Code']=np.where(output_df['mlh2']<0,'AN','')
        output_df['Flags']=np.where(output_df['mlh2']<0,'<-','')
        output_df['Qualifier Codes']=''
        output_df['AQS Method Code']='128'
        output_df['Data Grade']=''
        columns=['Site','Parameter','Average Interval','Date','Value','Raw Value',
                 'AQS Null Code','Flags','Qualifier Codes','AQS Method Code','Data Grade']
        output_df=output_df[columns]
        output_df=output_df.sort_values(by=['Date','Value'],ascending=False).drop_duplicates(subset=['Date'],keep='first')
        #plt.plot(mlh_2)
        output_df.to_csv(out_dir+'/'+filename.split('.')[0]+'.csv',index =False)
        
#end=pd.datetime.utcnow()          
#total=(end-start)
#print('runtime: {}'.format(total))
