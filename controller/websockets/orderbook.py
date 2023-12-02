import json
from websocket import create_connection

import settings


class WebsocketBot(object):
    def __init__(self):
        self.ws = create_connection(settings.websocket_url)

    def watch_stream(self):
        self.ws.send(json.dumps({
           "type": "subscribe",
           "channel": "btc_jpy-trades"
        }))
        while True:
            print(self.ws.recv())




