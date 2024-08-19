#!/usr/bin/python
from bitget.ws.bitget_ws_client import BitgetWsClient, SubscribeReq
from bitget import consts as c
import logging


def handle(message):
    logger.info("handle:" + message)


def handel_error(message):
    logger.error("handle_error:" + message)


if __name__ == '__main__':
    # Define the log format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Set the log level to logging.INFO, log format, and handlers
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler('status.log'),
            logging.StreamHandler()
        ]
    )

    # Get the logger
    logger = logging.getLogger()

    # The symbol for subscription
    symbol = 'BTCUSDT'

    # Create the client with the private WebSocket URL, API key, secret key, and passphrase
    client = BitgetWsClient(c.PUBLIC_WS_URL, need_login=False) \
        .error_listener(handel_error) \
        .build()
    
    logger.info("Created a Bitget client")

    # Subscribe to the order channel
    channels = [SubscribeReq("SPOT", "candle1m", symbol)]
    client.subscribe(channels, handle)
    logger.info("Subscribed to the ticker channel")