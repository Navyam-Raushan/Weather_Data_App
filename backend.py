import requests

API_KEY = "fc90e49ba4571fe9e453137533d5b75f"


def get_data(place, forecast_day=None, weather_key=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_value = 8 * forecast_day
    filtered_data = filtered_data[:nr_value]

    if weather_key == "Temperature":
        # t represents each temperature item in all nr_value list.
        filtered_data = [t["main"]["temp"] for t in filtered_data]
    else:
        # Same here to get each item observe the data structure carefully.
        filtered_data = [s["weather"][0]["main"] for s in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_day=3,
                   weather_key="Sky"))
