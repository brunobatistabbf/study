#ler arquivo
#leitura de arquivos fazem parte da biblioteca padrão do python

#duas maneiras de ler um arquivo:
#linha por linha
nome = "readArchieve.py"

with open(nome) as f:
    content = f.readlines()

print(content)
#ler bloco

arquivo = "readArchieve.py"

infile = open(arquivo, 'r')
data = infile.read()
infile.close()

print(data)

