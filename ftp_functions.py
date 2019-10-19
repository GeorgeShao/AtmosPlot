from ftplib import FTP
import os

BASE = "/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format CSV/"
ftp = FTP('ftp.asc-csa.gc.ca')
ftp.login()

def cat(path_to_file: str):
    return_string = str()
    def add_to_return_string(line):
        nonlocal return_string
        return_string += line + '\n'
    ftp.retrlines(f'RETR {BASE}{path_to_file}', add_to_return_string)
    return_string = return_string[:-1]
    return return_string

def ls(directory: str):
    ftp.cwd(f"{BASE}{directory}/")
    return ftp.nlst()

def quit():
    ftp.quit()
