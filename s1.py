# Get you Public IP
import requests

def get_public_ip():
    try:
        response = requests.get('https://ifconfig.me')
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        raise SystemExit(f"Error getting public IP address: {e}")

public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")