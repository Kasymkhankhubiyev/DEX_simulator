from .GeckoAPI import get_pools

def _calculate_assets_num(pool_volume_usd: float, base_price_usd: float, quote_price_usd: float, 
                         base_price_quote: float, quote_price_base: float) -> 'tuple[float, float]':

    """
    
        Assume M is a number of quote tocken and N a number of base tocken
        Let QT_{BT} be a price of a quote tocken in base tocken, and
        BT_{BT} be a price of base tocken in base tocken, BT_{BT} equals 1.
        Let P_Q, P_B be prices of quote and base tockens in USD respectfully,
        and PV a pool volume in USD.

        From one hand, assuming the pool AMM is Uniswap v3, a tocken price QT_{BT} derives from
        the following equation: M * QT_{BT} = N * BT_{BT} => (*) M = \frac{N}{QT_{BT}} is
        just a number. 

        From another hand, pool volume PV in USD is calculated as a total price of tockens in USD:
        (**) M * P_Q + N * P_B = PV

        considering (*) from (**) we get: N = \frac{PV * QT_{BT}}{P_Q + P_B * QT_{BT}}
        and M = \frac{N}{QT_{BT}} = \frac{PV * QT_{BT}}{P_Q + P_B * QT_{BT}}

        Arguments:
            pool_volume_usd, float - pool volume in USD (PV)
            base_price_usd, float - base tocken price in USD (PB)
            quote_price_usd, float - quote tocken price in USD (PQ)
            base_price_quote, float - base tocken price in quote (BT_{QT})
            quote_price_base, float - qoute tocken price in base (QT_{BT})

        Returns:
            M, float - number of quote tockens
            N, float - number of base tockens

    """

    N = pool_volume_usd / (quote_price_usd / quote_price_base + base_price_usd)

    M = N / quote_price_base

    return M, N

def get_assets_num(pool_name: str) -> 'tuple[float, float]':
    """
        returns assets number for a given pool name

        Arguments:
            pool_name, str - a pool name in a format `Base tocken / Quote tocken`

        Returns:
            M, float - number of quote tockens
            N, float - number of base tockens
    
    """
    _, pools_data = get_pools()

    data = pools_data[pool_name]

    return _calculate_assets_num(pool_volume_usd=float(data['market_cap_usd']),
                                base_price_usd=float(data['base_token_price_usd']),
                                quote_price_usd=float(data['quote_token_price_usd']),
                                base_price_quote=float(data['base_token_price_quote']),
                                quote_price_base=float(data['quote_token_price_base']))