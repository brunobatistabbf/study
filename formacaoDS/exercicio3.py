#Crie um programa que leia o peso de uma carga em numeros inteiros.Se o peso for até 10kg, informe que o valor será
#de R$500. Entre 11 e 20kg, informe que o valor será de R$80. Se for maior que 20 informe que o transporte não é aceito.
#testar varios pesos


def peso_carga(peso):
    if peso <= 10:
        print("Valor: R$ 500")
    elif peso == 11 or peso == 20 or peso > 11 < 20:
        print("Valor: R$ 80")
    elif peso > 20:
        print("Transporte não aceito")

valor = input("Insira o valor da carga")

try:
    valor_int = int(valor)
except:
    print("Não foi possivel converter o peso da carga para inteiro")

peso_carga(valor_int)