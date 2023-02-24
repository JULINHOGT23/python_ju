# Creamos una lista de números
numeros = [10, 15, 14, 8, 32, 20, 25, 30, 35, 40]

# Iteramos sobre cada número en la lista
for numero in numeros:
    # Si el número es divisible por 5 (su módulo es 0), lo imprimimos
    if numero % 5 == 0:
        print(numero)
