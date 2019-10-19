import os
from checkFileExists import checkFileExists

def returnlatlong(file_name):
    location_file = f"{file_name}_InfoMetadata"

    file = "./PartialDataset/"+file_name+"/"+location_file+".txt"

    if checkFileExists(file):
        meta = open(file,"r+")

    list2 = meta.readlines()
    latitude = list2[19][10:]
    longitude = list2[20][12:]
    latitude=float(latitude)
    longitude=float(longitude)
    return [latitude,longitude]

    
print(returnlatlong("sr7933"))
