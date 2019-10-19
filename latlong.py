import os
def returnlatlong(file_name):
    location_file = f"{file_name}_InfoMetadata"

    file = "./PartialDataset/"+file_name+"/"+location_file+".txt"

    meta = open(file,"r+")

    list2 = meta.readlines()
    latitude = list2[19][10:]
    longitude = list2[20][12:]


    return [list2[19],list2[20]]

print(returnlatlong(sr))
