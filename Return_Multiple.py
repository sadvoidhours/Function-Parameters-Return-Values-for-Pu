import requests

# Function to get latitude and longitude of a city
def get_coordinates(city, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200 and response.json():
        data = response.json()[0]  # Take the first result
        lat = data["lat"]
        lon = data["lon"]
        return lat, lon  # Returning multiple values
    else:
        print("Error fetching coordinates. Please check the city name.")
        return None

# Function to get weather data using latitude and longitude
def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()
        return temperature, humidity, condition
    else:
        print("Error fetching weather data.")
        return None

# --- MAIN PROGRAM ---
api_key = "a30a1fc305cd42b6ba86ea01c5cdf8c0"  # Replace with your actual OpenWeatherMap API key
city_name = input("Enter city name: ")

coords = get_coordinates(city_name, api_key)

if coords is not None:
    lat, lon = coords
    weather_data = get_weather(lat, lon, api_key)
    
    if weather_data is not None:
        temp, hum, cond = weather_data
        print(f"\nWeather Report for {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {hum}%")
        print(f"Condition: {cond}")
