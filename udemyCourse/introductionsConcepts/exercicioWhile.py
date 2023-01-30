"""
Python é uma linguagem de programação multiparadigma. Python foi criado po Guido.
"""

frase = 'Python é uma linguagem de programação multiparadigma. Python foi criado po Guido.'.lower()#minuscula
            #contador
print(frase.count('python'))
#Quantos vezes python aparece na frase
i = 0
qntapareceumaisvezes = 0
letraapareceumaisvezes = ''
#usando while, qual letra apareceu mais vezes
while i < len(frase):
    letra_atual = frase[i]
    quantas = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qntapareceumaisvezes < quantas:
        qntapareceumaisvezes = quantas
        letraapareceumaisvezes =  letra_atual



    i += 1

print("A letra que apareceu mais vezes foi " f'{letraapareceumaisvezes}' " que apareceu " f'{qntapareceumaisvezes}')