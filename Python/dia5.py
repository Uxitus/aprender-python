nombres = ["Uxis", "Ana", "Carlos", "María"]

print (nombres)
print(nombres[0])
print(nombres[2])
print("Total: ", len (nombres))

nombres.append("Luis")
print (nombres)

nombres.remove("Ana")
print(nombres)

calificaciones = [85, 92, 78, 96, 61, 74]
for cal in calificaciones:
    if cal >= 70:
        print ( cal, " - Aprobadas")
    else:
        print ( cal, " - Reprobado")

        
persona1 = {
    "nombre": "Uxis",
    "edad": 18,
    "Carrera": "Mecatronica"
    }

print(persona1["nombre"])
print(persona1["edad"])
persona1["promedio"] = 8.64
print(persona1)

estudiantes = [
    {"Nombre": "uxis", "promedio": 8.64},
    {"Nombre": "Ana", "promedio": 9.1},
    {"Nombre": "Carlos", "promedio": 7.3}
]
for estudiante in estudiantes:
    print(estudiante["Nombre"], "tiene un promedio de: ", estudiante["promedio"])