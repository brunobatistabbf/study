"""
Faça uma lista de compra
O usuario pode adicionar, apagar e listar
"""
import os

lista=[]
while True:
    print("Selecione uma opção: \n")
    opcao = input('[i]Inserir [a]Apagar [l]listar: [s]Sair \n')

    if opcao == 'i':
        valor = input('valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha um indice para apagar: ')

        try:
            indice = int(indice_str)
        except IndexError:
            print("Não foi possivel encontrar o indice")
        except ValueError:
            print("Insira uma valor inteiro")
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 's':
        print('saindo.')
        break

    else:
        print("Opção invalida: ")
