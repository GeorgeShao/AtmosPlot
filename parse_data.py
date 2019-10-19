import ftp_functions as ftp

def parse_csv(year_month, file_name):
    ozone_data = ftp.cat(f'{year_month}/{file_name}/Data-L2_1km_grid/O3.csv').split('\n')
    acid_data = ftp.cat(f'{year_month}/{file_name}/Data-L2_1km_grid/HCl.csv').split('\n')
    print(ozone_data)
    print(acid_data)
    ozone_data, acid_data = list(map(float, ozone_data)), list(map(float, acid_data))
    ozone_data, acid_data = [None if x == -999.0 else x for x in ozone_data], [None if x == -999.0 else x for x in acid_data]
    return ozone_data, acid_data

