import tkinter as tk

ventana = tk.Tk()
ventana.title("mi ventana")
ventana.geometry("800x600")

def destruye_ventana():
    ventana.destroy()


def limpiar_ventana():
    for elemento in ventana.winfo_children():
        elemento.destroy()

def pagina2():
    text2 = "esta es mi pagina 2"
    etiqueta_menu2 = tk.Label(ventana, text=text2, font=("Courier", 10), justify="left")
    etiqueta_menu2.pack(padx=10, pady=10)


def pintame_inicio():
    texto_bienvenida = """
                                        ¡Bienvenido a Mad Quiz!

        ******************************************************************************************
        *                                                                                        *
        *                                    REGLAS DE JUEGO                                     *
        *                                                                                        *
        *     -Juego para 1 jugador                                                              *
        *     -Contesta a las preguntas seleccionando una de sus cuatro respuestas posibles      *
        *     -Selecciona las respuestas pulsando a,b,c y d                                      *
        *                                                                                        *
        ******************************************************************************************
        """
    etiqueta_menu = tk.Label(ventana, text=texto_bienvenida, font=("Courier", 10), justify="left")
    etiqueta_menu.pack(padx=10, pady=10)
    boton_comenzar = tk.Button(ventana, text="INICIO", command= destruye_ventana)
    boton_comenzar.pack(pady=10)
pintame_inicio()

pagina2()
ventana.mainloop()