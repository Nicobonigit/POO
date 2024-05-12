#El ejercicio consiste en crear una super clase llamada persona y luego clase llamada empleado. se le dan parametros como nombre y edad en la superclase. Luego la clase empleado hereda estos atributos
# y también se ingresa el salario que cobra con el fin de saber si paga impuestos o no. 


class persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
    def mostrar(self):
        print(self.nombre)
        print(self.edad)
class empleado:
    def __init__ (self):
        super().__init__()
        self.sueldo=int(input("Ingrese sueldo: "))
    def pagaimpuesto(self):
        if self.sueldo > 3000:
            print("Paga impuesto")
        else:
            print("No paga impuesto")

p=persona()
e=empleado()
p.mostrar()
e.pagaimpuesto()


#otra forma de hacer el mismo ejercicio

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):  # Empleado hereda de Persona
    def __init__(self):
        super().__init__()  # Llama al constructor de Persona
        self.sueldo = int(input("Ingrese sueldo: "))

    def pagaimpuesto(self):
        if self.sueldo > 3000:
            print("Paga impuesto")
        else:
            print("No paga impuesto")


# Crear una instancia de Empleado
e = Empleado()
e.mostrar()  # Mostrar los detalles de la persona
e.pagaimpuesto()  # Comprobar si debe pagar impuestos
