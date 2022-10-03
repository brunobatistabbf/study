#metodo de classe é compatilhado entre todos os objetos
#coloque a classe como o primeiro argumento

#para transformar em um metodo de classe, adicione @classmethod


class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit.printName()