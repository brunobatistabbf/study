#criar um loop dentro de um loop
#passam por um ou mais loops

#normalmente aninham 2 ou 3 niveis de profundidade

pessoas = ["joao", "Carlos", "Mariza", "Larissa"]
restauranete = ["Japones",  "Americano", "Holandes", "Frances"]

for p in pessoas:
    for restaurante in  restauranete:
        print(p + " come um " + restaurante)