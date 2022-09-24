#time não faz parte da biblioteca padrão
import  time

#O modulo tempo tem todos os tipos de funções relacionados ao tempo

#Hora atual
timenow = time.localtime(time.time())
print(timenow)
print('\n')
#Convertendo para tempo humano
year, month, day, hour, minute = timenow[0:5]
print(timenow)
timenow = time.localtime(time.time())


#Programa funcionando
timee = time.localtime(time.time())
year, month, day, hour, minute = timee[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print("\n")
print(str(hour) + ":" + str(minute))

#imterromper a execução e esperar
print("Ola")
time.sleep(5)
print("Mundo")
time.sleep(1)

#Imprimindo a data no formato ano-mes-dia
exercicio =  time.localtime(time.time())
year, month, day = exercicio[0:3]

print(str(year) + "/" + str(month) + "/" + str(day))