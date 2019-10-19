import os
from checkFileExists import checkFileExists

file = './PartialDataset/sr7933/Data-L2_1km_grid/O3.csv'
if checkFileExists(file):
    with open(file) as f:
        ozone_data = f.readlines()

file = './PartialDataset/sr7933/Data-L2_1km_grid/HCl.csv'
if checkFileExists(file):
    with open(file) as f:
        acid_data = f.readlines()

print(ozone_data, acid_data)

ozone_data, acid_data = list(map(float, ozone_data)), list(map(float, acid_data))

ozone_data, acid_data = [None if x == -999.0 else x for x in ozone_data], [None if x == -999.0 else x for x in acid_data]

print(ozone_data, acid_data)
