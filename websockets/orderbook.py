import json
from websocket import create_connection

ws = create_connection("wss://ws-api.coincheck.com/")

ws.send(json.dumps({
   "type": "subscribe",
   "channel": "btc_jpy-trades"
}))

while True:
    print(ws.recv())

