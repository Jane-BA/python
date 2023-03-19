n = int(input())

if n >= 1 and n <= 150:
    aux = ''
    for x in range(1, n):
        aux.append(x)

print(aux)