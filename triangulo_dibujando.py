import turtle

class Triangulo:
    def __init__(self):
        self.ladoA = int(input("Ingrese el tamaño del lado A: "))
        self.ladoB = int(input("Ingrese el tamaño del lado B: "))
        self.ladoC = int(input("Ingrese el tamaño del lado C: "))

    def mostrar(self):
        print("El lado A es:", self.ladoA)
        print("El lado B es:", self.ladoB)
        print("El lado C es:", self.ladoC)

    def mayor(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print("El lado A es el mayor")
        elif self.ladoA == self.ladoB and self.ladoB == self.ladoC:
            print("Todos los lados son iguales")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print("El lado B es el mayor")
        else:
            print("El lado C es el mayor")

    def tipo(self):
        if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
            print("El triángulo es equilátero")
        elif self.ladoA != self.ladoB and self.ladoB != self.ladoC and self.ladoA != self.ladoC:
            print("El triángulo es escaleno")
        else:
            print("El triángulo es isósceles")

    def dibujar(self):
        # Inicializar la pantalla
        screen = turtle.Screen()
        screen.title("Dibujo del Triángulo")
        screen.setup(width=600, height=600)

        # Inicializar la pluma
        pen = turtle.Turtle()
        pen.speed(1)  # Velocidad de dibujo

        # Dibujar el triángulo
        pen.penup()
        pen.goto(-self.ladoA / 2, 0)  # Mover a la posición inicial
        pen.pendown()
        pen.forward(self.ladoA)  # Dibujar el lado A
        pen.left(120)  # Girar 120 grados a la izquierda
        pen.forward(self.ladoB)  # Dibujar el lado B
        pen.left(120)  # Girar 120 grados a la izquierda
        pen.forward(self.ladoC)  # Dibujar el lado C

        # Mantener la ventana abierta
        screen.mainloop()

triangulo = Triangulo()
triangulo.mostrar()
triangulo.mayor()
triangulo.tipo()
triangulo.dibujar()
