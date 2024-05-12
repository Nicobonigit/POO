from tkinter import *

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ahorcado")
        self.puntaje = 10
        self.palabra = "GATO" #Aquí se escribe la palagra a buscar
        self.letras_adivinadas = set()
        self.letras_incorrectas = set()

        self.crear_interfaz()

    def crear_interfaz(self):
        # Pantalla de puntos
        self.pantalla_puntos = Text(self.ventana, state="disabled", width=10, height=1, font=("Helvetica", 18))
        self.pantalla_puntos.grid(row=0, column=0, columnspan=2)
        self.actualizar_puntos()

        # Teclado
        teclado = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
        for fila in range(3):
            for columna in range(10):
                indice = fila * 10 + columna
                if indice < len(teclado):
                    boton = self.crear_boton(teclado[indice])
                    boton.grid(row=fila+1, column=columna)

        # Botón Reiniciar
        self.boton_reiniciar = Button(self.ventana, text="Reiniciar", command=self.reiniciar_juego)
        self.boton_reiniciar.grid(row=4, column=0, columnspan=2)

    def crear_boton(self, letra):
        return Button(self.ventana, text=letra, width=4, height=2, font=("Arial Black", 12),
                      command=lambda: self.click(letra))

    def click(self, letra):
        if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
            return
        if letra in self.palabra:
            self.letras_adivinadas.add(letra)
        else:
            self.letras_incorrectas.add(letra)
            self.puntaje -= 1
            if self.puntaje <= 0:
                self.mostrar_mensaje("¡PERDISTE!")
                self.deshabilitar_botones()
                return
        if self.palabra_completada():
            self.mostrar_mensaje("¡GANASTE!")
            self.deshabilitar_botones()
            return
        self.actualizar_puntos()

    def reiniciar_juego(self):
        self.puntaje = 10
        self.letras_adivinadas.clear()
        self.letras_incorrectas.clear()
        self.actualizar_puntos()
        self.habilitar_botones()
        for widget in self.ventana.winfo_children():
            if isinstance(widget, Label) and widget.cget("text") == "¡GANASTE!":
                widget.destroy()

    def actualizar_puntos(self):
        self.pantalla_puntos.config(state="normal")
        self.pantalla_puntos.delete(1.0, END)
        self.pantalla_puntos.insert(END, f"Puntos: {self.puntaje}")
        self.pantalla_puntos.config(state="disabled")

    def palabra_completada(self):
        return set(self.palabra) == self.letras_adivinadas

    def mostrar_mensaje(self, mensaje):
        mensaje_label = Label(self.ventana, text=mensaje, font=("Helvetica", 18))
        mensaje_label.grid(row=3, column=0, columnspan=2)

    def deshabilitar_botones(self):
        for widget in self.ventana.winfo_children():
            if isinstance(widget, Button) and widget != self.boton_reiniciar:
                widget.config(state="disabled")

    def habilitar_botones(self):
        for widget in self.ventana.winfo_children():
            if isinstance(widget, Button):
                widget.config(state="normal")

ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
