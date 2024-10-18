#Escribir un programa que pregunte por consola el precio de un producto en
#euros con dos decimales y muestre por pantalla el número de euros y el 
#número de céntimos del precio introducido.
precio_producto = input("Introduzca el precio del producto en € con dos decimales: ")
separar = precio_producto.split(".")
euros = separar[0]
centimos = separar[1]
print(f"el precio tiene {euros} euros y {centimos} céntimos")
