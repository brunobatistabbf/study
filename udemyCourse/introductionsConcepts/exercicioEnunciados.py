"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = 0
numeroInput = input("Digite um numero inteiro")
numero = int(numeroInput)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Qunatas horas é agora baseado em :  0-11,  12-17 e 18-23 ")
type(int(horario))
if horario <= 11:
    print("Bom diaaaaaa")
elif horario > 11  <= 17 :
    print("Boa tardeeeeeee")
else:
    print("Boa noiteeeeeeee")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
