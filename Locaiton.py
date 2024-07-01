
import cgi
from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Kumbha Marg")
print(getLoc.address)
print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)