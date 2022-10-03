#Para definir valores das variaveis usando metodos

class Friend:
    def __init__(self):
        self.job = "None"
        self.idade = "none"

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

Alicia = Friend()
Fred = Friend()

Alicia.setJob("Programador")
Fred.setJob("Agricultor")
Alicia.setIdade("19")
Fred.setIdade("32")
#idade
print(Alicia.idade)
print(Fred.idade)
#Profissão
print(Alicia.job)
print(Fred.job)