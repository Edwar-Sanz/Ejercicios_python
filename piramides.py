
# -------------------------------------------------------------------------------------------------
# imprime un cuadrado de numeros

for i in range(0, 91, 10):
	for j in range(1, 11):
		print( " {} ".format(i+j), end="")
	print()




# -------------------------------------------------------------------------------------------------

#piramide invertida:


altura = int(input("escribe un número..."))
mas = "O "


for i in range(altura):
    print("  " * i + mas * (altura+(altura-1)))
    altura -= 1
    
# -------------------------------------------------------------------------------------------------

# piramide


altura = int(input("escribe un número..."))
espacio = ". "
mas = "o "
a = 1


for i in range(altura):
    print(espacio * altura + mas * (i+a))
    altura -= 1
    a +=1


# -------------------------------------------------------------------------
# imprimir rectangulo dando las medidas



base = int(input("base: "))

altura = int(input("altura: "))


total = base*altura

for i in range(0, total, base):
    
    for j in range(base):
        print("$  ", end="")
        
    print("")