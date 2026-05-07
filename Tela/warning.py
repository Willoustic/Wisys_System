from tkinter import messagebox
from functions.caminho import resource_path

def warning_box():
    messagebox.showinfo(title='Aviso!', message="Para cancelar quaisquer automação ativada\n" \
    "basta arrastar o mouse para o canto superior esquerdo!")