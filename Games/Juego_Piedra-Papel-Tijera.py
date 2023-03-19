'''
Juego de piedra, papel o tijera......
'''
import random

options = ('piedra', 'papel', 'tijera')

machine_Wins = 0
user_Wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

### Eleccion Usurario
  user = input("piedra, papel o tijera ?  ")
  user = user.lower()
  if not user in options:
      print('Opcion no valida')
      continue
### Eleccion Maquina
  machine = random.choice(options)
  rounds += 1
  
  print('😁 = ', user)
  print('🤖 = ', machine)

  if user == machine:
    print("Empate")

  #Piedra
  elif user == 'piedra':
    if machine == 'papel':
      print(f"😁 : {user} VS 🤖 : {machine} => win MACHINE")
      machine_Wins += 1
      print('MACHINE: ', machine_Wins)
    else:
      print(f"😁 : {user} VS 🤖 : {machine} => win USER")
      user_Wins += 1
      print('USER: ', user_Wins)

  #Papel
  elif user == 'papel':
    if machine == 'tijera':
      print(f"😁 : {user} VS 🤖 : {machine} => win MACHINE")
      machine_Wins += 1
      print('MACHINE: ', machine_Wins)
    else:
      print(f"😁 : {user} VS 🤖 : {machine} => win USER")
      user_Wins += 1
      print('USER: ', user_Wins)

  #Tijera
  elif user == 'tijera':
    if machine == 'piedra':
      print(f"😁 : {user} VS 🤖 : {machine} => win MACHINE")
      machine_Wins += 1
      print('MACHINE: ', machine_Wins)
    else:
      print(f"😁 : {user} VS 🤖 : {machine} => win USER")
      user_Wins += 1
      print('USER: ', user_Wins)

  if machine_Wins == 2:
    print('*' * 10)
    print('¡¡¡ MACHINE WIN !!!')
    print('🤖 ', machine_Wins, '😁 ', user_Wins)
    break

  if user_Wins == 2:
    print('*' * 10)
    print('¡¡¡ USER WIN !!!')
    print('😁 ', user_Wins, '🤖 ', machine_Wins, )
    break