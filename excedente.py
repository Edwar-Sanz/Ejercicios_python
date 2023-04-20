"""
H hormigas recogen A granos de azúcar y deciden dividir en partes iguales todo 
lo recolectado. Calcule cuántos granos de azúcar quedaron al finalizar la 
repartición si cada una tomó la misma cantidad.

Detalles:
Tanto H como A son positivos y no sobrepasan el valor de los 50000.
"""
h = int(input("H: "))
a = int(input("A: "))

print(f"Excedente {a%h}")