"""
Empacotamento e Desempacotamento
"""

nomes = ['maria', 'helena', 'luiz']
nome1, nome2, nome3 = nomes
print(nome2)

devendo = ['mauro', 'hugo', 'luiza']
_, nomeH, *_ = devendo
print(nomeH) #nome do mauro
print(_) #é o restante


