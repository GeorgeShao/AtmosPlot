from ftplib import FTP
import os


ftp = FTP('ftp.asc-csa.gc.ca')
ftp.login()

def access(path_to_file: str):
    return_string = str()
    BASE = "users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV/"
    def add_to_return_string(line):
        nonlocal return_string
        return_string += line + '\n'
    ftp.retrlines(f'RETR {BASE}{path_to_file}', add_to_return_string)
    return_string = return_string[:-1]
    return return_string