# generamos la lista
números = [2, 5, 8, 10, 12, 15, 18, 20, 35, 48]

# interamos sobre cada número en la lista
for número in números:
    # si el número es divisible por 5, su residuo es 0
    if número % 5 == 0:
        print(número)
