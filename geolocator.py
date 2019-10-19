from latlong import returnlatlong
from geopy.geocoders import Nominatim

def geolocator(year_month, file_name):
    geolocator = Nominatim(user_agent="NASA")
    vare = returnlatlong(year_month, file_name)
    loc = str(str(vare[0])+", "+str(vare[1]))

    location = geolocator.reverse(loc)
    
    return location.address

# print(geolocator("2005-02", "sr7933"))