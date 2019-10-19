from latlong import returnlatlong
from geopy.geocoders import Nominatim

def geolocator(file_name):
    geolocator = Nominatim(user_agent="NASA")
    loc = str(str(returnlatlong(file_name)[0])+", "+str(returnlatlong(file_name)[1]))

    location = geolocator.reverse(loc)
    
    return location.address
print(geolocator("sr7933"))