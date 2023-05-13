import requests
from pathlib import Path
import os
import time

from name_to_longlat import ret_lonlat
from get_timezone import get_timezone

city = input("Enter the location name >>> ")
longitude, latitude = ret_lonlat(city)

# this part still have some issues
timestamp = time.time()
api_key = "<Enter your api key>"
time_zone_id = get_timezone(
    longitude=longitude, latitude=latitude, timestamp=timestamp, api_key=api_key
)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True,
    "hourly": "temperature_2m",
}
r = requests.get(url, params=params)
print(r.url)
# print(r.text)

path = Path("D:\Programming and cyber security\weathering_app")
with open(path / "data.json", "w") as file:
    file.write(r.text)

input("press Enter/return to finish !!")
os.system("cls")
