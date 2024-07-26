"""
Operação ternaria condicional em uma linha
<valor > if <condicao> else <outro valor>
"""
import dataclasses

condicao = 10 == 11
variavel = 'valor' if condicao else 'outro valor'
print(variavel)



