from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Canvas
from tkinter import BOTH

from exceptions import AMM_GRAP_ERROR
from .Deribit import get_coin_cost

import numpy as np


class UniswapCanvas:
    def __init__(self, canvas: Canvas, amm_data: dict) -> None:
        """
            amm_data = {'assetX': ,
                        'assetY': ,
                        'assetX_volume': ,
                        'assetY_volume':
                        'coin_cost': }
        
        """
        self.window = canvas
        self.fig = Figure()
        self.data = amm_data

        self.ax = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, self.window)

        self.ax.grid()
        self.ax.set_xlabel(f'{self.data["assetX"]}')
        self.ax.set_ylabel(f'{self.data["assetY"]}')
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    

    def draw(self, data_to_plot: dict) -> None:

        self.ax.cla()
        self.ax.set_xlabel(f'{self.data["assetX"]}')
        self.ax.set_ylabel(f'{self.data["assetY"]}')

        x = np.linspace(200, 500, 100)
        y = float(self.data["pool_volume"]) / x

        self.ax.plot(x, y, label='Pool')
        
        self.canvas.draw()