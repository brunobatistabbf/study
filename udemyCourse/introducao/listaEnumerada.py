"""
Lista enumerada
"""

lista = ['Maria', 'Joao', 'Felipe']

lista_enumerada = enumerate(lista)


for nome in lista_enumerada:
    print(nome)

#or

for indice, none in enumerate(lista):
    print(indice, nome)
