import os
import pandas as pd
import matplotlib.pyplot as plt

from binance import Client
from config import Config


plt.style.use('ggplot')

apikey = Config.API_KEY
secret = Config.SECRET_KEY


client = Client(apikey, secret)

def get_price(symbol : str):
    requested_price = client.get_symbol_ticker(symbol = symbol)
    return requested_price['price']


def get_avg_price(symbol : str):
    avg_price = client.get_avg_price(symbol = symbol)
    return avg_price['price']

def historical_data(symbol : str):
    historical_data = client.get_historical_klines(symbol = symbol, interval='1h', start_str="1 day ago UTC")
    historical_df = pd.DataFrame(historical_data)
    return historical_df

def get_historical_data(symbol, interval, lookback):
    df = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback))
    df = df.iloc[:,:6]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df


cnt = 0

def plotting(data, symbol):
    global cnt
    cnt += 1
    plt.cla()
    plt.plot(data.index, data.Close)
    plt.xlabel('Time')
    plt.ylabel('Price, USDT')
    plt.title(symbol)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    file_name = 'fig_' + str(cnt) + '.jpg'
    plt.savefig(file_name, dpi=100)
    return file_name

def removing_picture(file_name : str):
    path = file_name
    os.remove(path)

def price_change_percent(symbol):
    ticker = client.get_ticker(symbol=symbol)
    price_change_percent = float(ticker['priceChangePercent'])
    price_change_percent = round(price_change_percent, 2)
    return price_change_percent


