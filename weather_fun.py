import requests 
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local") 


def getWeather(api_key, user_city):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&APPID={api_key}")
    if weather_data.status_code == 200:
        wdata = weather_data.json()
        temp = wdata['main']['temp']
        desc = wdata['weather'][0]['description']
        print(f"The current temperature in {user_city} is {temp} with {desc}.")
        return temp
    else:
        print("Could not retrieve weather data. Check your city spelling, or make sure you added your API key in .env.local or followed instructions on line 39. ")
        return None

def setClothing(temp):
    if temp is None:
        return
    if temp <= 50:
        print('It is very cold out, remember to bundle up adn remain hydrated.')
    elif temp <= 59:
        print('It is cold out, consider bundling up! ')
    elif 60 <= temp <= 79:
        print('It is cool out, perfect for casual clothing.')
    elif 80 < temp <=90:
        print('It is warm out, consider cool clothing, and keep hydrating!')
    else:
        print('It is VERY hot outside, wear very cool clothing if you go outside and remember to hydrate!!')
    



if __name__ == "__main__":
    #api_key = "[Enter Your api_key here]"
    api_key = os.getenv("api_key")
    if not api_key:
        print("API key not found. Either check your .env.local file or just simply uncomment out line 39 and comment lines 40, 41, and 42 and " \
        "enter in your own API key from this link. https://openweathermap.org/api")
    user_city = input('Enter in your city: ')
    temp = getWeather(api_key, user_city)
    setClothing(temp)
