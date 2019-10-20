import ftp_functions as ftp

def parse_csv(year_month, file_name, gas_name_1, gas_name_2):
    ozone_data = ftp.cat(f'{year_month}/{file_name}/Data-L2_1km_grid/{gas_name_1}.csv').split('\n')
    acid_data = ftp.cat(f'{year_month}/{file_name}/Data-L2_1km_grid/{gas_name_2}.csv').split('\n')
    ozone_data, acid_data = list(map(float, ozone_data)), list(map(float, acid_data))
    ozone_data, acid_data = [None if x == -999.0 else x*1000000 for x in ozone_data], [None if x == -999.0 else x*1000000 for x in acid_data]
    return ozone_data, acid_data
