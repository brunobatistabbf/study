import os
os.system("dir")

#Modulos ajudam a organizar o codigo
#Um modulo é um arquivo python que possui funções ou classes

#Existem muitos modulos (as vezes chamados de bibliotecas)
#Usados para codificar mais rapido

#São blocos de construção
#Eles contem grandes conjuntos de funções, que fornecem funcionalidades adicionais

#Importe um modulo com import

#Obter funções especificas de um modulo
#from module import  function

from time import  sleep
sleep(2)
print("Esperou dois segundos")

#importa as funções que você pode usar
#from time
#time.sleep(2)

#Para ver as funções em um modulo
#no console python
import os
dir(os)