# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print("Opções:")

    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i + 1}. {opcao}")

    resposta = input("Escolha a resposta correta:")

    if pergunta["Opções"][int(resposta) - 1] == pergunta['Resposta']:
        print("Resposta correta!")
    else:
        print("Resposta errada!")

    print()