#adicionar item a uma lista append()
#para remover do final da lista pop()

x = [1 , 2 , 3]
x.append(4)
print(x)

x.append(5)
print(x)

x.pop()
print(x)

#Acessar itens

print(x[0])
print(x[1])
print(x[-1])

#Dada a lista y = [6,4,2] some os itens 12, 8 e 4.
#Altere o 2º item da lista para 3.
z = [6 ,4 ,2]
z.append(12)
z.append(8)
z.append(4)
print(z)
z[1] = 3
print(z)