### Python Version Suggestion

`python version：3.6+`

#### Step 1: Download the repository and install the required libraries

1.1 Clone this repository
```bash
git clone git@github.com:432HzQuant/Liquidity_Provider.git
```
1.2 Pull the `feature/bitget-sdk` branch into your local repository
```bash
git checkout -b feature/bitget-sdk origin/feature/bitget-sdk
```
1.3 Install the required libraries
```bash
pip install -r requirements.txt
```

#### Step 2：Configure Bitget Account

2.1 [Apply an API Key](https://www.bitget.com/zh-CN/account/newapi)

2.2 Fill out the API Key, Secret Key, Passphrase in the `.env` file
```text
BITGET_API_KEY=API_KEY
BITGET_SECRET=SECRET_KEY
BITGET_PASSPHRASE=PASSPHRASE
```

#### Step 3: Invoke Interfaces

* RestAPI

    * Run `PlaceOrderAPI.py`

    * In this example, the `PlaceOrderAPI.py` file is used to place an order. You can modify the parameters in the file to place different orders.

* WebSocket

    * Run `OrderChannelWS.py`

    * In this example, the `OrderChannelWS.py` file is used to subscribe to the `orders` channel with `DOGEUSDT` `SPOT` pair. You can modify the parameters in the file to subscribe to different channels.

Note：

* [Official API Document](https://bitgetlimited.github.io/apidoc/zh/spot/)

* Encountered `WebSocketAPI` Problems?

    * `asyncio`:

            https://docs.python.org/3/library/asyncio-dev.html

    * `websockets`:

            https://websockets.readthedocs.io/en/stable/intro.html
            https://github.com/aaugustin/websockets

    * About `code=1006`:

            https://github.com/Rapptz/discord.py/issues/1996
            https://github.com/aaugustin/websockets/issues/587