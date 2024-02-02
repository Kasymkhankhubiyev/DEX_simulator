from tkinter import Tk, PhotoImage
from tkinter import messagebox


def create_window() -> Tk:
    """
    Создаем главное окно
    :return: window
    """

    window = Tk()
    window.title("DEX Simulator")
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    window.geometry("{}x{}".format(w-10, h-1))
    # icon = PhotoImage(file='media/logo.png')
    # window.iconphoto(False, icon)
    return window


def clear_window(window: Tk, widget_place_type: str) -> None:
    
    if widget_place_type == 'place':
        _slaves = window.place_slaves()
    elif widget_place_type == 'pack':
        _slaves = window.pack_slaves()
    elif widget_place_type == 'grid':
        _slaves = window.grid_slaves()

    for _slave in _slaves:
        _slave.destroy()