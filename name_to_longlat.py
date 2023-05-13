from geopy.geocoders import Nominatim
from functools import partial


def ret_lonlat(city):
    """gets city name and returns longtitude, latitude

    Args:
        city (str): ..............
    """
    geolocator = Nominatim(user_agent="location_to_longlat")

    geocode = geolocator.geocode(city)
    return geocode.longitude, geocode.latitude
    # location = partial(geolocator.geocode, language="en")

    # print(location(city))


if __name__ == "__main__":
    city = "masal"
    print(ret_lonlat(city))
