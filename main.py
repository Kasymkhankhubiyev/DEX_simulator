from tkinter import messagebox

from helper import create_window

import MainMode.DEX_module as dex
import MainMode.MainMenu as mm


def on_closing():
    """
        обрабатываем закрытие программы запрашиваем подтверждение о закрытии.
    """
    
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти?'):
        win.destroy()


if __name__ == "__main__":
    win = create_window()

    win.protocol('WM_DELETE_WINDOW', on_closing)

    # main_mode = dex.DEX(win)
    main_mode = mm.MainMenu(win)
    main_mode.draw_main()

    win.mainloop()