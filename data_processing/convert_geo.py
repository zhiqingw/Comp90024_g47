# Author:      Zhiqing Wu
# Student id:  931919
# Description: convert coordinate to suburb

from geopy import Nominatim

def geo_convertor(coordinate):
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.reverse(coordinate)
    print(location.raw)
    address = location.raw['address']['suburb']
    # address = location.address.split(',')
    return(address)