# from tkinter import Tk
from customtkinter import CTk
from tkinter import messagebox


def create_window() -> CTk:
    """
    Создаем главное окно
    :return: window
    """

    window = CTk()
    window.title("DEX Simulator")
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    window.geometry("{}x{}".format(w-10, h-1))
    # icon = PhotoImage(file='media/logo.png')
    # window.iconphoto(False, icon)
    return window


def clear_window(window: CTk, widget_place_type: str) -> None:
    
    if widget_place_type == 'place':
        _slaves = window.place_slaves()
    elif widget_place_type == 'pack':
        _slaves = window.pack_slaves()
    elif widget_place_type == 'grid':
        _slaves = window.grid_slaves()

    for _slave in _slaves:
        _slave.destroy()


def is_None_and_empty_string(input: str) -> bool:
    """
        Checks if an imput string is None or empty or not

        Atributes:
            input, str - an input string to check

        Returns:
            is_None_or_empty, bool - True if None or empty, else False
    """
    if input is None or input.strip() == '':
        return True
    else:
        return False
    

def is_float(input: str) -> bool:
    """
        Checks if an input string is a float or not

        Atributes:
            input, str - a string to check

        Returns:
            is_float, bool - True if float, else False
    """
    try:
        float(input)
        return True
    except Exception:
        return False
    

def is_integer(input: str) -> bool:
    """
        Checks if an input string is an integer or not

        Atributes:
            input, str - a string to check

        Returns:
            is_float, bool - True if integer, else False
    """
    try:
        int(input)
        return True
    except Exception:
        return False
    

def is_numeric(input: str) -> bool:
    """
        Checks if an input string is numeric or not

        Atributes:
            input, str - a string to check

        Returns:
            is_numeric, bool - True if numeric, else False
    """
    if is_float(input) or is_integer(input):
        return True
    else:
        return False