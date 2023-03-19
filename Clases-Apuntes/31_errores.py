### ASSERT: evalua si cumple con la condicion, si no, lanza un error
suma = lambda x, y : x + y
assert suma(2, 2) == 4

### RAISE: evalua si cumple con la condicion, si no,
# manda un error personalizado
'''age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')'''

### Probar errores sin que el programa se detanga
try:
    print(0/0)      #Prueba...
except ZeroDivisionError as error:
    print(error)    #Cacha el error y lo imprime en mensaje

try:
    assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)

print('Hola')
print('......')

try:
    print(0/0)      #Prueba todo este codigo...
    assert 1 != 1, 'Uno no es igual a uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')

except ZeroDivisionError as error:
    print(error)    #Cacha cualquiee tipo de error posible
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola 2')
