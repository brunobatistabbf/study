#Faça uma função que receba uma string e imprima esta string na forma vertical
#por exemplo, se receber python, deve imprimir
#p
#y
#t
#h
#o
#N
#Uma string do python funciona como uma lista!


def vertical(texto):
    for caractere in texto:
        print(caractere)


lista_str  = input("Insira qualquer palavra")
vertical(lista_str)