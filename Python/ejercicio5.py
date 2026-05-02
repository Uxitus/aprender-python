estudiantes_ = []

numero = int(input("Cuantos estudiantes ingresara? "))

for i in range( numero ):
    nombre = input("Cual es su nombre? ")
    calificacion = int(input("Cual es su calificacion? "))
    estudiantes_.append ({"nombre": nombre, "calificacion": calificacion})
    
for estudiante in estudiantes_:
    print(estudiante["nombre"], "tiene un promedio de: ", estudiante["calificacion"])
    
suma = 0
for estudiante in estudiantes_:
    suma = suma + estudiante["calificacion"]
    
promedio = suma / numero
print( "este es el promedio del grupo", promedio)