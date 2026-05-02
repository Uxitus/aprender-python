numero = int(input("Ingrese un número el cual quieres ver su tabla de multiplicar del 1 al 10: "))

print ("Su tabla de multiplicar es la siguiente... ")

for multiplo in range(1,11):
    resultado = numero * multiplo
    print(numero, "x", multiplo, "=", resultado)
    