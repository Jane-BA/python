'''SET no permite duplicidades'''

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_types = {1, 'hola', False, 12.12}
print(set_types)

#"SET" colocarlo para convertira a conjunto los valores deseados
set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

#Lista a Set
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

#Set a lista
unique_numbers = list(set_numbers)
print(unique_numbers)

#Comandos para manipular set ....
print('.......')

size = len(set_countries)
print(size)

#Buscar
print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)

### Recuerda los valores y no permite duplicados ###
# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

### Remover, causa error si no encuantra la palabra ###
# remove
set_countries.remove('col')
print(set_countries)

# descarta
set_countries.discard('arg')
print(set_countries)

set_countries.discard('ar')
print(set_countries)

### Usar clear con cuidado, ya que lo borra todo
# clear
set_countries.clear()
print(set_countries)
print(len(set_countries))