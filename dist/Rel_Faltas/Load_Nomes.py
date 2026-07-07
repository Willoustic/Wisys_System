arquivo = open("Rel_Faltas\\nome_do_contato.txt", 'r')

posto_nomes = arquivo.read().split('\n')
nomes = {}

for dados in posto_nomes:
    nomes[dados.split(';')[0]] = dados.split(';')[1]

