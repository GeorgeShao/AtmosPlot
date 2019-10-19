import os
from geolocator import geolocator
from checkFileExists import checkFileExists
from latlong import returnlatlong
import ftp_functions as FTP

year = "2005-10"
array = FTP.ls(year)

gas = dict()

for i in array:
    