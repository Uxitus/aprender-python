#1

for vuelta in range(1,7):
    print("Vuelta numero, ", vuelta)
    
#2

contador = 0
while contador < 10:
    print("contador: ", contador)
    contador = contador + 1

print("Terminé")

#3

for i in range(10):
    if i == 5:
        break

    print(i)
    
for i in range(10):
    if i == 5:
        continue

    print(i)
   
#4

nombres = ["Uxis", "Romi", "Fer", "Cami", "Libny", "Pablin", "Joaquin"]
for nombre in nombres:
    print("Hola, ", nombre)