import pandas as pd
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def fetch_bitcoin_prices():
    api_key = os.getenv('API_KEY')
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key={api_key}'
    response = requests.get(url)
    data = response.json()['Data']['Data']
    return pd.DataFrame(data)

def plot_bitcoin_prices(df):
    df['time'] = pd.to_datetime(df['time'], unit='s')
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['close'], label='Bitcoin Price')
    plt.title('Bitcoin Historical Prices')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    df = fetch_bitcoin_prices()
    plot_bitcoin_prices(df)

if __name__ == "__main__":
    main()
