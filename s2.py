# Extend S1 by getting location
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


public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")

latitude, longitude = get_location(public_ip)
print(f"Latitude: {latitude}, Longitude: {longitude}")