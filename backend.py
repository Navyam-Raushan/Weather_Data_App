import requests

API_KEY = "fc90e49ba4571fe9e453137533d5b75f"


def get_data(place, forecast_day=None, weather_key=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_value = 8 * forecast_day
    filtered_data = filtered_data[:nr_value]

    return filtered_data
# Further filtering will be done in main file so that we need one if-else.


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_day=3,
                   weather_key="Sky"))
