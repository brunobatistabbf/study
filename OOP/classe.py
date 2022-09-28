#Objetos são sempre criados a partir de uma classe
class dog:
    name = ""
    age = 0

    def bark(self):
        print("AU AU AU")

chuto = dog()
chuto.bark()

#A palavra self refere-se ao objeto(você pode criar varios objetos de uma classe)

#CLASS --> Obj1
#      --> Obj2

# O metodo __init__ será chamado.
# Este é sempre o primeiro metodo que é chamado ao criar
# um novo objeto, O metodo é chamado de construtor

class Website:
    def __init__(self, title):
        self.title = title

    def location(self):
        print("Localizado em São Paulo, SP")

    def ShowTitle(self):
        print(self.title)

obj = Website('pythonbasics.org')
obj.ShowTitle()

obj2 = Website("youtube.com.br")
obj2.ShowTitle()
obj2.location()

