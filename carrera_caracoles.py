import os, time

def mostrar_menu():
    print("\t\t\t¡Bienvenido a Carrera de Caracoles!\n")
    print("******************************************************************************************")
    print("*                                                                                        *")
    print("*\t\t\t\tREGLAS DE JUEGO                                          *")
    print("*                                                                                        *")
    print("*\t-Juego para 2 jugadores                                                          *")
    print("*\t-Ganará el jugador que más pulsaciones de tecla consiga en el tiempo establecido *")
    print("*\t-Jugador 1: Tecla A  |  Jugador 2: Tecla L                                       *")
    print("*                                                                                        *")
    print("******************************************************************************************")

def pintame_circuito(posicion):
    print("🐌---------------------------------------------------------------------------------------🏁")
    
def jugar():
    mostrar_menu()
    print("Preparate para la carrera...\n\n\n")
    input("Pulsa Enter para continuar")
    os.system("clear")
    print("¡¡¡PREPARADO!!!")
    time.sleep(2)
    os.system("clear")
    print("¡¡¡LISTO!!!")
    time.sleep(2)
    os.system("clear")
    print("¡¡¡YA!!!")
    time.sleep(0.6)
    os.system("clear")
    pintame_circuito(posicion)
    

jugar()