#O método join recebe uma sequência como argumento. A sequência é escrita como argumento único: você precisa adicionar colchetes ao redor da sequência.
firstname = "Rodrigo"
lastname = "Coelho"

sequencia = (firstname , lastname)

name = " ".join(sequencia)
print(name)

palavras = ["guatemala", "Nigeria", "Butão"]
paises = '-'.join(palavras)
print(paises)