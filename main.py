import requests
import os
from dotenv import load_dotenv

load_dotenv()

def weather():

    api = os.getenv('Weather_API')
    city = input("Enter the City Name : ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        print(f"{city} Weather")
        temp = f"{(data['main']['temp']):.1f}"
        hum = data['main']['humidity']
        curr = data['weather'][0]['main']
        print(f"Temperature : {temp}'C \n"
              f"Humidity : {hum}% \n"
              f"Overall : {curr}")
    else :
        print("Invalid City")

if __name__ == "__main__":

        weather()

