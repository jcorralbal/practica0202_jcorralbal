#Escribir un programa que pregunte el nombre del usuario en la consola y un 
#número entero e imprima por pantalla en líneas distintas el nombre del
#usuario tantas veces como el número introducido.
nom_usuario = input("Introduza su nombre de usuario: ")
num_entero = int(input("Introduza un número entero: "))
print((nom_usuario + "\n" ) * num_entero)

