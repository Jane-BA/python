person = {
    'name' : 'Nicolas',
    'last' : 'Molina',
    'langs' : ['Python', 'JS'],
    'age' : 87
}

#Imprimir un valor ....
print(person)
print(len(person))
print(person['age'])
print(person.get('unValor')) #Usando GET evitamos errores
print('langs' in person)

#Modificando y agregando values ....
person['name'] = 'Santy'
person['age'] -= 50
person['langs'].append('rust')
print(person)

#Borrando ....
del person['last']
person.pop('age')
print(person)

#Imprimiendo por partes ....
print('....items....')
print(person.items())

print('....keys....')
print(person.keys())

print('....values....')
print(person.values())
