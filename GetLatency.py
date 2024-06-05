import os
import time
import logging
import bitget.bitget_api as baseApi
from dotenv import load_dotenv
from bitget.exceptions import BitgetAPIException

# Set the log level to logging.INFO
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("latency.log")])

logger = logging.getLogger()

# Time latency decorator
def latency_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Time latency: {end - start} seconds")
        return result
    return wrapper

class TestLatency(baseApi.BitgetApi):
    def __init__(self, apiKey, secretKey, passphrase):
        super().__init__(apiKey, secretKey, passphrase)
    
    @latency_decorator
    def place_order(self, symbol, side, orderType, force, price, size):
        params = {
            "symbol": symbol,
            "side": side,
            "orderType": orderType,
            "force": force,
            "price": price,
            "size": size
        }

        response = self.post("/api/v2/spot/trade/place-order", params)
        return response
    
    @latency_decorator
    def cancel_order(self, symbol, orderId):
        params = {
            "symbol": symbol,
            "orderId": orderId
        }

        response = self.post("/api/v2/spot/trade/cancel-order", params)
        return response

if __name__ == '__main__':
    # Load the API key, secret key, and passphrase from the .env file
    load_dotenv(dotenv_path='.env')

    # Get the API key, secret key, and passphrase from the environment variables
    apiKey = os.getenv("BITGET_API_KEY")
    secretKey = os.getenv("BITGET_SECRET")
    passphrase = os.getenv("BITGET_PASSPHRASE")

    test_latency_instance = TestLatency(apiKey, secretKey, passphrase)

    def call_api_with_latency(test_latency_instance, symbol, side, orderType, force, price, size, sleep_time):
        try:
            response = test_latency_instance.place_order(
                symbol=symbol,
                side=side,
                orderType=orderType,
                force=force,
                price=price,
                size=size
            )
            orderId = response["data"]["orderId"]
        except BitgetAPIException as e:
            logger.warning("Place order error:" + e.message)
        
        logger.info(f"Sleep {sleep_time} seconds")
        time.sleep(sleep_time)

        try:
            response = test_latency_instance.cancel_order(
                symbol=symbol,
                orderId=orderId
            )
            logger.info(response.get("msg"))
        except BitgetAPIException as e:
            logger.warning("Cancel order error:" + e.message)

    run_times = 10

    for i in range(run_times):
        logger.info(f"---- Run {i+1} times ----")
        call_api_with_latency(
            test_latency_instance=test_latency_instance,
            symbol="DOGEUSDT",
            side="buy", 
            orderType="limit",
            force="GTC",
            price="0.15",
            size="100",
            sleep_time=1)
