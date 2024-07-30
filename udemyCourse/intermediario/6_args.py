"""
*args empocotamento e desempacotamento
args - Argumentos não nomeados
"""
#Exemplo somando usando args
def soma(*args):
    total = 0
    for numero in args:
        total = total + numero

    print(total)

soma(1, 3, 5, 34, 67, 90, 5, 34, 1, 2, 3, 4, 4, 4, 96765, 1000000)

#Desempacotamento
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))