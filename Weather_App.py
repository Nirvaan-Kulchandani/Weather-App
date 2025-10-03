# 1️⃣5️⃣ Weather Dashboard	   requests, tkinter	  API + GUI combined

import requests
from tkinter import *
from tkinter import messagebox


def get_weather():
    '''Fetches weather data for a given city using OopenWeatherMap API.'''

    city = city_entry.get().lower()
    # API_Key = api_entry.get().lower()
    API_Key = "c2a1cf593242c41873cbc5f4b3aba9c6"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
    response = requests.get(url)

    data =response.json()
    print(data)

    try:

        if response.status_code == 200:
            city_name = data['name']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            weather = data['weather'][0]['description']

            result_text.config(text=f"City: {city_name}\nTemperature: {temperature}°C\nIt feels like: {feels_like}°C\nHumidity: {humidity}%\nWeather: {weather}\n Wind Speed: {wind_speed} m/s\n")
    
    except Exception as E:
        
        result_text.config(text=f"{E}")


root= Tk()

root.title("Nirvaan Weather APP")
root.geometry("450x500")
root.config(bg="grey96")

city_label = Label(root, text="Enter City Name:", bg="purple", fg="limegreen", font=("Algerian", 12))
city_label.grid(row=0, column=0, padx=5, pady=10)

city_entry = Entry(root, width=30, font=("Comic Sans MS", 10))
city_entry.grid(row=0,column=1, padx=10, pady=10)

# api_label = Label(root, text="Enter API Key:", bg="purple", fg="yellow", font=("Comic Sans MS", 12))
# api_label.grid(row=1,column=0, padx=5, pady=10)

# api_entry = Entry(root, width=30, font=("Comic Sans MS", 10))
# api_entry.grid(row=1,column=1, padx=10, pady=10)

Submit_btn = Button(root, text="Submit Info", command=get_weather)
Submit_btn.grid(row=2, column=1, padx=10, pady=10)

result_text = Label(root, bg="black", fg="yellow", font=("Comic Sans MS", 15))
result_text.grid(row = 3, column=1, padx=20, pady=20)

if __name__ == "__main__":
    root.mainloop()