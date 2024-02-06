import tkinter as tk


from .Graph import UniswapCanvas


class DEX:
    def __init__(self, window: tk.Tk, data: dict, pool_name: str) -> None:
        """
        
            Arguments:
                window, tk.Tk - main_window
                pool_name, str - a pool name in a format `Base Asset / Quote Asset`
                data, dict: - dictionary with pool data, contains:
                                pools_data: {pool_name: {
                                        base_token_price_usd: float,
                                        base_token_price_quote: float,
                                        quote_token_price_usd: float,
                                        quote_token_price_base: float,
                                        market_cap_usd: float,
                                        price_change_percentage_h1: float,
                                        price_change_percentage_h24: float
                                }
        
        """
        self.window = window
        self.canvas, self.pool_canvas = None, None
        self.pool_data = data
        self.pool_name = pool_name

    def draw(self) -> None:
        amm_canvas = tk.Canvas(self.window, borderwidth=10)
        amm_canvas.grid(row=1, column=0, padx=10, pady=10)
        amm_data = {'assetX': self.pool_name.split('/')[0].strip(),
                    'assetY': self.pool_name.split('/')[-1].strip(),
                    'assetX_volume': self.pool_data['quote_token_price_base'],
                    'assetY_volume': self.pool_data['base_token_price_quote'],
                    'pool_volume': self.pool_data['market_cap_usd']}
        amm_graph = UniswapCanvas(amm_canvas, amm_data)
        amm_graph.draw({})
