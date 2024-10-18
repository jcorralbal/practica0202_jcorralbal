#Escribir un programa que pregunte el nombre del usuario en la consola y
#después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
#tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas
#y <n> es el número de letras que tienen el nombre.
nom_usuario = input("Introduza su nombre de usuario: ")
mayus_nom_usuario = nom_usuario.upper()
num_letras_nom = len(nom_usuario)
print(f"{mayus_nom_usuario} tiene {num_letras_nom} letras ")
