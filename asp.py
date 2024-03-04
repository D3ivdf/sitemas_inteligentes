from time import sleep
import random
import turtle

class Ambiente(object):
    def __init__(self):
        # Estado limpio: 0   Estado Sucio: 1
        # Condic iniciales (Sucio, Sucio) ---- Aleatorio 
        self.localizacion = {"A": 1, "B": 1, "C": 1, "D": 1}
        for habitacion in self.localizacion:
            self.localizacion[habitacion] = random.choice([0, 1])

        # Crear los cuadrados para representar las habitaciones
        self.cuadrados = {}
        posiciones = {"A": (-120, 0), "B": (120, 0), "C": (0, 120), "D": (0, -120)}
        for habitacion, posicion in posiciones.items():
            self.crear_cuadrado(habitacion, posicion)

    def crear_cuadrado(self, habitacion, posicion):
        t = turtle.Turtle()
        t.penup()
        t.setpos(posicion)
        t.begin_fill()
        t.shape("square")
        t.turtlesize(5)
        if self.localizacion[habitacion] == 0:
            t.color("green")
        else:
            t.color("blue")
        t.end_fill()
        t.penup()
        self.cuadrados[habitacion] = t

    def limpiar_habitacion(self, habitacion):
        if self.localizacion[habitacion] == 1:
            self.localizacion[habitacion] = 0
            sleep(3)
            self.cuadrados[habitacion].color("green")
            print(f"La habitación {habitacion} ha sido limpiada.")
        else:
            print(f"La habitación {habitacion} ya está limpia.")

class Aspiradora(Ambiente):
    def __init__(self, Ambiente):
        super().__init__()  # Llama al inicializador de la clase base Ambiente
        self.localizacion = Ambiente.localizacion  # Inicializa localizacion como el mismo diccionario que en Ambiente
        self.movimientos = 0
        self.crear_aspiradora()
        self.contador_turtle = turtle.Turtle()
        self.contador_turtle.penup()
        self.contador_turtle.setpos(0, -180)
        self.contador_turtle.write("Movimientos: {}".format(self.movimientos), align="center", font=("Arial", 12, "normal"))
        self.verifica_estado_aspiradora(Ambiente)

    def crear_aspiradora(self):
        self.aspiradora = turtle.Turtle()
        self.aspiradora.penup()
        self.aspiradora.setpos(0, 0)
        self.aspiradora.begin_fill()
        self.aspiradora.shape("triangle")
        self.aspiradora.color("red")
        self.aspiradora.end_fill()
        self.aspiradora.penup()

    def moverse_a_habitacion(self, habitacion):
        if self.localizacion is not None:
            self.movimientos += 1
            self.contador_turtle.clear()
            self.contador_turtle.write("Movimientos: {}".format(self.movimientos), align="center", font=("Arial", 12, "normal"))

        if habitacion != self.localizacion:
            if habitacion == "A":
                self.aspiradora.setpos(-120, 0)
            elif habitacion == "B":
                self.aspiradora.setpos(120, 0)
            elif habitacion == "C":
                self.aspiradora.setpos(0, 120)
            elif habitacion == "D":
                self.aspiradora.setpos(0, -120)
            self.localizacion = habitacion

    def verifica_estado_aspiradora(self, Ambiente):
        for habitacion, estado in Ambiente.localizacion.items():
            if estado == 1:
                self.moverse_a_habitacion(habitacion)
                self.limpiar_habitacion(habitacion)

        print("Las habitaciones ahora están limpias.")

    def desempeno(self):
        print(f"El desempeño de la aspiradora es de {self.movimientos} movimientos.")
    def heuristica(self, Ambiente):
        habitaciones_sucias = [habitacion for habitacion, estado in Ambiente.localizacion.items() if estado == 1]

        while habitaciones_sucias:
            habitacion_mas_lejana = self.encontrar_habitacion_mas_lejana(habitaciones_sucias)
            self.moverse_a_habitacion(habitacion_mas_lejana)
            self.limpiar_habitacion(habitacion_mas_lejana)
            habitaciones_sucias.remove(habitacion_mas_lejana)

    def encontrar_habitacion_mas_lejana(self, habitaciones):
        distancias = {}
        for habitacion in habitaciones:
            distancia = self.calcular_distancia(habitacion)
            distancias[habitacion] = distancia
        return max(distancias, key=distancias.get)

    def calcular_distancia(self, habitacion):
        if habitacion == "A":
            return abs(self.aspiradora.xcor() + 120)
        elif habitacion == "B":
            return abs(self.aspiradora.xcor() - 120)
        elif habitacion == "C":
            return abs(self.aspiradora.ycor() - 120)
        elif habitacion == "D":
            return abs(self.aspiradora.ycor() + 120)

# Ejemplo de uso
ElAmbiente = Ambiente()
ElAspiradora = Aspiradora(ElAmbiente)
ElAspiradora.desempeno()
