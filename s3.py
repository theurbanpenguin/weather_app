# The stage 3 files finally gets the weather data
import requests

def get_public_ip():
    try:
        response = requests.get('https://ifconfig.me')
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        raise SystemExit(f"Error getting public IP address: {e}")


def get_location(ip_address):
    try:
        url = f'https://ipapi.co/{ip_address}/json/'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'latitude' in data and 'longitude' in data:
            return data['latitude'], data['longitude']
        else:
            raise ValueError("Could not retrieve location data from response")
    except requests.RequestException as e:
        raise SystemExit(f"Error getting location data: {e}")


def get_weather_forecast(latitude, longitude):
    try:
        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max&timezone=auto'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'daily' in data and 'temperature_2m_max' in data['daily']:
            return data['daily']['temperature_2m_max']
        else:
            raise ValueError("Could not retrieve weather data from response")
    except requests.RequestException as e:
        raise SystemExit(f"Error getting weather data: {e}")


public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")

latitude, longitude = get_location(public_ip)
print(f"Latitude: {latitude}, Longitude: {longitude}")

max_temperatures = get_weather_forecast(latitude, longitude)
print("Maximum temperatures for the next 7 days:")
for day, temp in enumerate(max_temperatures, start=1):
    print(f"Day {day}: {temp}°C")