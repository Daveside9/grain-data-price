import pandas as pd
import json

def process_ginger_data():
    with open('data/ginger_data.json') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df = df.dropna()  # Example cleaning step: drop rows with missing values
    df.to_csv('data/processed_ginger_data.csv', index=False)
    print("Ginger data processed.")

def process_maize_data():
    with open('data/maize_data.json') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df = df.dropna()
    df.to_csv('data/processed_maize_data.csv', index=False)
    print("Maize data processed.")

def process_rice_data():
    with open('data/rice_data.json') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df = df.dropna()
    df.to_csv('data/processed_rice_data.csv', index=False)
    print("Rice data processed.")

def process_cocoa_data():
    with open('data/cocoa_data.json') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df = df.dropna()
    df.to_csv('data/processed_cocoa_data.csv', index=False)
    print("Cocoa data processed.")
