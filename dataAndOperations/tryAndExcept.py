#Para lidar com exceções
#Para lidar adequadamente com problemas

#Para tratar exceções os try-catch é usado

#Todas as exceções em python herdam da classe BaseException

#try:
#    <faça algo>
#except Exception:
#    <Trate o erro> #esse codigo só executado se ocorrer uma exceção

try:
    1/0
except ZeroDivisionError:
    print("ERROR: Dividingo por Zero")

print("O programa continuou")


try:
    open("shootMe.py")
except:
    print("Arquivo não encontrado")

print("Arquivo ShootMe.py")

#Da para escrever varios tipos de except em um codigo
#try:
#your code here
#except FileNotFoundError:
#handle exception
#except IsADirectoryError:
#handle exception
#except:
#all other types of exceptions
#print('Should reach here')



try:
    x = input("Digite o número: ")
    x = x + 1
    print(x)
except:
    print("Entrada Invalida")

#ZeroDivisionError, NameError, TypeError e outros...


def fail():
    1 / 0
try:
    fail()
except:
    print('Exception occured')
print('Program continues')


#Finally sempre é executada no try
try:
    f = open("test.txt")
except:
    print('Could not open file')
finally:
    f.close()

print('Program continue')


#try else
try:
    x = 1
except:
    print('Failed to set x')
else:
    print('No exception occured')
finally:
    print('We always do this')

#Você pode forçar exceções com a palavra-chave raise

#Você pode criar o proprio exception para seu codigo
#Precisa cria uma classe que herda de Exception

class LunchError(Exception):
    pass

raise LunchError("Programmer went to lunch")

#É bom colocar exceções em arquivos separados erros.py

