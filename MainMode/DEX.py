from DeckoApi import GeckoTerminalAPI

gt = GeckoTerminalAPI()


def get_price(assetX: str, assetY: str, api_response: dict) -> dict:
    """
    Adapted function to work with the API response directly, with error handling for missing 'symbol' key.

    Args:
        assetX (str): Symbol of the first asset.
        assetY (str): Symbol of the second asset.
        api_response (dict): The API response containing pool data.

    Returns:
        dict: A dictionary with the pool's depth, and the current prices of asset X and Y in the pool.
    """
    attributes = api_response['data']['attributes']

    symbol_to_price = {}

    for token in api_response.get('included', []):
        token_attr = token.get('attributes', {})
        symbol = token_attr.get('symbol')
        if symbol:
            # Determine if the token is the base or quote token by matching its ID
            if token['id'] == api_response['data']['relationships']['base_token']['data']['id']:
                symbol_to_price[symbol] = float(attributes['base_token_price_usd'])
            elif token['id'] == api_response['data']['relationships']['quote_token']['data']['id']:
                symbol_to_price[symbol] = float(attributes['quote_token_price_usd'])

    depth = symbol_to_price.get(assetX, 0) * symbol_to_price.get(assetY, 0)

    return {
        'depth': depth,
        'assetX_price': symbol_to_price.get(assetX, None),
        'assetY_price': symbol_to_price.get(assetY, None)
    }
    
#Для использования нужно взять информацию по конкретному пулу с помощью функции:
# pool_data = gt.network_pool_address(network="eth", address="0x331399c614ca67dee86733e5a2fba40dbb16827c")
#Мы взяли пул PORK / WETH 1% 
# result = get_price('PORK', 'WETH', pool_data)

# print("Pool Data:")
# print(f"Depth: {result['depth']}")
# print(f"PORK Price in Pool: {result['assetX_price']} USD")
# print(f"WETH Price in Pool: {result['assetY_price']} USD")



def get_historical_data(assetX: str, assetY: str, start_date = None, 
                        end_date = None, time_step = '1h'):
    """
        This function returns a historical data of a pool state and trunsactions

        Atributes:
            assetX, str - a ticker name of an asset X
            assetY, str - a ticker name of an asset Y
            start_date, str - a date from which to start aggregating data, 
                              if not provided, start from the first transaction in history
            end_date, str - a date until which to agregate data,
                            if not provided, get data until the current date
            time_step, str - a time step, to agregate data, by default equals 1 hour

        Returns:
            data, dict (?)
    """
    pass
