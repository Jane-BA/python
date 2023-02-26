counter = 0

while counter < 20:
    counter += 1
    if counter == 9:
        break
    print(counter)

print('........')

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)