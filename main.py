from controller.websockets.orderbook import WebsocketBot

if __name__ == '__main__':
    bot = WebsocketBot()
    bot.watch_stream()
