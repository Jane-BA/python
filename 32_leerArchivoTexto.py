'''
#Abrir el archivo...
file = open('./historia.txt')

#Leer todo el .txt
print(file.read())
print('....')

#Leer linea x linea
print(file.readline())

#Leer linea x linea de forma automatica...
for line in file:
    print(line)

#Cerrar el archivo
file.close()'''

#forma mas comun de ejecutar y cerrar
# el .txt de forma automatica
with open('./historia.txt', 'r+') as file:
    file.write('\n nueva linea')
    file.write('\n otra nueva linea')
    file.write('\n una linea mas')

    for line in file:
        print(line)

'''
PERMISOS...
'R' agrega al texto
r  => solo lectura
r+ => lectura y escritura

'W' sobreescribe el texto
w  => solo escritura
w+ => escritura y lectura
'''