#Escribir un programa que pregunte el correo electrónico del usuario 
#en la consola y muestre por pantalla otro correo electrónico con el 
#mismo nombre (la parte delantera de la arroba @) pero con dominio ceu.es.
correo_elec = input("Introduzca su correo electrónico: ")
correo_nuevo = correo_elec.split("@")[0]
print(correo_nuevo + "@ceu.es")
