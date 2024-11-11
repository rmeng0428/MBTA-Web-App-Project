import os
import json
import urllib.parse
import urllib.request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Useful base URLs
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
    return json.loads(response_text)


def get_mapbox_url(place_name: str) -> str:
    """
    Given a place name or address, return a properly encoded URL to make a Mapbox geocoding request.
    """
    query = urllib.parse.quote(place_name)
    return f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
    """
    url = get_mapbox_url(place_name)
    data = get_json(url)
    coordinates = data["features"][0]["geometry"]["coordinates"]
    longitude, latitude = coordinates[0], coordinates[1]
    return str(latitude), str(longitude)


def get_mbta_url(latitude: str, longitude: str, transportation_type: str = None) -> str:
    """
    Given latitude, longitude, and an optional transportation type, return a properly formatted URL to query the MBTA stops API.
    """
    params = {
        "api_key": MBTA_API_KEY,
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
    }
    # Filter by transportation type if specified
    if transportation_type:
        if transportation_type.lower() == "t":
            params["filter[route_type]"] = "1"  # Subway
        elif transportation_type.lower() == "bus":
            params["filter[route_type]"] = "3"  # Bus
        elif transportation_type.lower() == "commuter rail":
            params["filter[route_type]"] = "2"  # Commuter Rail

    query_string = urllib.parse.urlencode(params)
    return f"{MBTA_BASE_URL}?{query_string}"


def get_nearest_station(
    latitude: str, longitude: str, transportation_type: str = None
) -> tuple[str, bool]:
    """
    Given latitude, longitude, and an optional transportation type, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station.
    """
    url = get_mbta_url(latitude, longitude, transportation_type)
    data = get_json(url)

    # Check if any station data is available
    if not data["data"]:
        return "No nearby station found", False

    nearest_station = data["data"][0]["attributes"]["name"]
    wheelchair_accessible = data["data"][0]["attributes"]["wheelchair_boarding"] == 1
    return nearest_station, wheelchair_accessible


def get_weather(latitude: str, longitude: str) -> str:
    """
    Given latitude and longitude, return a string describing the current weather.
    """
    url = f"{OPENWEATHER_BASE_URL}?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}&units=imperial"
    data = get_json(url)
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return f"{weather_description.capitalize()}, {temperature}°F"


def find_stop_near(
    place_name: str, transportation_type: str = None
) -> tuple[str, str, str, bool]:
    """
    Given a place name or address, and an optional transportation type, return the latitude, longitude, nearest MBTA stop, whether it is wheelchair accessible, and current weather information..
    """
    latitude, longitude = get_lat_lng(place_name)
    station_name, accessible = get_nearest_station(
        latitude, longitude, transportation_type
    )
    weather = get_weather(latitude, longitude)
    return latitude, longitude, station_name, accessible, weather


def main():
    """
    Test the find_stop_near function.
    """
    place_name = input("Enter a place name or address: ")
    transportation_type = input(
        "Enter transportation type (T, Bus, Commuter Rail, or leave blank for any): "
    )
    latitude, longitude, station, accessible, weather = find_stop_near(
        place_name, transportation_type
    )
    accessibility = "Yes" if accessible else "No"
    print(f"Location: {place_name}")
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print(f"The nearest MBTA stop is {station}. Wheelchair accessible: {accessibility}")
    print(f"Current weather: {weather}")



if __name__ == "__main__":
    main()
