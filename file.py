import requests
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    def get_data(self, city):
        params = {'q': city, 'appid': self.api_key}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['list']
        else:
            print(f"Error: {response.status_code}")
            return None

def temperature(weather_data, target_time):
    for entry in weather_data:
        if entry['dt_txt'] == target_time:
            return entry['main']['temp']
    return None

def wind_speed(weather_data, target_time):
    for entry in weather_data:
        if entry['dt_txt'] == target_time:
            return entry['wind']['speed']
    return None

def pressure(weather_data, target_time):
    for entry in weather_data:
        if entry['dt_txt'] == target_time:
            return entry['main']['pressure']
    return None

def main():
    api_key = "REST GET API"
    city = "London"
    weather_api = WeatherAPI(api_key)
    weather_data = weather_api.get_data(city)

    if weather_data is None:
        print("Unable to fetch weather data. Exiting.")
        return

    while True:
        print("\n1. Temperature\n2. Wind Speed\n3. Pressure\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting program.")
            break
        elif choice in ['1', '2', '3']:
            target_time = input("Enter the date with time (yyyy-mm-dd hh:mm:ss): ")
            if choice == '1':
                result = temperature(weather_data, target_time)
                parameter = 'Temperature'
            elif choice == '2':
                result = wind_speed(weather_data, target_time)
                parameter = 'Wind Speed'
            elif choice == '3':
                result = pressure(weather_data, target_time)
                parameter = 'Pressure'

            if result is not None:
                print(f"{parameter} at {target_time}: {result}")
            else:
                print(f"No data available for {parameter} at {target_time}")
        else:
            print("Invalid choice. Please enter a valid option.")
main()
