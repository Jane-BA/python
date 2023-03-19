set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Todos los mentos de ambos conjuntos sin repetir duplicados
### col, mex, bol, pe ###
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Solo muestra los elem duplicados al momento de intersectarse
### bol ###
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Muestra los elementos diferentes a los del otro conjunto
### col, mex ###
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#Muestra los elementos diferentes en cada conjunto,
#excluyendo los elem repetidos
### col, mex, pe ###
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)