import requests

API_KEY = "fc90e49ba4571fe9e453137533d5b75f"


def get_data(place, forecast_day=None, weather_key=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    dates = []
    temperature = []
    for i in range(int(forecast_day)):
        dates.append(data["list"][i]["dt_txt"])
        temperature.append(data["list"][i]["main"]["temp"])

    return dates,temperature


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_day=3))
