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
        