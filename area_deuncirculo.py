''' un programa el cual nos permita conocer el área de un 
circulo dado su radio. El programa debe cumplir con los 
siguientes requerimientos.

El usuario debe ser capaz de ingresar (vía teclado) el radio del circulo.
El programa podrá calcular el área del circulo mediante el radio ingresado por el usuario.
El programa podrá aceptar un radio con o sin punto decimal.
El programa debe mostrar en consola, con el siguiente mensaje:
 El área del circulo es: x, el resultado de la operación.'''

from math import pi

r = float(input("Ingresa el radio del circulo: "))

print(f"El área del circulo es: {round(pi * r**2, 2)}")