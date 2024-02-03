import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from .DEX_module import DEX

from helper import clear_window
from helper import is_integer, is_float, is_numeric, is_None_and_empty_string
from exceptions import SimulationParamsError

Labels_font = ('Arial', 30)

# TODO: we need to make json with available stocks, amms to check from 

class StarterSetting:
    """
    
    """
    def __init__(self, main_menu,  window: tk.Tk) -> None:
        """
        
        """
        self.window = window
        self.main_menu = main_menu

        self.lp_type = None
        self.lp_assetX, self.lp_assetX_volume = None, None
        self.lp_assetY, self.lp_assetY_volume = None, None
        self.amm_type, self.noisy_lt_num = None, None

        self.back_btn, self.start_btn = None, None

    def draw_main(self):
        """
        
        """
        main_canvas = tk.Canvas(self.window)
        main_canvas.pack(anchor=tk.CENTER, expand=True)

        # TODO: pack into iterable function
        tk.Label(main_canvas, text='Liqudity Pool (LP) type:', font=Labels_font).grid(row=0, column=0, padx=20, pady=7)
        self.lp_type = ttk.Combobox(main_canvas, values=['Constant', 'Stochastic'], font=Labels_font,
                                    width=10)
        self.lp_type.grid(row=0, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='LP asset X:', font=Labels_font).grid(row=1, column=0, padx=10, pady=7)
        self.lp_assetX = ttk.Combobox(main_canvas, values=['BTC', 'ETH'], font=Labels_font,
                                      width=10)
        self.lp_assetX.grid(row=1, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='Asset Amount:', font=Labels_font).grid(row=2, column=0, padx=10, pady=7)
        self.lp_assetX_volume = ttk.Spinbox(main_canvas, font=Labels_font, width=10, 
                                            from_=0.01, to=1000, increment=0.01)
        self.lp_assetX_volume.grid(row=2, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='LP asset Y:', font=Labels_font).grid(row=3, column=0, padx=10, pady=7)
        self.lp_assetY = ttk.Combobox(main_canvas, values=['USDC', 'USDT'], font=Labels_font,
                                      width=10)
        self.lp_assetY.grid(row=3, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='Asset Amount:', font=Labels_font).grid(row=4, column=0, padx=10, pady=7)
        self.lp_assetY_volume = ttk.Spinbox(main_canvas, font=Labels_font, width=10, 
                                            from_=0.01, to=1000, increment=0.01)
        self.lp_assetY_volume.grid(row=4, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text='AMM type:', font=Labels_font).grid(row=5, column=0, padx=10, pady=7)
        self.amm_type = ttk.Combobox(main_canvas, values=['Uniswap V3', 'SUMM', 'Weighted SUMM'],
                                     font=Labels_font, width=10)
        self.amm_type.grid(row=5, column=1, padx=10, pady=7)

        tk.Label(main_canvas, text="Noisy LT amount:", font=Labels_font).grid(row=6, column=0,
                                                                              padx=10, pady=7)
        self.noisy_lt_num = ttk.Spinbox(main_canvas, font=Labels_font, width=10,
                                        from_=1, to=50, increment=1)
        self.noisy_lt_num.grid(row=6, column=1, padx=10, pady=7)

        start_exit_canvas = tk.Canvas(main_canvas, width=30)
        start_exit_canvas.grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky='we')

        self.back_btn = tk.Button(start_exit_canvas, text='Back', background='red', font=Labels_font,
                                  command=self._back_to_main_menu)
        self.back_btn.grid(row=0, column=0, pady=3, padx=20, sticky='e')

        tk.Label(start_exit_canvas, width=15, font=Labels_font).grid(row=0, column=1)

        self.start_btn = tk.Button(start_exit_canvas, text='Start', background='green', font=Labels_font,
                                   command=self._run_modulation)
        self.start_btn.grid(row=0, column=2, pady=3,padx=10, sticky='e')


    def _back_to_main_menu(self) -> None:
        clear_window(self.window, 'pack')
        self.main_menu.draw_main()


    def _run_modulation(self) ->None:
        try:
            data = {}
            if not is_None_and_empty_string(self.lp_type.get()):
                data['lp_type'] = self.lp_type.get().strip()
            else:
                raise SimulationParamsError('Liquidity Pool type is empty', '')
            
            # TODO: we need to check from available
            if not is_None_and_empty_string(self.lp_assetX.get()):
                data['lp_assetX'] = self.lp_assetX.get().strip()
            else:
                raise SimulationParamsError('Asset is not available', self.lp_assetX.get())
            

            if not is_None_and_empty_string(self.lp_assetX_volume.get()) and \
                is_float(self.lp_assetX_volume.get().strip()) and \
                    float(self.lp_assetX_volume.get().strip()) > 0.01:

                data['lp_assetX_volume'] = float(self.lp_assetX_volume.get())
            else:
                raise SimulationParamsError(f'Asset {self.lp_assetX.get()} volume must be numeric', 
                                            self.lp_assetX_volume.get())
            
            # TODO: we need to check from available
            if self.lp_assetY.get() is not None and self.lp_assetY.get().strip() != '':
                data['lp_assetY'] = self.lp_assetY.get()
            else:
                raise SimulationParamsError('Asset is not available', self.lp_assetY.get())

        
            if not is_None_and_empty_string(self.lp_assetY_volume.get()) and \
                is_float(self.lp_assetY_volume.get().strip()) and \
                    float(self.lp_assetY_volume.get().strip()) > 0.01:

                data['lp_assetY_volume'] = float(self.lp_assetY_volume.get())
            else:
                raise SimulationParamsError(f'Asset {self.lp_assetY_volume.get()} volume must be numeric',
                                            self.lp_assetY_volume.get())

            # TODO: we need to check from available
            if self.amm_type.get() is not None and self.amm_type.get().strip() != '':
                data['amm_type'] = self.amm_type.get().strip()
            else:
                raise SimulationParamsError('Not valid AMM type', self.amm_type.get().strip())

            
            if not is_None_and_empty_string(self.noisy_lt_num.get()) and \
                is_integer(self.noisy_lt_num.get().strip()) and int(self.noisy_lt_num.get().strip()) >= 0:

                data['noisy_lt_num'] = int(self.noisy_lt_num.get().strip())
            else:
                raise SimulationParamsError('Noisy traders number must be integer', self.noisy_lt_num.get().strip())
            
            dm = DEX(self.window)

            clear_window(self.window, 'pack')
            dm.draw_main()

        except Exception as e:
            messagebox.showerror(e.args)


