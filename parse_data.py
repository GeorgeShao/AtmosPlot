def checkFileExists(file_name):
    if os.path.isfile(f'{file_name}'):
        print(f'File {file_name} exists')
        return True
    else:
        print(f'ERROR: File {file_name} does not exist')
        raise FileNotFoundError
        return False


if checkFileExists('./PartialDataset/sr7933/Data-L2_1km_grid/O3.csv'):
    with open('./PartialDataset/sr7933/Data-L2_1km_grid/O3.csv') as f:
        ozone_data = f.readlines()

if checkFileExists('./PartialDataset/sr7933/Data-L2_1km_grid/HCl.csv'):
    with open('./PartialDataset/sr7933/Data-L2_1km_grid/HCl.csv') as f:
        acid_data = f.readlines()

print(ozone_data, acid_data)

ozone_data, acid_data = list(map(float, ozone_data)), list(map(float, acid_data))

print(ozone_data, acid_data)

