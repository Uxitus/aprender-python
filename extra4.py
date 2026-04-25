numero_de_numeros= int(input("Cuantos numeros quieres sumar?"))
suma = 0


for n1 in range(1, numero_de_numeros + 1):
      numero= int(input("Número " + str(n1) +  ": "))
      suma = suma + numero
print ("La suma total es: " , suma)