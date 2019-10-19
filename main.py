# from geolocator import geolocator
from latlong import returnlatlong
import ftp_functions as FTP
import parse_data

year_month = "2005-10"
array = FTP.ls(year_month)

DATA = dict()

for i in array:
    # print(i)
    latlong = returnlatlong(year_month, i)
    ozone_data, acid_data = parse_data.parse_csv(year_month, i)
    if latlong[2] in DATA:
        DATA[latlong[2]].append([i, latlong[0], latlong[1], ozone_data, acid_data])
    else:
        DATA[latlong[2]] = [[i, latlong[0], latlong[1], ozone_data, acid_data]]

print(DATA)