#funções no python poder retornar varias variaveis
#Exclusivo do python

def complexfunction(a , b):
    sum = a + b
    return  sum

print(complexfunction(10, 50))


def getPerson():
    name = "Andre"
    age = 22
    country = "BR"
    return  name, age, country

name,age,country = getPerson()
print(name)
print(age)
print(country)

def somase():
    numero1 = 10
    numero2 = 10
    sum = numero1 + numero2
    return numero1, numero2, sum


numero1, numero2, sum = somase()
print(numero1)
print(numero2)
print(sum)

