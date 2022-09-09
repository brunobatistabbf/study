#uma string pode ser dividida em substring usando o metodo split

#Dada uma frase, a string pode ser dividida em palavras. Se você tiver um parágrafo,
#poderá dividir por frase. Se você tiver uma palavra, poderá dividi-la em caracteres
#ndividuais.

s = "divide em caracteres"
palavras = s.split()
print(palavras)
print(len(palavras)) #numero de palavras
print(len(s))#numero de caracteres

#dividir uma palavra em caracteres
x = "onibus"
lista = list(x)
print(lista)
#saida : ['o', 'n', 'i', 'b', 'u', 's']
