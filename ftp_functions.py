from ftplib import FTP
import os


ftp = FTP('ftp.asc-csa.gc.ca')
ftp.login()

def access(path_to_file: str):
    path_to_file = os.path.normpath(path).split(os.sep)
    return_string = str()
    BASE = "users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV/"
    ftp.retrlines(f'RETR {base}{path_to_file}', lambda x: return_string.append(x))
    return return_string