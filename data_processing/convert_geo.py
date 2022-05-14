from geopy import Nominatim

def geo_convertor(coordinate):
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.reverse(coordinate)
    address = location.address.split(',')
    return(address[-6])