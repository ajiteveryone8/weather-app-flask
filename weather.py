import requests




def get_lat_long(city):
    # Define the API URL and parameters
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q":  city ,  # Location query
        "limit": 1,      # Limit the results to 1
        "appid": "16a8f265266ed99c216c405059ee0569"  # Your OpenWeatherMap API key
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  
        # Get the latitude and longitude
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return (latitude, longitude)
    else:
        print("Error fetching data:", response.status_code)
        return ()







def get_weather_data(city):
    
    latLongData =  get_lat_long(city)
    # Open-Meteo API endpoint
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters for the weather request
    params = {
        "latitude": latLongData[0],
        "longitude": latLongData[1],
        "current_weather": "true",  # Get current weather data
        "hourly": "temperature_2m",  # Get hourly temperature data (2 meters above ground)
        "relative_humidity_2m": "true"
    }
    
    try:
        # Send GET request to the Open-Meteo API
        response = requests.get(url, params=params)
        
        # Check if the response status code is OK (200)
        if response.status_code == 200:
            data = response.json()
            current_temp = data['current_weather']['temperature']
            windspeed = data['current_weather']['windspeed']
            winddirection = data['current_weather']['winddirection']
            hourly_temps = data['hourly']['temperature_2m']
            elevation = data['elevation']
            
            return current_temp, hourly_temps, windspeed, winddirection,elevation
        else:
            print(f"Error: Unable to fetch data (status code: {response.status_code})")
            return None, None, None, None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    
# Example usage:
latitude = 52.52  # Latitude for Berlin, Germany
longitude = 13.41  # Longitude for Berlin, Germany



current_temp, hourly_temps, windspeed, winddirection,elevation = get_weather_data('jaipur')
print(current_temp)
