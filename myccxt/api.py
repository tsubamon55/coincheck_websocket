import ccxt
from pprint import pprint

base = ccxt.coincheck()
print(base.has)

markets = base.load_markets()

# pprint(markets)

ticker = base.fetch_ticker(symbol='BTC/JPY')

# candles = base.fetch_ohlcv(symbol='BTC/JPY', timeframe='15m', since=None, limit=None, params={})
#
# pprint(candles)
