#Escribir un programa que pregunte el nombre de un producto, su precio 
#y un número de unidades y muestre por pantalla una cadena con el nombre 
#del producto seguido de su precio unitario con 6 dígitos enteros y 2
#decimales, el número de unidades con tres dígitos y el coste total con
#8 dígitos enteros y 2 decimales.
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = float(precio * unidades)
print ("El producto {} vale {:9.2f}€ y quiero {:3d} unidades"
       "y el coste total es {:11.2f}€"
       .format(producto, precio, unidades, coste_total))
