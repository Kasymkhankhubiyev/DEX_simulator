import tkinter as tk


from .LTaker import LTaker
from .Graph import UniswapCanvas
from .pool_eval import get_assets_num

label_font = ('TimesNewRoman', 20)
title_label_font = ('TimesNewRoman', 30)

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

        self.liq_taker = LTaker({})
        self.amm = None


    def draw(self) -> None:
        M, N = get_assets_num(self.pool_name)
        tk.Button(self.window, text='Back to Menu', bg='red', font=title_label_font,
                  command=self._go_to_main_menu).grid(row=0, column=0, sticky='w', pady=10, padx=10)
        amm_canvas = tk.Canvas(self.window, borderwidth=10)
        amm_canvas.grid(row=1, column=0, padx=10, pady=10)
        ## -- ## -- ## -- ## -- ##
        liq_taker_canvas = tk.Canvas(self.window)
        liq_taker_canvas.grid(row=1, column=1, padx=10, pady=10)

        liq_taker_canvas_row_num = 0

        tk.Label(liq_taker_canvas, text='LP Depth:',
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                        column=0, padx=5, pady=5)
        pool_depth =float(self.pool_data['market_cap_usd'])/float(self.pool_data['base_token_price_usd'])
        tk.Label(liq_taker_canvas, text=f"{pool_depth:.5f}", 
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                        column=1, padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text=f"1 {self.pool_name.split('/')[-1].strip()} =" +\
                  f" {float(self.pool_data['quote_token_price_base']):.5f} " +\
                    f"{self.pool_name.split('/')[0].strip()}",
                 font=label_font).grid(row=liq_taker_canvas_row_num,
                                        column=0, columnspan=2, 
                                        padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        # TODO: make an appropriate output format for a low price tockens
        tk.Label(liq_taker_canvas, text=f"1 {self.pool_name.split('/')[0].strip()} =" +\
                    f" {float(self.pool_data['base_token_price_quote']):.9f} " +\
                        f"{self.pool_name.split('/')[-1].strip()}",
                        font=label_font).grid(row=liq_taker_canvas_row_num, 
                                                column=0, columnspan=2, 
                                                padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text='Price change', 
                 font=title_label_font, relief=tk.SUNKEN).grid(row=liq_taker_canvas_row_num, column=0, 
                                                         columnspan=2, padx=5, pady=10)
        liq_taker_canvas_row_num += 1

        h1_change = float(self.pool_data['price_change_percentage_h1']) 
        if h1_change < 0:
            h1_color = 'red'
        else: 
            h1_color = 'green'

        tk.Label(liq_taker_canvas, text=f'1 hour: {h1_change:.3f}%', 
                 font=label_font, fg=h1_color).grid(row=liq_taker_canvas_row_num, column=0,
                                                    padx=5, pady=5)
        
        h2_change = float(self.pool_data['price_change_percentage_h24']) 
        if h2_change < 0:
            h2_color = 'red'
        else: 
            h2_color = 'green'

        tk.Label(liq_taker_canvas, text=f'24 hour: {h2_change:.3f}%', 
                 font=label_font, fg=h2_color).grid(row=liq_taker_canvas_row_num, column=1,
                                                    padx=5, pady=5)
        
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text='Wallet:', 
                 font=title_label_font, relief=tk.SUNKEN).grid(row=liq_taker_canvas_row_num, 
                                                                          column=0, columnspan=2)
        liq_taker_canvas_row_num += 1
        tk.Label(liq_taker_canvas, text=f'{self.pool_name.split("/")[0].strip()}',
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                        column=0, sticky='w',
                                        padx=5, pady=5)
        tk.Label(liq_taker_canvas, text='100',
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                       column=1, padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text=f'{self.pool_name.split("/")[-1].strip()}',
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                        column=0, sticky= 'w',
                                        padx=5, pady=5)
        tk.Label(liq_taker_canvas, text='100',
                 font=label_font).grid(row=liq_taker_canvas_row_num, 
                                       column=1, padx=5, pady=5)
        
        liq_taker_canvas_row_num += 1
        
        ## -- ## -- ## -- ## -- ##

        tk.Label(liq_taker_canvas, text='Make order:', 
                 font=title_label_font, relief=tk.SUNKEN).grid(row=liq_taker_canvas_row_num,
                                                               column=0, columnspan=2,
                                                               padx=5, pady=10)
        liq_taker_canvas_row_num += 1

        tk.Label(liq_taker_canvas, text=f'{self.pool_name.split("/")[0].strip()}',
                 font=label_font).grid(row=liq_taker_canvas_row_num, column=0, padx=5, pady=5)
        tk.Entry(liq_taker_canvas, 
                 font=label_font, width=12, relief=tk.SUNKEN, 
                 background='white', borderwidth=5).grid(row=liq_taker_canvas_row_num, 
                                                                   column=1, padx=5, pady=5)
        
        liq_taker_canvas_row_num += 1

        transaction_type = tk.IntVar()

        tk.Checkbutton(liq_taker_canvas, text='Sell', 
                       onvalue=1, offvalue=0, font=label_font,
                       variable=transaction_type,
                       height=3, width=10).grid(row=liq_taker_canvas_row_num, column=0,
                                                padx=5, pady=5)
        tk.Checkbutton(liq_taker_canvas, text='Buy',
                       onvalue=-1, offvalue=0,font= label_font,
                       variable=transaction_type,
                       height=3, width=10).grid(row=liq_taker_canvas_row_num, column=1,
                                                padx=5, pady=5)
        liq_taker_canvas_row_num += 1

        ## -- ## -- ## -- ## -- ##
        amm_data = {'assetX': self.pool_name.split('/')[0].strip(),
                    'assetY': self.pool_name.split('/')[-1].strip(),
                    'assetX_volume': M,
                    'assetY_volume': N,
                    'quote_price_base': float(self.pool_data['quote_token_price_base']),
                    'pool_volume': float(self.pool_data['market_cap_usd']) / float(self.pool_data['base_token_price_usd'])}
        
        amm_graph = UniswapCanvas(amm_canvas, amm_data)
        amm_graph.draw({})


    def _go_to_main_menu(self) -> None:
        pass
