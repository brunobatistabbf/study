"""
tipo lista =  mutavel
suporta varios tipos de valores
indice e fatiamento
metodos uteis: append, insert, pop, del, cler, extend, +
Create read update delete
"""

lista = [123, True, 'Bruno Batista', 1.23]
lista[2] = 'Bruno é Gostoso'
print(lista, type(lista))
del lista[3]
del lista[0]
del lista[0]
lista.append("e Brabo")
lista.append("é Ironia")
lista.insert(1, 1000000)
lista.pop()
print(lista)
listaA = [1, 2, 3]
listaB = [4, 5,6]
listaC = listaA + listaB
print(listaC)
listaA.extend(listaB) #mexe diretamente na lista
print(listaA)