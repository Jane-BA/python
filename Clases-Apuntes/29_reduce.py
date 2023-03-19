import functools

num = [1, 2, 3, 4, 5, 6]

## Funcion REDUCE, se llama a si misma recordando el resusltado de los valores iterados
#COUNTER actua como el almacenador de los resultados
#counter + item = ...item
# 1+2 = 3+3 = 6+4 = 10
result = functools.reduce(lambda counter, item : counter + item, num)

print(result)

### Desglosando la funcion REDUCE ...
def accum(counter, item):
    print('counter >>', counter)
    print('item >>', item)
    return counter + item

r = functools.reduce (accum, num)
print(r)