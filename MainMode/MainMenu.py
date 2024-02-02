import tkinter as tk

btns_font = ('Arial', 35)

class MainMenu:
    def __init__(self, window) -> None:
        self.window = window

    def draw_main(self):
        place_canvas = tk.Canvas(self.window)
        place_canvas.pack(anchor=tk.CENTER, expand=True)
        self.arbitrage_mode_btn = tk.Button(place_canvas, text='Arbitrage', font=btns_font)
        self.arbitrage_mode_btn.grid(row=0, column=0, pady=10)
        self.modulation_mode_btn = tk.Button(place_canvas, text='Simulator', font=btns_font)
        self.modulation_mode_btn.grid(row=1, column=0, pady=10)

    def _go_to_modulation(self):
        pass

    def clear(self,):
        # self.window.
        pass