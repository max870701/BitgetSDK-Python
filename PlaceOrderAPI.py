from bitget.exceptions import BitgetAPIException
from dotenv import load_dotenv
import bitget.bitget_api as baseApi
import os
import logging

if __name__ == '__main__':
    # Set the log level to logging.INFO
    logging.basicConfig(level=logging.INFO)
    
    # Load the API key, secret key, and passphrase from the .env file
    load_dotenv(dotenv_path='.env')

    # Get the API key, secret key, and passphrase from the environment variables
    apiKey = os.getenv("BITGET_API_KEY")
    secretKey = os.getenv("BITGET_SECRET")
    passphrase = os.getenv("BITGET_PASSPHRASE")

    # Create an instance of the BitgetApi class
    baseApi = baseApi.BitgetApi(
                        apiKey,
                        secretKey,
                        passphrase
                        )
    
    try:
        # Set the parameters for the post request
        params = {
            "symbol": "DOGEUSDT",
            "side": "buy",
            "orderType": "limit",
            "force": "GTC",
            "price": "0.1643",
            "size": "70",
            "clientOid": "post_order_test_1"
        }

        # Place order by sending a post request
        response = baseApi.post("/api/v2/spot/trade/place-order", params)

        print(response)
        
    except BitgetAPIException as e:
        print("error:" + e.message)