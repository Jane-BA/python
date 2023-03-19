'''
[expresion----for elem--in iterable------if condition
i * 2 ........for i.....in range(1, 101) if i % 2 == 0

n ............for n.....in cadena []
n ** 2 .......for n.....in range (1, 10)
(n*2) % 3.....for n.....in lista
'''
### SIMPLE ###
#Forma tradicional...
num = []
for element in range(1, 11):
    num.append(element)
print(num)

#List Comprehension...
numbers = [x for x in range(1, 11)]
print(numbers)

### AGREGANDO IF ###
#Forma tradicional...
a = []
for element in range(1, 11):
    if element % 2 == 0:
        a.append(element * 2)
print(a)

#List Comprehension...
b = [x * 2 for x in range(1, 11) if x % 2 == 0]
print(b)

### EN DICCIONARIOS CON NUMEROS ###
#Forma tradicional...
dic = {}
for i in range(1, 5):
    dic[i] = i * 2
print(dic)

#List Comprehension...
diccionario = {j: j * 2 for j in range(1, 5)}
print(diccionario)

### EN DICCIONARIOS CON STRINGS ###
#Forma tradicional...
import ctypes
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
print(population)

#List Comprehension...
pop = {country: random.randint(1, 100) for country in countries}
print(pop)

### CREANDO DICCIONARIO A PARTIR DE 2 LISTAS ###
name = ['nico', 'zule', 'santi']
age = [12, 56, 98]

#Usando la funcion ZIP para entrelazar listas
print (list(zip(name, age)))

#List Comprehension...
dictionary = {n: a for (n, a) in zip(name, age)}
print(dictionary)

### CREANDO DICCIONARIO A PARTIR DE 2 LISTAS con condicional###
unionCountyPopulation = {co: po for(co, po) in pop.items() if po > 30}
print(unionCountyPopulation)

text = 'Hola, soy Nicolas'
unique = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique)
