"""
Um iteravel dentro do outro
"""

salas = [
    ["Bruno Fagner", "Bruno Batista"],
    ["Carlos Eduardo", "Carlos Rodrigues"],
    ["Guilherme Dutra", "Guilherme Richard", "Carlos Alberto de Nobrega", (1 , 2, 3, 4, 5)],

]

print(salas[1][0])
print(salas[0][1])
print(salas[2][3][3])

for sala in salas:
    print(sala)

