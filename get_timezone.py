import time
import requests


def get_timezone(latitude, longitude, api_key, timestamp):
    """returns time zone id

    Args:
        latitude (int): .......
        longitude (int): .......
        api_key (str): .......
        timestamp (float): .......

    """
    url = "https://maps.googleapis.com/maps/api/timezone/json"

    params = {
        "location": f"{longitude},{latitude}",
        "timestamp": timestamp,
        "key": api_key,
    }

    response = requests.get(url, params=params)
    return response.text


if __name__ == "__main__":
    from name_to_longlat import ret_lonlat

    api_key = "AIzaSyByMHhtuWyecqJhUc4R0r57V5EWGism9rU"
    timestamp = time.time()
    # print(timestamp)
    longitude, latitude = ret_lonlat("masal")

    print(get_timezone(longitude, latitude, api_key, timestamp))
