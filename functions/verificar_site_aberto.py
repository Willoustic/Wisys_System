def verificar_pagina_aberta():
    from time import sleep
    from pyperclip import copy, paste
    import pyautogui as px
    valor = copy('')
    while True:
        sleep(1)
        px.hotkey('ctrl', 'a')
        px.hotkey('ctrl', 'c')
        px.write('.')
        valor = paste()
        if (valor != ''):
            px.hotkey('ctrl', 'a')
            px.press('del')
            break