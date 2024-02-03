


def get_pool_data(assetX: str, assetY: str) -> dict:
    """
        The function returns a pool state, including its depth,
        current prices of X and Y assets in the pool

        Atributes:
            assetX, str - ticker name of the first asset
            assetY, str - ticker name of the second asset

        Returns:
            data, dict - a dictionary with data describing a pool state,
                        in a following format:
                            data = {'depth': (float) a pool depth,
                                    'assetX_price': (float) an asset X price in the pool,
                                    'assetY_price': (float) an asset Y price in the pool}
    """
    # TODO: FOR Alexander
    # need to make a function that gets data trough API, packs in a specific format 
    # and returns data

    pass


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
