import json
from websocket import create_connection

import settings
from model.websocket.orderbook import Transaction, session
import logging
import json

logger = logging.getLogger(__name__)


class WebsocketBot(object):
    def __init__(self):
        self.ws = create_connection(settings.websocket_url)

    def watch_stream(self):
        self.ws.send(json.dumps({
           "type": "subscribe",
           "channel": "btc_jpy-trades"
        }))
        logger.info('connected')
        while True:
            tx = json.loads(self.ws.recv())
            for t in tx:
                logger.info(t)
                column = Transaction(
                    timestamp=t[0],
                    txid=t[1],
                    trade_pair=t[2],
                    rate=t[3],
                    amount=t[4],
                    buy_or_sell=t[5],
                    taker_txid=t[6],
                    maker_txid=t[7],
                )
                session.add(column)
            session.commit()




