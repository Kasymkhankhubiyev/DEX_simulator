from GeckoAPI import get_pools

def calculate_assets_num(pool_volume_usd, base_price_usd, quote_price_usd, base_price_quote):
    pool_volume_quote = pool_volume_usd / quote_price_usd

    Descriminant = base_price_quote ** 2 * pool_volume_usd ** 2 - 4 * base_price_usd * quote_price_usd * \
          pool_volume_quote * base_price_quote
    
    N_1 = (base_price_quote * pool_volume_quote - Descriminant**(0.5)) / (2 * base_price_usd * base_price_quote)
    N_2 = (base_price_quote * pool_volume_quote + Descriminant**(0.5)) / (2 * base_price_usd * base_price_quote)

    N = max(0, max(N_1, N_2))

    M = pool_volume_quote / N / base_price_quote

    # print(pool_volume_usd)

    # N = (pool_volume_usd - pool_volume_quote * quote_price_usd) / (base_price_usd - base_price_quote * quote_price_usd)
    # M = pool_volume_quote - N * base_price_quote

    print(M, N)


if __name__ == "__main__":
    pools, pools_data = get_pools()

    data = pools_data[pools[0]]

    # print(data)
    print(pools[0])

    calculate_assets_num(pool_volume_usd=float(data['market_cap_usd']),
                         base_price_usd=float(data['base_token_price_usd']),
                         quote_price_usd=float(data['quote_token_price_usd']),
                         base_price_quote=float(data['base_token_price_quote']))