#varivel global pode ser usada ou nao no codigo
#varivel local só pode ser conhecida em uma área

def algo():
    localVar = 1
    print(localVar)

saldo = 0

def addAmount (x):
    global  balance
    balance = balance + x

addAmount(5)
print(balance)

