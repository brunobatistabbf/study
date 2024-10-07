# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

def operacao(opcao):
    if (opcao == 1):
        def duplicar(numero):
            return numero * 2

        return duplicar
    elif (opcao == 2):
        def triplicar(numero):
            return numero * 3

        return triplicar
    elif (opcao == 3):
        def quadriplicar(numero):
            return numero * 4

        return quadriplicar
    else:
        print("Opcao Invalida!")
        return None


print("_____________________CALC_NOW______________________")
print("Duplique, triplique e quadruplique qualquer numero")
print(" 1-Duplique\n 2-Triplique\n 3-Quadriplique")
opcao = int(input("Escolha a operação desejada: "))

numero = int(input("Insira o número que deseja realizar a operação"))

recebe_operacao = operacao(opcao)
if recebe_operacao:
    print(f"Resultado{recebe_operacao(numero)}")
else:
    print("Falha ao Proceder")