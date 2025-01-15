import requests
import json

def fetch_ginger_data():
    with open('configs/api_config.json') as f:
        config = json.load(f)
    
    response = requests.get(config['ginger_api_url'], headers={'Authorization': f"Bearer {config['api_key']}"})
    with open('data/ginger_data.json', 'w') as f:
        json.dump(response.json(), f)
    print("Ginger data fetched.")

def fetch_maize_data():
    with open('configs/api_config.json') as f:
        config = json.load(f)
    
    response = requests.get(config['maize_api_url'], headers={'Authorization': f"Bearer {config['api_key']}"})
    with open('data/maize_data.json', 'w') as f:
        json.dump(response.json(), f)
    print("Maize data fetched.")

def fetch_rice_data():
    with open('configs/api_config.json') as f:
        config = json.load(f)
    
    response = requests.get(config['rice_api_url'], headers={'Authorization': f"Bearer {config['api_key']}"})
    with open('data/rice_data.json', 'w') as f:
        json.dump(response.json(), f)
    print("Rice data fetched.")

def fetch_cocoa_data():
    with open('configs/api_config.json') as f:
        config = json.load(f)
    
    response = requests.get(config['cocoa_api_url'], headers={'Authorization': f"Bearer {config['api_key']}"})
    with open('data/cocoa_data.json', 'w') as f:
        json.dump(response.json(), f)
    print("Cocoa data fetched.")
