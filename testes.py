"""TESTES"""

from Sites.bot_chrome import BotMaster

def sites():
    """WHILE PARA RODAR"""
    while True:
        while True:
            try:
                posto = int(input('Selecione o Posto: '))
            except ExceptionGroup as e:
                print(e)
                print("Posto inválido!")

            if posto < 4 and posto >= 0:
                break


        if posto == 0:
            break
        else:
            BotMaster(posto).run()

sites()
