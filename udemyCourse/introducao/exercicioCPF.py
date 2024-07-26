"""
Codigo de gerador de CPF
"""

cpf = 'Insira o cpf ai sem - e . apenas os primeiros 9 digitos'

novoDigito = cpf[:9]
contadorRegressivo = 10

resultadoPrimeiroDigito = 0

for digito1 in novoDigito:
    resultadoPrimeiroDigito += int(digito1) * contadorRegressivo
    contadorRegressivo -= 1

digito1 =  (resultadoPrimeiroDigito * 10) % 11
digito1 =  digito1 if digito1 <= 9 else 0
print(digito1)

#segundo digito
decimoDigito = novoDigito + str(digito1)
contadorRegressivo2 = 11

resultadoSegundoDigito = 0

for digito in decimoDigito:
    resultadoSegundoDigito += (int(digito) * contadorRegressivo2)
    contadorRegressivo2 -= 1
digito2 = (resultadoSegundoDigito * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

print(digito2)

novoCPF = f'{novoDigito}{digito1}{digito2}'
print(novoCPF)