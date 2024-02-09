import asyncio
import json
import websockets


URL = 'wss://www.deribit.com/ws/api/v2'


def get_coin_cost(coin: str) -> float:
    """
        returns a cost of a given coin from Deribit

    
    """

    # TODO make a function to get data from a Deribit API

    return get_current_mid_price(coin)

    # if coin == 'BTC':
    #     return 42600.0
    # elif coin == 'ETH':
    #     return 2605.2

    
    

def make_public_message(asset: str) -> dict:
    order_book_msg = {
        "jsonrpc": "2.0",
        "id": 42,
        "method": "public/get_order_book",
        "params": {
            "instrument_name": f"{asset}-PERPETUAL",
            "depth": 30
        }
    }

    return order_book_msg


async def pub_api(msg):
        async with websockets.connect(URL) as websocket:
            await websocket.send(msg)
            while websocket.open:
                response = await websocket.recv()
                return json.loads(response)
            

def get_current_mid_price(asset: str):
    message = make_public_message(asset)
    book = asyncio.get_event_loop().run_until_complete(pub_api(json.dumps(message)))
    asks = book['result']['asks'][0][0]
    bids = book['result']['bids'][0][0]
    return (asks + bids) / 2

def get_order_book(message: dict):
    book = asyncio.get_event_loop().run_until_complete(pub_api(json.dumps(message)))
    asks = book['result']['asks']
    bids = book['result']['bids']
    return asks, bids