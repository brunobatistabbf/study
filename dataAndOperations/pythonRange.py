#A função range() gera uma lista de números. Isso é muito útil
#ao criar novas listas ou ao usar loops
#for: pode ser usado para ambos

#Python range() parameters
#termo de parada
number = 9
print(range(number))


#tambem pode definir
#range(start, stop, step)

#escrevendo uma lista de 100 numeros
x = list(range(100))
print(x)

#contar de 1 a 100
y = list(range(1, 100))
print(y)




for i in range(1, 11):
    print(i)

for i in range( 0 , 25 , 5 ):
    print(i)

#crie uma lista de mil numeros
z = list(range(1001))
print(z)
print(min(z))
print(max(z))
print()
par = []
impar = []

for i in z:
    if (i % 2 == 0):
       par.append(i)
    else:
        impar.append(i)

print(par)
print(impar)