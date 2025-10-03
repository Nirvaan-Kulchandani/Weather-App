import requests

API_KEY = "04ee89c10c12ffb1a995982bcb9b9445"
CITY = input("Enter the City whose weather details you want: ")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=393ad9ef2bfc3ba7254556cfa25efdb9&units=metric"

response = requests.get(URL)
weather_data = response.json()

# Extract relevant information
temperature = weather_data["main"]["temp"]
feels_like = weather_data["main"]["feels_like"]
humidity = weather_data["main"]["humidity"]
wind_speed = weather_data["wind"]["speed"]
weather_description = weather_data["weather"][0]["description"]
country = weather_data["sys"]["country"]

# Print it in a readable format
print(f"Location: {CITY}, {country}")
print(f"Temperature: {temperature}°C (Feels like {feels_like}°C)")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Weather: {weather_description.capitalize()}\n\n\n")

Do_Exit = input("Press Ok! to exit: ")