### .-.-.-.-. MAP .-.-.-.-. ###
numbers1 = [1, 2, 3, 4]
print(numbers1)

# 1° transformacion
trans_1 = []
for i in numbers1:
    trans_1.append(i * 2)
print(trans_1)

# 2° transformacion
trans_2 = list(map(lambda i : i * 2, numbers1))
print(trans_2)

#-Se necesita transformar a lista ya que que queda como mapa-#
#-MAP ejecuta HOF con lambda e iterando los elem de un arreglo-#

print('...')
print(numbers1)
numbers2 = [5, 6, 7]
print(numbers2)

r1 = list(map(lambda x, y : x + y, numbers1, numbers2))
print(r1)

### .-. MAP con DICCIONARIOS .-. ###
items = [
    {'product': 'camisa',
    'price': 100},

    {'product': 'pantalones',
    'price': 300},
    
    {'product': 'sueter',
    'price': 250}
]
## itera sobre items mostrando el contenido de 'price'
prices = list(map(lambda item : item['price'], items))
print(prices)

## añade un nuevo key llamado 'taxes' y le agrega un valor
def add_taxes(item):
    aux = item.copy()
    aux['taxes'] = aux['price'] * .19
    return aux

## con map itera items dentro de la funcion 'add_taxes' para generar los nuevos valores
new_items = list(map(add_taxes, items))

print('New list')
print(new_items)
print('Old list')
print(items)
