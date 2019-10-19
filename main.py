import os
from geolocator import geolocator
from latlong import returnlatlong
import ftp_functions as FTP
import parse_data

year_month = "2005-10"
array = FTP.ls(year_month)

gas = dict()

for i in array:
    print('Iteration')
    latlong = returnlatlong(year_month, i)
    ozone_data, acid_data = parse_data.parse_csv(year_month, i)
    gas[i] = [latlong[0], latlong[1], ozone_data, acid_data]

print(gas)