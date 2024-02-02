import tkinter as tk

from tkinter import ttk

from helper import clear_window

Labels_font = ('Arial', 30)

class StarterSetting:
    def __init__(self, window: tk.Tk) -> None:

        self.window = window

    def draw_main(self):
        main_canvas = tk.Canvas(self.window)
        main_canvas.pack(anchor=tk.CENTER, expand=True)

        tk.Label(main_canvas, text='Liqudity Pool (LP) type:', font=Labels_font).grid(row=0, column=0, padx=20, pady=7)
        self.lp_type = ttk.Combobox(main_canvas, values=['Constant', 'Stochastic'], font=Labels_font)
        self.lp_type.grid(row=0, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='LP asset X:', font=Labels_font).grid(row=1, column=0, padx=10, pady=7)
        self.lp_assetX = ttk.Combobox(main_canvas, values=['BTC', 'ETH'], font=Labels_font)
        self.lp_assetX.grid(row=1, column=1, padx=10, pady=7)

        

    def _clear_window(self):
        clear_window(self.window, 'pack')

