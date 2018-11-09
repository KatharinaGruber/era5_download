# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:12:50 2018

@author: KatharinaG
"""
# script for downloading era5 single levels data with cds api
# get account at: https://cds.climate.copernicus.eu/user/register?destination=%2F%23!%2Fhome
# check license agreement
# install csdapi and key: https://cds.climate.copernicus.eu/api-how-to
# (to create .cdsapirc file create text file and rename to .cdsapirc.)
# if using conda, make sure to install it via conda prompt
# see data you can download: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

# data are availabe from 2000 until now
# for variables available see link above


import cdsapi
import numpy as np
import calendar
import os

# define directory in which data shall be stored
os.chdir("C:/Users/KatharinaG/Documents/DOK/era5/data_aut")

c = cdsapi.Client()


# define variable to download (eg. u component 100m wind)
var = '100m_u_component_of_wind'
# define the years you want to download
yearstart = 2000
yearend = 2017
# define the start and end month you want to download
monthstart = 1
monthend = 12
# define the start and end day you want to download
daystart = 1
dayend = 31
# define spatial limits of download (eg. around Austria)
lon1 = 8
lon2 = 18
lat1 = 45.5
lat2 = 50

# create lists
years = np.array(range(yearstart,yearend+1),dtype="str")
lonlat = [lat2, lon1, lat1, lon2]
                



for year in years:
    if (int(year)==yearstart) and (int(year)==yearend):
        months = np.array(range(monthstart,monthend+1),dtype="str")
    elif (year == yearstart) :
        months = np.array(range(monthstart,13),dtype="str")
    elif (year == yearend):
        months = np.array(range(1,monthend + 1),dtype="str")
    else:
        months = np.array(range(1,13),dtype="str")
               
    for month in months:
        
        if int(month) < 10:
            m = '0' + month
        else:
            m = month
        
        if(int(year) == yearstart) and (int(year) == yearend) and (int(month) == monthstart) and (int(month) == monthend):
                days = list(np.array(range(daystart,dayend+1),dtype="str"))
        elif (int(year) == yearstart) and (int(month) == monthstart):
            days = list(np.array(range(daystart,calendar.monthrange(int(year),int(month))[1]+1),dtype="str"))
        elif (int(year) == yearend) and (int(month) == monthend):
            days = list(np.array(range(1,dayend+1),dtype="str"))
        else:
            days = list(np.array(range(1,calendar.monthrange(int(year),int(month))[1]+1),dtype="str"))
        
        for day in days:
            if int(day) < 10:
                d = '0' + day
            else:
                d = day
                
            c.retrieve(
                    'reanalysis-era5-single-levels',
                    {
                            'variable': var,
                            'product_type':'reanalysis',
                            'year': year,
                            'month': month,
                            'day': day,
                            'time':[
                                    '00:00','01:00','02:00',
                                    '03:00','04:00','05:00',
                                    '06:00','07:00','08:00',
                                    '09:00','10:00','11:00',
                                    '12:00','13:00','14:00',
                                    '15:00','16:00','17:00',
                                    '18:00','19:00','20:00',
                                    '21:00','22:00','23:00'
                                    ],
                            'area': lonlat,
                            'format':'netcdf',
                            #'grid': '0.3/0.3'
                        },
                        'era5_' + var + '_' + year + m + d + '.nc')