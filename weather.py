import requests

def get_weather(city):
    api_key = "4ef987b54c2b433e7600cc90e49d8873"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters to send with the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For Celsius temperature
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        print(f"Error: {data.get('message')}")
        return

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
