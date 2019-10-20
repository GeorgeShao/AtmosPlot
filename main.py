# from geolocator import geolocator
from latlong import returnlatlong
import ftp_functions as FTP
import parse_data

year_month = "2007-10"
array = FTP.ls(year_month)

DATA = list()

for i in array:
    # print(i)
    latlong = returnlatlong(year_month, i)
    ozone_data, acid_data = parse_data.parse_csv(year_month, i)
    DATA.append(ozone_data)
    DATA.append(acid_data)
    DATA.append(latlong)

print(DATA)