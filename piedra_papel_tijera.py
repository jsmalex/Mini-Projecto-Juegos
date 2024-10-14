import random
import os

def pinto_menu():
    print("\n\t\t\t--Bienvenido al juego piedra, papel y tijera--")
    print("\n\t********************************************************************************\n\t*                                                                              *\n\t*\t\t\t\tREGLAS DEL JUEGO                               *\n\t*                                                                              *\n\t*\t-Introduce tu eleccion entre las palabras piedra, papel o tijera.      *\n\t*\t-Te enfrentaras a la computadora y ganara el mejor de 3 rondas.        *\n\t*\t-¡¡Suerte y dale todo maquina!!                                        *\n\t*                                                                              *\n\t********************************************************************************\n")


def pido_dato():
    while True:
        eleccion_usuario = input("Introduce piedra, papel o tijera: ").lower()
        if eleccion_usuario != "piedra" and eleccion_usuario != "papel" and eleccion_usuario != "tijera":
            print(f'La palabra "{eleccion_usuario}" no es una opcion valida.')
        else:
            return eleccion_usuario


def eleccion_IA():
    numero_aleatorio = random.randint(1, 3)
    if numero_aleatorio == 1:
        eleccion_de_la_maquina = "piedra"
    elif numero_aleatorio == 2:
        eleccion_de_la_maquina = "papel"
    elif numero_aleatorio == 3:
        eleccion_de_la_maquina = "tijera"
    return eleccion_de_la_maquina

def pinta_marcador():
    global puntos_usuario, puntos_maquina
    print("****************************")
    print("*    JUGADOR    *    IA    *")
    print("****************************")
    print(f"*       {puntos_usuario}      *      {puntos_maquina}    *")
    print("****************************")


def comparar_resultado(eleccion_usuario, eleccion_de_la_maquina):
    global puntos_usuario, puntos_maquina
    if eleccion_usuario == eleccion_de_la_maquina:
        pinta_marcador()
        print(f"Empate!!! {eleccion_usuario} vs {eleccion_de_la_maquina}. Las cosa esta muy malita\n")
    elif (eleccion_usuario == "piedra" and eleccion_de_la_maquina == "tijera") or (eleccion_usuario == "tijera" and eleccion_de_la_maquina == "papel") or (eleccion_usuario =="papel" and eleccion_de_la_maquina == "piedra"):
        puntos_usuario += 1
        pinta_marcador()
        print(f"Has ganado el duelo {eleccion_usuario} vs {eleccion_de_la_maquina}. Llevas {puntos_usuario} partidas ganadas.Estas que te sales\n")
    elif (eleccion_de_la_maquina == "piedra" and eleccion_usuario == "tijera") or (eleccion_de_la_maquina == "tijera" and eleccion_usuario == "papel") or (eleccion_de_la_maquina =="papel" and eleccion_usuario == "piedra"):
        puntos_maquina += 1
        pinta_marcador()
        print(f"Pierdes el duelo {eleccion_usuario} vs {eleccion_de_la_maquina}. Llevas {puntos_usuario} partidas ganadas. Cuidadin con Terminator.\n")

def jugar():
    eleccion_usuario = pido_dato()
    os.system('clear')
    eleccion_de_la_maquina = eleccion_IA()
    comparar_resultado(eleccion_usuario, eleccion_de_la_maquina)


puntos_usuario = 0
puntos_maquina = 0
pinto_menu()
while (puntos_usuario < 3) and (puntos_maquina < 3):
    jugar()

if puntos_usuario == 3:
    print("Felicidades has ganado 🥳")
elif puntos_maquina ==3:
    print("Gano la IA. Suerte la proxima partida 🥳")