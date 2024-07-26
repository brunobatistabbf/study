"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'bruno'
letra_acertadas = ''
numero_tentativas = 10
tentativas = 0 #Resolver bugs de tentativas

while True:
    numero_tentativas -= 1
    letra_digitada = input("Digite uma letra")


    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if palavra_secreta == palavra_formada:
        print("\n \n Você ganhou!!! Parabéns")
        print(f"A palavra secreta era {palavra_secreta}")
        break


    print(palavra_formada)

print("Jogo Fechado")
