# from tkinter import Tk, Canvas
import tkinter as tk

from .Graph import UniswapCanvas
from .Deribit import get_coin_cost


label_font = ('TimesNewRoman', 20)

class DEX:
    """
        Class that runs a modulation of AMM
    """
    def __init__(self, window: tk.Tk, data: dict) -> None:
        """
            Atributes:
                window, tk.Tk - main graphic window to display on
                data, dict - data dict with settings for modulation,
                            contains following structural data:

                            data = {
                                'lp_type': (str) type of liqudity pool; might be constant, or stochastic,
                                'lp_assetX': (str) a name of asset X in LP,
                                'lp_assetX_volume': (float) a volume of the asset X,
                                'lp_assetY': (str) a name of asset Y in LP,
                                'lp_assetY_volume': (float) a volume of the asset Y,
                                'amm_type: (str) a name of AMM, the function that balance a cost of assets
                                'noisy_lt_num': (int) number of noisy liquidity traders interacting in a Pool,
                                                available only for stochastic pools
                            }
        """

        self.window = window
        self.canvas, self.pool_canvas = None, None
        self.data = data
        print('created')


    def draw_main(self) -> None:
        
        # print('start')
        upper_line = tk.Canvas(self.window, relief=tk.RIDGE)
        upper_line.grid(row=0, column=0, columnspan=3, padx=10, pady=15)
        tk.Label(upper_line, text=f'DEX -- {self.data["lp_assetX"]}/{self.data["lp_assetY"]}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0, column=0, 
                                                         padx=5, rowspan=2,
                                                         sticky='w')
        tk.Label(upper_line, text=f'DEPTH -- {self.data["lp_assetX_volume"]*self.data["lp_assetY_volume"]:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0,column=1, 
                                                         padx=5, rowspan=2,
                                                         sticky='w')
        # print('start')
        tk.Label(upper_line, text=f'{self.data["lp_assetX"]} amount -- {self.data["lp_assetX_volume"]:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0,column=2, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        tk.Label(upper_line, text=f'{self.data["lp_assetY"]} amount -- {self.data["lp_assetY_volume"]:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1,column=2, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        # print('start')
        tk.Label(upper_line, 
                 text=f'{self.data["lp_assetX"]} pool price: {self.data["lp_assetX_volume"]*self.data["lp_assetY_volume"] / self.data["lp_assetX_volume"]:.5f}', 
                 relief=tk.SUNKEN, font=label_font,
                 foreground='red').grid(row=0, column=3, 
                                        padx=5, pady=3,
                                        sticky='w')
        
        coint_cost = get_coin_cost(self.data["lp_assetX"])
        # print('start')
        tk.Label(upper_line, text=f'{self.data["lp_assetX"]} stock price: {coint_cost:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1, column=3, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        
        tk.Label(upper_line, 
                 text=f'{self.data["lp_assetY"]} pool price: {self.data["lp_assetX_volume"]*self.data["lp_assetY_volume"] / self.data["lp_assetX_volume"]:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0, column=4, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        tk.Label(upper_line, text=f'{self.data["lp_assetY"]} stock price: {1 / coint_cost:.5f}', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1, column=4, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        # print('start')
        amm_canvas = tk.Canvas(self.window)
        amm_canvas.grid(row=1, column=0)
        amm_data = {'assetX': self.data["lp_assetX"],
                    'assetY': self.data["lp_assetY"],
                    'assetX_volume': float(self.data["lp_assetX_volume"]),
                    'assetY_volume': float(self.data["lp_assetY_volume"])}
        amm_graph = UniswapCanvas(amm_canvas, amm_data)
        # print('start')
        amm_graph.draw()
