#Sem funções, temos apenas uma longa lista de instruções. As funções podem ajudá-lo a organizar o código. As funções também podem ser reutilizadas, muitas vezes incluídas em módulos.
#Exemplo simples
#sempre começa com def
def currentYear():
    print('2002')

currentYear()

#multiplicação
def f(x,y):
    return x*y

print(f(3,4))

#função de soma
def soma() :
    mylist = [1,2,3,4,5]
    z = 0
    for x in mylist:
        z = z + (mylist[x])
        x += 1
        #acho que ta errado





