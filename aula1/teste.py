cont = 0
while cont < 10:
    if cont % 2 != 0:
        cont += 1
        continue
    print(cont)
    cont += 1