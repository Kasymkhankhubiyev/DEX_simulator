def get_coin_cost(coin: str) -> float:
    """
        returns a cost of a given coin from Deribit
    """

    if coin == 'BTC':
        return 42600.0
    elif coin == 'ETH':
        return 2605.2