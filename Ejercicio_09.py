#Escribir un programa que pregunte al usuario la fecha de su nacimiento en 
#formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar
#el programa anterior para que también funcione cuando el día o el mes se 
#introduzcan con un solo carácter.
print("Según este formato de fecha dd/mm/aaaa")
fecha_nacimiento = input("Introduzca su fecha de nacimiento: ")
separar = fecha_nacimiento.split("/") 
dia = separar[0]
mes = separar[1]
año = separar[2]
print(f"el dia es {dia}, el mes es {mes} y el año es {año}")
