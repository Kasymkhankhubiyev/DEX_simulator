import tkinter as tk

from helper import clear_window
from .SimulationSettings import StarterSetting


btns_font = ('Arial', 35)

class MainMenu:
    def __init__(self, window) -> None:
        self.window = window

    def draw_main(self):
        place_canvas = tk.Canvas(self.window)
        place_canvas.pack(anchor=tk.CENTER, expand=True)

        self.arbitrage_mode_btn = tk.Button(place_canvas, text='Arbitrage', font=btns_font)
        self.arbitrage_mode_btn.grid(row=0, column=0, pady=10)

        self.modulation_mode_btn = tk.Button(place_canvas, text='Simulator', font=btns_font,
                                             command=self._go_to_modulation)
        self.modulation_mode_btn.grid(row=1, column=0, pady=10)

    def _go_to_modulation(self):
        clear_window(self.window, 'pack')
        self.window.update()

        simulation_settings_window = StarterSetting(self.window)
        simulation_settings_window.draw_main()
