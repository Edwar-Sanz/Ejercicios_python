#juego mastermind
import os
import random

os.system("cls")

print("*********************************************************")
print("*                                                       *")
print("*    INSTRUCCIONES:                                     *")
print("*    Escribe cuatro números que no se repitan, sigue    *")
print("*    las pistas hasta encontrar el número correcto.     *")
print("*    escribe- salir -para terminar el juego.            *")
print("*                                                       *")
print("*********************************************************")

input()
os.system("cls")


# Generando el numero aleatorio
caracteres = "1234567890"
numero = ""
while len(numero) < 4:
    i = random.choice(caracteres)
    if i not in numero:
        numero += i

numero = "1234"


# Empieza el juego
resultado = []

while True:


    #imprimiento el resultado
    os.system("cls")
    print("* Tu número", "* Números acertados", "* Posiciones acertadas")
    print("")
    espacio = " "
    for i in range(len((resultado))):
        print(f"* {espacio*2}{resultado[i][0]}{espacio*3} * {espacio*8}{resultado[i][1]}{espacio*8} * {espacio*9}{resultado[i][2]}{espacio*8} *")
        print("")



    
    # Validando la entrada
    jugando = True
    while True:   
        aux = ""
        repetidos = ""
        entrada = input("Escribe cuatro números que no se repitan    ")

        if entrada.capitalize() == "Salir":
            jugando = False
            break

        elif entrada.capitalize() != "Salir":
            if len(entrada) != 4:
                continue

            for i in entrada:
                if i not in aux:
                    aux += i
                elif i in aux:
                    repetidos += i
                if i not in caracteres:
                    repetidos += i            

            if len(repetidos) != 0:
                continue

            else:
                break
    if jugando == False:
        break
        

    # Comparando entrada y numero aleatorio
    numero_acertado = 0
    posicion_acertada = 0
    contador = 0
    for i in entrada:

        if i in numero:
            numero_acertado += 1

        if i == numero[contador]:
            posicion_acertada += 1

        contador += 1


    # se crea un lista con el resultado de la ronda
    ronda = [entrada, numero_acertado, posicion_acertada]

    #se guarda el resultado de la ronda en la lista de resultados
    resultado.append(ronda)


    if posicion_acertada == 4:
        print("Has ganado!")
        break