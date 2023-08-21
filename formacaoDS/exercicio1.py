#Faça um programa que tenha uma função chamada amplitude.
# A função deve receber uma lista e imprimir a amplitude.
# Crie também um código para testar sua função


def amplitude(lista):
    if len(lista) == 0:
        print("Erro: Lista Vazia!")
        return None
    else:
        return max(lista) - min(lista)

lista_de_valores = [2, 10, 5, 8, 15, 3]
resultado = amplitude(lista_de_valores)
print(f"A amplitude da lista é: {resultado}")
