import os, time, keyboard

longitud_pista = 100
posicion_jugador_1 = 0
posicion_jugador_2 = 0
meta = longitud_pista



def mostrar_menu():
    print("\n\t\t\t¡Bienvenido a Carrera de Caracoles!\n")
    print("******************************************************************************************")
    print("*                                                                                        *")
    print("*\t\t\t\tREGLAS DE JUEGO                                          *")
    print("*                                                                                        *")
    print("*\t-Juego para 2 jugadores                                                          *")
    print("*\t-Ganará el caracol que más pulsaciones de tecla consiga y llegue a la meta       *")
    print("*\t-Jugador 1: Tecla A  |  Jugador 2: Tecla L                                       *")
    print("*                                                                                        *")
    print("******************************************************************************************")


def pintame_circuito():
    pista_1 = ['-' for _ in range(longitud_pista)]
    pista_2 = ['-' for _ in range(longitud_pista)]
    pista_1[longitud_pista - 1]= "🏁"
    pista_2[longitud_pista - 1]= "🏁"
    pista_1[posicion_jugador_1] = '🐌'  # Representa el caracol del jugador 1
    pista_2[posicion_jugador_2] = '🐌'  # Representa el caracol del jugador 2
    print("Jugador 1 (A): " + ''.join(pista_1))
    print("Jugador 2 (L): " + ''.join(pista_2))
    print("\n\n")
    

def arrranque_inicial():
    print("Preparate para la carrera...\n\n\n")
    input("Pulsa Enter para continuar")
    os.system("clear")
    print("\t\t\t\t\t\t\t¡¡¡PREPARADO!!!\n")
    print("\t\t\t\t\t\t\t      🔴🔴\n\n\n\n\n\n\n")
    pintame_circuito()
    time.sleep(2)
    os.system("clear")
    print("\t\t\t\t\t\t\t  ¡¡¡LISTO!!!\n")
    print("\t\t\t\t\t\t\t      🔴⚪\n\n\n\n\n\n\n")
    pintame_circuito()
    time.sleep(2)
    os.system("clear")
    print("\t\t\t\t\t\t\t    ¡¡¡YA!!!\n")
    print("\t\t\t\t\t\t\t      🟢🟢\n\n\n\n\n\n\n")
    pintame_circuito()
    time.sleep(0.5)
    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n")
    pintame_circuito()


def hay_ganador():
    if posicion_jugador_1 >= meta:
        print("\t\t\t\t\t\t\t¡Jugador 1 gana!\n\n\n")
        return True
    elif posicion_jugador_2 >= meta:
        print("\t\t\t\t\t\t\t¡Jugador 2 gana!\n\n\n")
        return True
    return False


def jugar():
    global posicion_jugador_1, posicion_jugador_2

    mostrar_menu()
    arrranque_inicial()

    while True:
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n")
        pintame_circuito()

        if keyboard.is_pressed("a"):
            posicion_jugador_1 += 1
        
        if keyboard.is_pressed("l"):
            posicion_jugador_2 += 1

        if hay_ganador():
            break

        time.sleep(0.05)
        
    input("Pulsa Enter para terminar\n\n")


jugar()