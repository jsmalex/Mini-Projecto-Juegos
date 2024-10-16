import os, random
lista_de_preguntas = (
    ("¿Cuál es el único mamífero que puede volar sin hacer escala en el aeropuerto?",
     {"a": "Un murciélago en plena fiesta", 
      "b": "Un pingüino con alas postizas", 
      "c": "Una ardilla que acaba de ver a Superman", 
      "d": "Un colibrí que se inscribió en un curso de vuelo"},
     "a"),
    
    ("¿Cuántos corazones tiene un pulpo en una primera cita?",
     {"a": "Uno y late de nervios", 
      "b": "Dos, por si uno se rompe", 
      "c": "Tres, porque así es de romántico", 
      "d": "Cuatro, para sobrevivir a sus ex"},
     "c"),
    
    ("¿Cuál es el animal más lento del mundo, ideal para el 'club de los que siempre llegan tarde'?",
     {"a": "Una tortuga con jet lag", 
      "b": "Un perezoso que ni se entera de la hora", 
      "c": "Un caracol en tacones", 
      "d": "Una estrella de mar que ni sabe que tiene patas"},
     "b"),
    
    ("¿Cuál es el único continente donde no se puede hacer un safari desértico?",
     {"a": "Asia, porque siempre está de fiesta", 
      "b": "Europa, donde lo más salvaje es un té en Londres", 
      "c": "Oceanía, con canguros haciendo senderismo", 
      "d": "América del Sur, donde hasta los desiertos son tropicales"},
     "b"),
    
    ("¿Qué animal tiene la mordida más fuerte, capaz de abrir hasta una lata de atún sin abrelatas?",
     {"a": "Un león después de la siesta", 
      "b": "Un tiburón cuando se queda sin dientes", 
      "c": "Un cocodrilo que confunde tu brazo con su almuerzo", 
      "d": "Un lobo con hambre de pizza"},
     "c"),
    
    ("¿Qué país consume tanto chocolate que podrías pensar que están en una dieta 'cacaoterapéutica'?",
     {"a": "Suiza, donde el chocolate es desayuno, almuerzo y cena", 
      "b": "Estados Unidos, donde los chocolates son del tamaño de coches", 
      "c": "Alemania, porque necesitan energía para bailar polka", 
      "d": "Bélgica, donde el chocolate es legalmente considerado un hobby"},
     "a"),
    
    ("¿Cuál es el planeta más caliente del sistema solar, como para freír huevos en la superficie?",
     {"a": "Venus, el sauna cósmico", 
      "b": "Mercurio, el horno solar", 
      "c": "Marte, el desierto sin SPF", 
      "d": "Júpiter, que se pone celoso porque tiene tormentas"},
     "a"),
    
    ("¿Qué insecto puede sobrevivir hasta una semana sin cabeza, como si fuera un truco de circo?",
     {"a": "Un mosquito que nunca sabe cuándo rendirse", 
      "b": "Una hormiga con ganas de vivir a lo loco", 
      "c": "Una cucaracha que piensa que es inmortal", 
      "d": "Una mosca que ha visto demasiadas películas de acción"},
     "c"),
    
    ("¿Qué fruta flota en el agua porque se cree más ligera que el aire?",
     {"a": "Una naranja con complejo de boya", 
      "b": "Una manzana que se toma muy en serio la dieta", 
      "c": "Una pera que se apuntó a clases de natación", 
      "d": "Un plátano con flotador incluido"},
     "a"),
    
    ("¿Cuántos años puede dormir un caracol cuando se siente 'cansadito'?",
     {"a": "Tres años, porque sueña a lo grande", 
      "b": "Uno, porque le gusta la siesta", 
      "c": "Cinco, por si acaso suena la alarma", 
      "d": "Diez, y luego necesita un café muy cargado"},
     "a")
)

puntos = 0
preguntas = 0
preguntas_que_han_salido = []

def mostrar_menu():
    print("\n\t\t\t¡Bienvenido a Mad Quiz!\n")
    print("******************************************************************************************")
    print("*                                                                                        *")
    print("*\t\t\t\tREGLAS DE JUEGO                                          *")
    print("*                                                                                        *")
    print("*\t-Juego para 1 jugador                                                            *")
    print("*\t-Contesta a las preguntas seleccionando una de sus cuatro respuestas posibles    *")
    print("*\t-Selecciona las respuestas pulsando a,b,c y d                                    *")
    print("*                                                                                        *")
    print("******************************************************************************************")
    input("\n\n\nPulsa Enter para continuar.")

def mostrar_pregunta(n_pregunta):
    os.system("clear")
    print(f"{preguntas + 1}º pregunta:\n")
    print(lista_de_preguntas[n_pregunta][0])
    print()
    print("\tA - " + lista_de_preguntas[n_pregunta][1]["a"] + "\t\tB - " + lista_de_preguntas[n_pregunta][1]["b"] + "\n\tC - " + lista_de_preguntas[n_pregunta][1]["c"] + "\t\tD - " + lista_de_preguntas[n_pregunta][1]["d"] + "\n")


def pregunta_aleatoria():
    global preguntas_que_han_salido
    while True:
        pregunta = random.randint(0, 9)
        if len(list(filter(lambda x : x == pregunta, preguntas_que_han_salido))) == 0:
            preguntas_que_han_salido.append(pregunta)
            return pregunta


def coger_respuesta():
    while True:
        respuesta = input("Indica una respuesta correcta:").lower()
        if respuesta == "a" or respuesta == "b" or respuesta == "c" or respuesta == "d":
            return respuesta
    

def comprobar_acierto(respuesta, n_pregunta):
    global puntos
    if respuesta == lista_de_preguntas[n_pregunta][2]:
        print("\n¡¡¡Felicidades!!! Has acertado!!! Ganas 10 puntos.")
        puntos += 10
    else:
        print(f"\nLo siento...la respuesta correcta es la {lista_de_preguntas[n_pregunta][2]}. Suerte con la siguiente.")

def jugar():
    global preguntas, puntos
    mostrar_menu()
    while True:
        numero_de_pregunta = pregunta_aleatoria()
        mostrar_pregunta(numero_de_pregunta)
        respuesta = coger_respuesta()
        comprobar_acierto(respuesta, numero_de_pregunta)
        input("\n\n\n\nPulsa Enter para continuar.")
        preguntas += 1
        if preguntas == 10:
            break
    print(f"\n\nTu puntuacion final es de {puntos} puntos.")


jugar()