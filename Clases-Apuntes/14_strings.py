text = 'Ella sabe Python'
'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''
print("Ella" in text)  #True

size = len(text)
print(size)

print(text)
print(text.upper())  #Mayus
print(text.lower())  #Minus
print(text.count('a'))  #Num de 'a'

print(text.swapcase())  #Mayus a minus y viceversa
print(text.startswith('Ella'))  #True/False
print(text.endswith('Rust'))  #True/False
print(text.replace('Python', 'Go'))  #Reemplaza una palabra por otra

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())  #Primera letra en mayus
print(text_2.title())  #Primera letra de c/palabra en mayus
print(text_2.isdigit())  #Es dijito ? True/False
print("398".isdigit())
'''
Indexing......
'''
print(text[0])  #E
print(text[size - 1])  #n
print(text[-1])  #n
'''
Slicing......
'''
print(text[:5])  #Ella
print(text[10:])  #Python
print(text[10:16:2])  #Pto
'''
.extend(lista) permite extender una lista agregándole los elementos de otra lista

.sort() ordena la lista de manera ascendente o descendente
'''

numbers = [1, 2, 3, 4]
tasks = ["t1", "t2", "t3"]

numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, "Hola")
print(numbers)

new_List = numbers + tasks
print(new_List)

'''
---- Tuplas ----
Estructura de datos inmutables que contiene
una secuencia ordenada de elementos
numbers(1, 2, 3)

Es inmutable y por lo tanto no puede ser
modificada, lo que permite proteger mejor
la data si no queremos que se modifique por error

my_list = list(numbers)
*Convertirlo de tupla a lista

my_tuple = tuple(my list)
*Convertirlo de lista a tupla

Esto con el fin de no modificar la lista a
una tupla
'''