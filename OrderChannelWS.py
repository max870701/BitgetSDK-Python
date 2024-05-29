#!/usr/bin/python
from bitget.ws.bitget_ws_client import BitgetWsClient, SubscribeReq
from bitget import consts as c
from dotenv import load_dotenv
import os
import logging
import time


def handle(message):
    with open('./connection-status.txt', 'a') as file:
        # insert the time of the message
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"{time_now} Connection status: {message}\n")
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

    # Load the API key, secret key, and passphrase from the .env file
    load_dotenv(dotenv_path='.env')

    logger.info("Loaded the env file")

    # Get the API key, secret key, and passphrase from the environment variables
    api_key = os.getenv("BITGET_API_KEY")
    secret_key = os.getenv("BITGET_SECRET")
    passphrase = os.getenv("BITGET_PASSPHRASE")

    logging.info("Loaded the environment variables")

    # The symbol for subscription
    symbol = 'DOGEUSDT'

    # Create the client with the private WebSocket URL, API key, secret key, and passphrase
    client = BitgetWsClient(c.PRIVATE_WS_URL, need_login=True) \
        .api_key(api_key) \
        .api_secret_key(secret_key) \
        .passphrase(passphrase) \
        .error_listener(handel_error) \
        .build()
    
    logger.info("Created a Bitget client")

    # Subscribe to the order channel
    channels = [SubscribeReq("SPOT", "orders", symbol)]
    client.subscribe(channels, handle)
    logger.info("Subscribed to the orders channel")