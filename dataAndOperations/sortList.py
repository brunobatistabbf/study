#Classificar uma lista é muito fácil: o Python possui
#suporte embutido para classificar listas.

x = [ 3 , 6 , 21 , 1 , 5 , 98 , 4 , 23 , 1 , 6 ]
x.sort()
print(x)

#uma lista de strings tambem pode sre classificadas
words = [ "Ser" , "Carro" , "Sempre" , "Porta" , "Comer" ]
words.sort()
print(words)

#classificar em ordem reversa
x = [ 3 , 6 , 21 , 1 , 5 , 98 , 4 , 23 , 1 , 6 ]
x.sort()
x = list(reversed(x))
print(x)

#classificar de uma maneira mais elegante
words = words[:: -1]
