## ...Basico... ##
def my_funcBasic():
    print('This is my func1')
    print('This is my func1')

my_funcBasic()

## ...Usando Parametros... ##
def my_funcParam(text):
    print(text * 2)

my_funcParam('Imprime 2 veces ')

## ...Usando Matematicas... ##
def my_funcMat(a, b):
    print(a + b)

my_funcMat(1, 5)

## ...Funcion dentro de otra Funcion ... ##
def suma(a, b):
    my_funcParam(a + b)

suma(1, 5)

print('...return...')

## ...Funcion con RETURN... ##
def my_return(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

resto = my_return(1, 10)
print(resto)

resto2 = my_return(resto, resto+15)
print(resto2)

## ...Funcion con valores por defecto ... ##
def my_defect(length=1, width=1, depth=1):
    return length * width * depth, length, 'hola' #Retorna multiples valores

result = my_defect(width=8)
r, w, t = my_defect(width=8)

print(result)
print(r)
print(w)
print(t)

## ...Funcion lambda ... ##
def increment(x):
    return x + 1

Fun_Lambda = lambda x : x+1

r1 = increment(10)
r2 = Fun_Lambda(20)

print(r1)
print(r2)
print('............')

## ...Funcion lambda ... ##
full_name = lambda name, last : f'Full name is {name.title()} {last.title()}'
text = full_name('nicolas', 'perez')
print(text)

####..-..-..-.. HOF ..-..-..-..####
## ...Higher Order Function ... ##
# funcion como parametro de otra funcion #
def inc(x):
    return x + 1        # 3 + 1 = 4

def hof(x, func):
    return x + func(x)  # 3 + 4 = 7

r3 = hof(3, inc)        # r3 = 7
print(r3)

####..-..-.. HOF con LAMBDA ..-..-..####
# funcion directamente en la funcion lambda #
y = lambda x : x + 2             # 3 + 2 = 5
z = lambda x, func : x + func(x) # 3 + 5 = 8

###Forma 1
r4 = z(3, y)
print(r4)

###Forma 2  -.-Eliminamos el uso del la funcion "y"-.-
r5 = z(3, lambda x : x + 2)
print(r5)

r6 = z(3, lambda x : x * 4) #-Es mas facil reutitizar el codigo-#
print(r6)
