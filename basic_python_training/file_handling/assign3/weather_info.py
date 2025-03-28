import json
file_path="/Users/consultadd/Desktop/python_training/file_handling/assign3/weather.json"

def read_weather_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)  # Load JSON data

    for city in data["list"]:
        name = city["name"]
        temperature = city["main"]["temp"]
        pressure = city["main"]["pressure"]
        wind_speed = city["wind"]["speed"]
        weather_desc = city["weather"][0]["description"]

        print(f"Location: {name}")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {weather_desc}")
        print("-" * 40)

read_weather_data(file_path)
