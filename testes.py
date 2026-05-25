from backend.get_postos import Banco

def printar():
    banco = Banco()
    
    for posto in banco.get_nomes():
        if (banco.get_class(posto) == 'All'):
            print(banco.get_id(posto))

printar()