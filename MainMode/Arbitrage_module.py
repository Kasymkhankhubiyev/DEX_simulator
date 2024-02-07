import tkinter as tk


from .Graph import UniswapCanvas
from .pool_eval import get_assets_num


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
        M, N = get_assets_num(self.pool_name)
        amm_canvas = tk.Canvas(self.window, borderwidth=10)
        amm_canvas.grid(row=1, column=0, padx=10, pady=10)
        ## -- ## -- ## -- ## -- ##
        liq_taker_canvas = tk.Canvas(self.window)
        liq_taker_canvas.grid(row=1, column=1, padx=10, pady=10)

        liq_taker_canvas_row_num = 0

        tk.Label(liq_taker_canvas, text='Глубина LP:').grid(row=liq_taker_canvas_row_num, 
                                                            column=0, padx=5, pady=5)
        pool_depth =float(self.pool_data['market_cap_usd'])/float(self.pool_data['base_token_price_usd'])
        tk.Label(liq_taker_canvas, text=f"{pool_depth:.5f}").grid(row=liq_taker_canvas_row_num, 
                                                                  column=1, padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text=f"1 {self.pool_name.split('/')[0].strip()} =" +\
                  f" {float(self.pool_data['quote_token_price_base']):.5f} " +\
                    f"{self.pool_name.split('/')[-1].strip()}").grid(row=liq_taker_canvas_row_num,
                                                                     column=0, columnspan=2, 
                                                                     padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        # TODO: make an appropriate output format for a low price tockens
        tk.Label(liq_taker_canvas, text=f"1 {self.pool_name.split('/')[-1].strip()} =" +\
                    f" {float(self.pool_data['base_token_price_quote']):.9f} " +\
                        f"{self.pool_name.split('/')[-1].strip()}").grid(row=liq_taker_canvas_row_num, 
                                                                         column=0, columnspan=2, 
                                                                         padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text='Кошелек:').grid(row=liq_taker_canvas_row_num, 
                                                         column=0, columnspan=2)
        liq_taker_canvas_row_num += 1
        tk.Label(liq_taker_canvas, text=f'{self.pool_name.split("/")[0].strip()}').grid(row=liq_taker_canvas_row_num, 
                                                                                        column=0, 
                                                                                        padx=5, pady=5)
        tk.Label(liq_taker_canvas, text='100').grid(row=liq_taker_canvas_row_num, column=1, padx=5, pady=5)
        liq_taker_canvas_row_num += 1
        tk.Label(liq_taker_canvas, text=f'{self.pool_name.split("/")[1-1].strip()}').grid(row=liq_taker_canvas_row_num, 
                                                                                          column=0, 
                                                                                          padx=5, pady=5)
        tk.Label(liq_taker_canvas, text='100').grid(row=liq_taker_canvas_row_num, column=1, padx=5, pady=5)


        ## -- ## -- ## -- ## -- ##
        amm_data = {'assetX': self.pool_name.split('/')[0].strip(),
                    'assetY': self.pool_name.split('/')[-1].strip(),
                    'assetX_volume': M,
                    'assetY_volume': N,
                    'quote_price_base': float(self.pool_data['quote_token_price_base']),
                    'pool_volume': float(self.pool_data['market_cap_usd']) / float(self.pool_data['base_token_price_usd'])}
        
        amm_graph = UniswapCanvas(amm_canvas, amm_data)
        amm_graph.draw({})
