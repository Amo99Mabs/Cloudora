import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric"
)


response = requests.get(url)

data = response.json()

if response.status_code == 200:

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather = data["weather"][0]["description"]

    # Weather emoji
    if "cloud" in weather.lower():
       emoji = "☁️"
    elif "rain" in weather.lower():
       emoji = "🌧️"
    elif "clear" in weather.lower():
       emoji = "☀️"
    elif "thunder" in weather.lower():
       emoji = "⛈️"
    else:
       emoji = "🌍"


    print("\n-------- WEATHER REPORT --------")
    print(f"City: {city_name}")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"🌤️ Weather: {weather} {emoji}")
else: 
    print("❌ City not found.")