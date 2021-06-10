import requests
from datetime import datetime
import pandas as pd
import os

from stockstats import StockDataFrame

from math import pi

# Lo saqué de aca https://towardsdatascience.com/cryptocurrency-analysis-with-python-macd-452ceb251d7c

from_symbol = 'ETH'
to_symbol = 'USDT'
exchange = 'Binance'
datetime_interval = 'hour'


def get_filename(from_symbol, to_symbol, exchange, datetime_interval, download_date):
    return f'{from_symbol}_{to_symbol}_{exchange}_{datetime_interval}_{download_date}.csv'


def download_data(from_symbol, to_symbol, exchange, datetime_interval):
    supported_intervals = {'minute', 'hour', 'day'}
    assert datetime_interval in supported_intervals, f'datetime_interval should be one of {supported_intervals}'
    print(f'Downloading {datetime_interval} trading data for {from_symbol} {to_symbol} from {exchange}')
    base_url = 'https://min-api.cryptocompare.com/data/histo'
    url = '%s%s' % (base_url, datetime_interval)
    params = {'fsym': from_symbol, 'tsym': to_symbol,
              'limit': 100, 'aggregate': 1,
              'e': exchange}
    request = requests.get(url, params=params)
    data = request.json()
    return data


def convert_to_dataframe(data):
    df = pd.json_normalize(data, ['Data'])
    df['datetime'] = pd.to_datetime(df.time, unit='s')
    df = df[['datetime', 'low', 'high', 'open',
             'close', 'volumefrom', 'volumeto']]
    return df


def filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    print('Filtering %d empty datapoints' % indices.shape[0])
    df = df.drop(indices)
    return df

# Trading strategy
def read_dataset(filename):
    print('Reading data from %s' % filename)
    df = pd.read_csv(filename)
    # change type from object to datetime
    df.datetime = pd.to_datetime(df.datetime)
    df = df.set_index('datetime')
    df = df.sort_index() # sort by datetime
    print(df.shape)
    return df


def signal():
    data = download_data(from_symbol, to_symbol, exchange, datetime_interval)
    df = convert_to_dataframe(data)
    df = filter_empty_datapoints(df)
    current_datetime = datetime.now().date().isoformat()
    filename = get_filename(from_symbol, to_symbol, exchange, datetime_interval, current_datetime)
    print('Saving data to %s' % filename)
    df.to_csv(filename, index=False)

    df = read_dataset(filename)

    # Calculate the trading strategy
    df = StockDataFrame.retype(df)
    df['macd'] = df.get('macd')  # calculate MACD

    # Obtengo las ultimas dos rows
    rows = df.tail(2)
    before = rows.iloc[0]
    after = rows.iloc[1]

    result = ""
    # Si son de distinto signo
    if after['macdh'] * before['macdh'] <= 0:
        # Si el úlimo macd es pasitivo es compra, si no venta
        if after['macdh'] > 0:
            result += "**Comprar ETH** 📈"
            result += f"\n**Entrada:** `{round(after['open'])}`"
            result += f"\n**Take Profit:** `{round(after['open'] * (1 + 0.015))}`"
        else:
            result += "**Vender ETH** 📉"
            result += f"\n**Entrada:** `{round(after['open'])}`"
            result += f"\n**Take Profit:** `{round(after['open'] * (1 - 0.015))}`"

    print(result)
    os.remove(filename)
    return result





