#Recorrer en un rango
for element in range(1, 6):
    print(element)

print('....')

#Recorrer una lista
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

#Recorrer una tupla
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)

#Recorrer un diccionario
product = {
    'name' : 'camisa',
    'price' : 100,
    'stock' : 89
}
for key in product:
    print(key, ' > ', product[key])

for key, value in product.items():
    print(key, ' > ', value)

#Recorrer una lista de diccionarios
people = [
    {'name': 'nico',
     'age': 4},
    {'name': 'zule',
     'age': 4},
    {'name': 'santi',
     'age': 4}
]
for person in people:
    print('name > ', person['name'])

### Iterar de manera manual con NEXT
#For itera de manera automatica#
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))