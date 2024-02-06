from geckoterminal_api import GeckoTerminalAPI


def get_pools(assetX='eth'):
    """
        returns available pools list

        Arguments: 
            assetX, str - name of an asset

        Retruns:
            pools: list
            pools_data: {pool_name: {
                            base_token_price_usd: float,
                            base_token_price_quote: float,
                            quote_token_price_usd: float,
                            quote_token_price_base: float,
                            market_cap_usd: float,
                            price_change_percentage_h1: float,
                            price_change_percentage_h24: float
            }}
    """
    gt = GeckoTerminalAPI()
    res = gt.network_trending_pools(assetX.lower())
    data = res['data']

    pools = [_data['attributes']['name'] for _data in data if _data['attributes']['market_cap_usd'] is not None]

    pools_data = {}
    for _data in data:
        if _data['attributes']['market_cap_usd'] is not None:
            pools_data [_data['attributes']['name']] = {
                'base_token_price_usd': _data['attributes']['base_token_price_usd'],
                'base_token_price_quote': _data['attributes']['base_token_price_quote_token'],
                'quote_token_price_usd': _data['attributes']['quote_token_price_usd'],
                'quote_token_price_base': _data['attributes']['quote_token_price_base_token'],
                'market_cap_usd': _data['attributes']['reserve_in_usd'],
                'price_change_percentage_h1': _data['attributes']['price_change_percentage']['h1'],
                'price_change_percentage_h24': _data['attributes']['price_change_percentage']['h24']} 
    
    return pools, pools_data