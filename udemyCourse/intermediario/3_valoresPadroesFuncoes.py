"""
Valores padrão para parametros
Refatorar: Editar Codigo
"""

def valorpadrao(x, z=None):
    if z is not None:
        print("Chocado!")
    else:
        print(f'{x + x}')

valorpadrao(10)