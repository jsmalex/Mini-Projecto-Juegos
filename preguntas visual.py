import tkinter as tk, random, os


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
ventana = tk.Tk()

def limpiar_ventana():
    for elemento in ventana.winfo_children():
        elemento.destroy()

    
def mostrar_bienvenida():
    texto_bienvenida = """
                                     ¡Bienvenido a Mad Quiz!

    ******************************************************************************************
    *                                                                                        *
    *                                   REGLAS DEL JUEGO                                     *
    *                                                                                        *
    *     -Juego para 1 jugador                                                              *
    *     -Contesta a las preguntas seleccionando una de sus cuatro respuestas posibles      *
    *     -Selecciona las respuestas pulsando a,b,c y d                                      *
    *     -Cada pregunta acertada suma 10 puntos                                             *
    *                                                                                        *
    ******************************************************************************************
    """
    etiqueta_menu = tk.Label(ventana, text=texto_bienvenida, font=("Courier", 10), justify="left")
    etiqueta_menu.pack(padx=10, pady=10)
    boton_comenzar = tk.Button(ventana, text="INICIO", command= mostrar_pregunta)
    boton_comenzar.pack(pady=10)


def verificar_respuesta(n_pregunta, respuesta, ventana, puntos):
    respuesta_correcta = lista_de_preguntas[n_pregunta][2]
    if respuesta == respuesta_correcta:
        puntos += 10
        texto_acierto = tk.Label(ventana, text="¡¡¡Felicidades!!! Has acertado!!! Ganas 10 puntos.", font=("Arial", 14))
        texto_acierto.pack(pady=10)
    else:
        texto_fallo = tk.Label(ventana, text=f"Lo siento...la respuesta correcta es la {respuesta_correcta}. Suerte con la siguiente.", font=("Arial", 14))
        texto_fallo.pack(pady=10)


def mostrar_pregunta():
    limpiar_ventana()
    
    # Título de la pregunta
    pregunta_texto = tk.Label(ventana, text=f"{preguntas + 1}º pregunta:", font=("Arial", 14))
    pregunta_texto.pack(pady=10)
    
    # Pregunta
    pregunta_label = tk.Label(ventana, text=lista_de_preguntas[n_pregunta][0], font=("Arial", 12), wraplength=600)
    pregunta_label.pack(pady=10)
    
    # Opciones de respuesta
    opciones = lista_de_preguntas[n_pregunta][1]
    
    # Botones para cada respuesta
    boton_a = tk.Button(ventana, text=f"A - {opciones['a']}", font=("Arial", 10), command=lambda: verificar_respuesta(n_pregunta, 'a', ventana, puntos))
    boton_a.pack(pady=5)
    
    boton_b = tk.Button(ventana, text=f"B - {opciones['b']}", font=("Arial", 10), command=lambda: verificar_respuesta(n_pregunta, 'b', ventana, puntos))
    boton_b.pack(pady=5)
    
    boton_c = tk.Button(ventana, text=f"C - {opciones['c']}", font=("Arial", 10), command=lambda: verificar_respuesta(n_pregunta, 'c', ventana, puntos))
    boton_c.pack(pady=5)
    
    boton_d = tk.Button(ventana, text=f"D - {opciones['d']}", font=("Arial", 10), command=lambda: verificar_respuesta(n_pregunta, 'd', ventana, puntos))
    boton_d.pack(pady=5)


def jugar():
    ventana.title("MAD QUIZ")
    ventana.geometry("800x600")
    mostrar_bienvenida()
    while True:
        numero_de_pregunta = pregunta_aleatoria(preguntas_que_han_salido)
        mostrar_pregunta(ventana, numero_de_pregunta, puntos)
        preguntas += 1
        if preguntas == 10:
            break

os.system("clear")
jugar()

ventana.mainloop()