import requests

API_KEY = "e6e7b37781bbcd21d786d6b3071fffd4"

city = input("Enter city name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city}&appid={API_KEY}&units=metric"
)

response = requests.get(url)

data = response.json()

if response.status_code == 200:

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather = data["weather"][0]["description"]

    print("\n-------- WEATHER REPORT --------")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather.title()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("City not found.")