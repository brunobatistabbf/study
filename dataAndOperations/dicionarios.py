#dicionarios em python são um tipo de coleção
#comtem uma lista de itens, cada item tem uma chave e valor

#dicionario é uma mapeamento 1 para 1

palavras = {}

#palavras[chaves] = valor

words = {}
words["BMP"] = "BITMAP"
words["BTW"] = "A Proposito"
words["BRB"] = "Volto Já"

print(words["BMP"])
print(words["BRB"])

#Faça um mapeamento de países para codigos de paises
paises = {}
paises["BRA"] = "Brasil"
paises["EUA"] = "Estados Unidos"
paises["RUS"] = "Russia"

print("Paises em guerra: " + paises["RUS"])
