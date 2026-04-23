edad =  int(input("Cuantos años tienes?"))

if edad >= 18:
    print("Vaya ya eres mayor de edad, felicidades!")
else:
    print("Auh, aun eres menor de edad, chiquitin!")
    
#2

temperatura = int(input("Hola, sabes a que temperatura estamos?"))

if temperatura <= 0 : 
    print("Vaya, es verdad, hace frio!")
elif temperatura <= 15:
    print("Es verdad, hace un poco de fresco!")
elif temperatura <= 25:
    print("Tienes toda la razon, es agradable el clima")
else:
    print("Hace calor eeh")
    
#3

edad_3= int(input("Hola, cuantos años tines?"))
credencia= input("Tienes INE?") .lower()

if edad_3 >= 18 and credencia == "si"or credencia == "Si":
    print("Vaya, vaya, tienes la edad y tienes INE, asi que pasa, bienvenido/a")
elif edad_3 >= 18 and credencia == "no" or credencia == "No":
    print("Vaya eres mayor, pero no tienes INE, sorry, no pasas")
else:
    print("Aja, con que no tienes ni la edad eeh, vayase a ver si ya puso la marrana, mejor")
    