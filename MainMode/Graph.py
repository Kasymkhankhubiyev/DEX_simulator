from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Canvas
from tkinter import BOTH

from exceptions import AMM_GRAP_ERROR

import numpy as np


class UniswapCanvas:
    def __init__(self, canvas: Canvas, X=None, Y=None) -> None:
        self.window = canvas
        self.fig = Figure()
        if X is None or Y is None:
            raise AMM_GRAP_ERROR
        
        self.X = X
        self.Y = Y

        self.ax = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, self.window)

        self.ax.grid()
        self.ax.set_xlabel(f'{self.X}')
        self.ax.set_ylabel(f'{self.Y}')
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    

    def draw(self, data: dict) -> None:
        self.ax.cla()
        self.ax.set_xlabel(f'{self.X}')
        self.ax.set_ylabel(f'{self.Y}')

        x = np.linspace(0.5, 70, 100)
        y = 43000 / x

        self.ax.plot(x, y, label='Pool')
        
        # self.ax.plot(data['x_s'], data['E_c_s'], c='red', label='Conduction Band')
        # self.ax.plot(data['x_s'], data['E_f_s'], c='darkorange', label='Fermi Energy')
        # self.ax.plot(data['x_s'][0:round(len(data['x_s']) / 2)],
        #         data['E_as_s'][0:round(len(data['E_as_s']) / 2)], c='green', label='Acceptor Energy')
        # self.ax.plot(data['x_s'], data['E_d_s'], c='blue', label='Donor Energy')
        # self.ax.plot(data['x_s'], data['E_v_s'], c='purple', label='Valence Band')

        # if(data['E_v_s'][0]<0):
        #     self.ax.axhline(-1*data['phi'], c='k', linestyle='dashed')
        # else:
        #     self.ax.axhline(data['phi'], c='k', linestyle='dashed')
        # self.ax.axvline(data['W'], c='k', linestyle='dashed')

        # self.ax.legend(fontsize=10, loc='right')
        self.canvas.draw()