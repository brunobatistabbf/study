# Exercios com função
def multiplica(*args):
    multiplica = args[0]
    for numero in args:
        multiplica = multiplica * numero
    print(multiplica)

multiplica(1, 2, 3)

def par_ou_impar(*args):
    i = 0
    while i < len(args):
        if args[i] % 2 == 0:
            print(f"Numero {args[i]} é Par")
        else:
            print(f"Numero {args[i]} é Impar")
        i = i + 1


par_ou_impar(1, 2, 3)