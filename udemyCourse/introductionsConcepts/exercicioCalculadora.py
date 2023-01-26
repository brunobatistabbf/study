"""Calculadora com While"""

while True:
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    operador = input("Digite o operador (+-/*)")

    numero_valido = None
    numero1float = 0.0
    numero2float = 0.0

    try:
        numero1float = float(numero1)
        numero2float = float(numero2)
        numero_valido =  True
    except:
        numero_valido = None

    if numero_valido == None:
        print("Numeros são invalidos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    #Operações
    print("Realizando sua conta")
    if operador == '+':
        print(numero1float + numero2float)
    elif operador == '-':
        print(numero1float - numero2float)
    elif operador == '/':
        print(numero1float / numero2float)
    elif operador == '*':
        print(numero1float * numero2float )
    else:
        print("Insira um operador valido")
        continue

    sair = input("Quer sair? [s/n]")
    sair = sair.lower().startswith('s') #colocando em minusculo e verficando se começa com s de sair

    if sair is True:
        break

