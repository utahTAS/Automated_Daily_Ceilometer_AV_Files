# Automated_Daily_Ceilometer_AV_Files
EXE's to get ceilometer data from netCDF files and create text files to push to MS SQl (AV) server

## Pre-requisites
Should ony need a windows computer with a task scheduler to run

## Description
This program is a stand alone package that can be run on a station computer to get AV ready text files from netCDf files that come off of the ceilometer. The file structure and station names are hard coded into the script, so the exe's will only work on the two laptops for which the program was built. However, they should technichally work on any computer with the following directories

directory='C:/BLViewData'
out_dir='C:/Processed_netCDF'

This will definitely only work for netCDF ceilometer files, as is, but could quickly be converted for other uses.

## Built With
-I used pyinstaller to build these files. The following spec files were used for the build, and are included in the project. 

auto_pull_MLH_from_ceilometer_HW_v3.spec
auto_pull_MLH_from_ceilometer_LN_v1.spec

I used the following lines to build the exes:

pyinstaller --exclude-module PyQt5 --exclude-module dask --onefile U:\PLAN\BCUBRICH\Python\Ceilometer_Data\auto_pull_MLH_from_ceilometer_HW_v3.py

pyinstaller --exclude-module PyQt5 --exclude-module dask --onefile U:\PLAN\BCUBRICH\Python\Ceilometer_Data\auto_pull_MLH_from_ceilometer_LN_v1.py

## Use

The easiest way to use this app is to schedule it once a day with the windows task scheduler. 

# Python libraries
To run this script in a python IDE rather than as an exe you will need the following
-numpy
-pandas
-netCDF4
-os
