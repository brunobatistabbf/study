#iterable é um objeto python que pode ser usado como uma sequencia
#você pode ir para o proximo item da sequencia usando o metodo next()

#é um objeto container = só pode retornar um elemento por vez

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
print(iterable)

for item in iterable:
    print(item)

x = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterabl = x.keys()
iterator = iter(iterabl)
print( next(iterator) )
print( next(iterator) )

items = [ "one","two","three","four" ]
iterator = iter(items)
x = next(iterator)
print("\n")
print(x)