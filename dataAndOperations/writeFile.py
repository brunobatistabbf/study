#write archieve in python
#a funcionalidade de gravação de arquivo faz parte do modulo padrão

#gravar e anexar são coisas diferentes

#voce pode abrir um arquivo para escrita usando a linha
#f  = open("teste.txt", "w")
#para anexar a um arquivo use:
#f = open("teste.txt", "a")

# create and open file
f = open("test.txt","w")

# write data to file
f.write("Hello World, \n")
f.write("This data will be written to the file.")

# close file
f.close()


x = open("acalme.txt", "w")
x.write("Acalme-se")
x.close()