import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

# from .DEX_module import DEX
from .GeckoAPI import get_pools

from .Deribit import get_coin_cost
from helper import clear_window
from helper import is_integer, is_float, is_numeric, is_None_and_empty_string
from exceptions import SimulationParamsError


Labels_font = ('Arial', 30)


class ArbitrageSetting:
    def __init__(self, window, main_menu) -> None:
        self.window = window
        self.main_menu = main_menu

    def draw(self) -> None:
        main_canvas = tk.Canvas(self.window)
        main_canvas.pack(anchor=tk.CENTER, expand=True)

        tk.Label(main_canvas, text='Choose a pool to trade in:',
                 font=Labels_font).grid(row=0, column=0, padx=20, pady=7)
        
        self.pools, self.pools_data = get_pools()
        """
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
        self.lp_type = ttk.Combobox(main_canvas, values=self.pools,
                                    width=20, height=20,
                                    font=Labels_font)
        self.lp_type.grid(row=0, column=1, padx=10, pady=7)
        self.lp_type.set(self.pools[0])

        self.lp_type.bind('<<ComboboxSelected>>', self._select_handler)

        self._labels_names = ['Base token price in USD', 'Base token price in Quote', 
                        'Quote token price in USD', 'Base token price in Base',
                        'Market volume', 'price 1h change', 'price 24h change']
        
        _labels_values = [self.pools_data[self.pools[0]]['base_token_price_usd'],
                          self.pools_data[self.pools[0]]['base_token_price_quote'],
                          self.pools_data[self.pools[0]]['quote_token_price_usd'],
                          self.pools_data[self.pools[0]]['quote_token_price_base'],
                          self.pools_data[self.pools[0]]['market_cap_usd'],
                          self.pools_data[self.pools[0]]['price_change_percentage_h1'],
                          self.pools_data[self.pools[0]]['price_change_percentage_h24']]
        self._value_label_objects = []

        for idx, (_name, _value) in enumerate(zip(self._labels_names, _labels_values)):
            tk.Label(main_canvas, text=_name, font=Labels_font).grid(row=idx+1, column=0, padx=10, pady=7)
            value_label = tk.Label(main_canvas, text=f'{float(_value):.7f}', font=Labels_font)
            value_label.grid(row=idx+1, column=1, padx=10, pady=7)
            self._value_label_objects.append(value_label)

        ## -- ## -- ## Back and Start buttions ## -- ## -- ##

        # start_exit_canvas = tk.Canvas(main_canvas, width=30)
        # start_exit_canvas.grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky='we')

        self.back_btn = tk.Button(main_canvas, text='Back', font=Labels_font,
                                  command=self._back_to_main_menu, bg='red')
        self.back_btn.grid(row=len(_labels_values)+1, column=0, pady=7, padx=10)

        self.start_btn = tk.Button(main_canvas, text='Start', bg='green', font=Labels_font,
                                   command=self._run_modulation)
        self.start_btn.grid(row=len(_labels_values)+1, column=1, pady=7, padx=10)

    def _get_labels_values(self, pool_name: str) -> list:
        return [self.pools_data[pool_name]['base_token_price_usd'],
                self.pools_data[pool_name]['base_token_price_quote'],
                self.pools_data[pool_name]['quote_token_price_usd'],
                self.pools_data[pool_name]['quote_token_price_base'],
                self.pools_data[pool_name]['market_cap_usd'],
                self.pools_data[pool_name]['price_change_percentage_h1'],
                self.pools_data[pool_name]['price_change_percentage_h24']]

    def _select_handler(self, event):
        pool_name = self.lp_type.get()
        label_values = self._get_labels_values(pool_name)
        for lbl_obj, lbl_val in zip(self._value_label_objects, label_values):
            lbl_obj.configure(text=f'{float(lbl_val):.7f}')

    def _back_to_main_menu(self) -> None:
        clear_window(self.window, 'pack')
        self.main_menu.draw_main()

    def _run_modulation(self) -> None:
        pass