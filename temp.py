import time

######## ftp_functions.py

from ftplib import FTP
import os

BASE = "users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV/"
ftp = FTP('ftp.asc-csa.gc.ca')
ftp.login()

def cat(path_to_file: str):
    return_string = str()
    def add_to_return_string(line):
        nonlocal return_string
        return_string += line + '\n'
    print(f"RUNNING COMMAND ON FTP: 'RETR {BASE}{path_to_file}'")
    ftp.retrlines(f'RETR {BASE}{path_to_file}', add_to_return_string)
    return_string = return_string[:-1]
    return return_string

def ls(directory: str):
    ftp.cwd(f"{BASE}{directory}/")
    return ftp.nlst()


####### latlong.py

def returnlatlong(year_month, file_name):

    file = f"{year_month}/{file_name}/{file_name}_InfoMetadata .txt"  # XXX: space before .txt
    print(file)
    meta = cat(file)

    list2 = meta.split('\n')
    latitude = list2[19][10:]
    longitude = list2[20][12:]
    latitude=float(latitude)
    longitude=float(longitude)
    return [latitude,longitude]




array = ls("2005-10")
time.sleep(5)
print()