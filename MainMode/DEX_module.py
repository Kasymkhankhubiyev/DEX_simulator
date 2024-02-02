# from tkinter import Tk, Canvas
import tkinter as tk

from .Graph import UniswapCanvas


label_font = ('TimesNewRoman', 20)

class DEX:
    """
    
    """
    def __init__(self, window: tk.Tk) -> None:
        """

        """

        self.window = window
        self.canvas, self.pool_canvas = None, None


    def draw_main(self) -> None:
        
        upper_line = tk.Canvas(self.window, relief=tk.RIDGE)
        upper_line.grid(row=0, column=0, columnspan=3, padx=10, pady=15)
        tk.Label(upper_line, text='DEX -- BTC/USDC', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0, column=0, 
                                                         padx=5, rowspan=2,
                                                         sticky='w')
        tk.Label(upper_line, text='DEPTH -- 10000', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0,column=1, 
                                                         padx=5, rowspan=2,
                                                         sticky='w')
        
        tk.Label(upper_line, text='BTC amount -- 10000', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0,column=2, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        tk.Label(upper_line, text='USDC amount -- 10000', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1,column=2, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        
        tk.Label(upper_line, text='BTC pool price: x_p', 
                 relief=tk.SUNKEN, font=label_font,
                 foreground='red').grid(row=0, column=3, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        tk.Label(upper_line, text='BTC stock price: x_s', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1, column=3, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        
        tk.Label(upper_line, text='USDC pool price: y_p', 
                 relief=tk.SUNKEN, font=label_font).grid(row=0, column=4, 
                                                         padx=5, pady=3,
                                                         sticky='w')
        tk.Label(upper_line, text='USDC stock price: y_n', 
                 relief=tk.SUNKEN, font=label_font).grid(row=1, column=4, 
                                                         padx=5, pady=3,
                                                         sticky='w')

        amm_canvas = tk.Canvas(self.window)
        amm_canvas.grid(row=1, column=0)
        amm_graph = UniswapCanvas(amm_canvas, 'BTC', 'USDT')
        amm_graph.draw({})
