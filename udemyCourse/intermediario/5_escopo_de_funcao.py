x = 3
def escopo():
    global x
    t = 10

    def outra_funcao():
        y = 20
        print(x, t, y)
        print(x + y)

    outra_funcao()

escopo()
print(x)