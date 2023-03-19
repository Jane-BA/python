### Preguntar por el sistema operativo donde se ejecuta este codigo
print('... sys ...')
import sys
print(sys.path)

### EXPRESIONES REGULADAS
#busca e imprime solo el dato buscado dentro de un texto
print('... re ...')
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

### TIEMPO
#formato de computadora (sistema UNIX)
print('... time ...')
import time
timestamp = time.time()
print(timestamp)

#pregunta por la hora local, luego lo convierte con el sist ASCII
local = time.localtime()
print(local)
result = time.asctime(local)
print(result)

### MANEJO DE LISTAS
#cuenta la frecuencia de cada numero y retorna el resultado en un diccionario
print('... collections ...')
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)