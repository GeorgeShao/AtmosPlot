import os
from checkFileExists import checkFileExists
import ftp_functions as ftp

def returnlatlong(year_month, file_name):

    file = f"{year_month}/{file_name}/{file_name}_InfoMetadata.txt"

    

    list2 = meta.readlines()
    latitude = list2[19][10:]
    longitude = list2[20][12:]
    latitude=float(latitude)
    longitude=float(longitude)
    return [latitude,longitude]

    