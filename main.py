from tkinter import messagebox

from helper import create_window


def on_closing():
    """
        обрабатываем закрытие программы запрашиваем подтверждение о закрытии.
    """
    
    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти?'):
        win.destroy()


if __name__ == "__main__":
    win = create_window()

    win.protocol('WM_DELETE_WINDOW', on_closing)

    main_mode = None

    win.mainloop()