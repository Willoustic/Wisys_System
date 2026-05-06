import tkinter as tk

def tela_na_resolução(width, height):
    get = tk.Tk()
    largura = get.winfo_screenwidth()
    altura = get.winfo_screenheight()
    get.destroy()
    x = (largura // 2) - (width // 2)
    y = (altura // 2) - (height // 2)
    geometry = f'{width}x{height}+{x}+{y-50}'
    return geometry


def resolução():
    get = tk.Tk()
    largura = get.winfo_screenwidth()
    altura = get.winfo_screenheight()
    get.destroy()
    return largura, altura
