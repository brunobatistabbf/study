#Descubra se uma String contém outra String

s = "porta fechada"
index =  s.find("fechada")
print(index)

#outro meio é usando o _in_
x =  "por que o leitão se esconde do leão"

if "leitão" in x :
    print("Ajude o leitão")

if "Leão" in x:
    print("Reconhece Maiuscula")
else :
    print("Não reconhece maiuscula")

frase = input()
if "Silva" or "silva" in frase:
    print("Familia Silva")
else:
    print("Não é da Familia Silva")

