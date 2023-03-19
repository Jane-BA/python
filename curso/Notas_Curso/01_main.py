#Comentario
print("Holis")

#Operaciones...
print(12 + 5)
"""
Varias lineas
de comentario
"""

''' Variabbles '''

my_name = "Nicolas"
print(my_name)

my_ege = input("Cual es tu edad? ")
print("Usando input...", my_ege)

is_single = True
print(type(is_single))

#Srings .....
name = "Jan"
last_name = "Bri"

#Format
template1 = "I'm " + name + ' ' + last_name

template2 = "Hi, mi nombre es {} y mi apellido es {}".format(name, last_name)

template3 = f"Holis, soy {name} {last_name} y mi edad es {my_ege}"

print(template1)
print(template2)
print(template3)

age = 25
print(age)
#Python no permite operador ++
age += 1
print(age)

#Conversion de tipos de datos
"""
str => name = str(name)
int => age = int(age)
bool => question = bool(question)
"""
