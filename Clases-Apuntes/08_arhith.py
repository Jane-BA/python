print(10 + 10) # 20
print(10 - 5) # 5
print(10 * 5) # 50
print(10 / 2) # 5.0
print(10 % 2) # 0 Residuo de la division

print(10 / 3) # 3.33333....
print(10 % 3) # 1
print(10 // 3) # 3 Division sin decimal

print(2**3) # 8 Exponente

print("..........")
"""Comparando num Flotantes"""
x = 3.3
y = 1.1 + 2.2
xy = (x == y)

print(f"x = {x}")
print(f"y = {y}")
print(f"x = y? {xy}")

print("Convesion Forzada con str...")
y_str = format(y, "2g") #Solo 2 decimales
print('str => ', y_str)
print(y_str == str(x))

print("Convesion Matematica...")
tolerance = 3.3
"""Valor absoluto impide negativos"""
print(abs(x - y))
print(abs(x - y) < tolerance)

print("La mejor manera de hacerlo...")
print(x == round(y, 1)) #Redondea el valor

print(1992 % 4)
print(1800 % 4)

print(1992 % 100)
print(1800 % 100)

print(1992 % 400)
print(1800 % 400)