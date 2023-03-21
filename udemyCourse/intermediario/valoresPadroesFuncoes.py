"""
Valores padrão para parametros
Refatorar: Editar Codigo
"""

def valorpadrao(x, z=None):
    if z is not None:
        print("Eita")
    else:
        print(f'{x + x}')

valorpadrao(10)