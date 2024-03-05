import random
import turtle
from time import sleep

class Ambiente(object):
    def __init__(self):
        self.localizacion = {"A": random.choice([0,1]),
                             "B": random.choice([0,1]),
                             "C": random.choice([0,1]),
                             "D": random.choice([0,1])}
        print("=" * 40)
        print('Estado inicial del ambiente:', self.localizacion)

        self.A = turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120, 0)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        if self.localizacion["A"] == 0:
            self.A.color("green")
        else:
            self.A.color("blue")
        self.A.end_fill()
        self.A.penup()

        self.B = turtle.Turtle()
        self.B.penup()
        self.B.setpos(120, 0)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        if self.localizacion["B"] == 0:
            self.B.color("green")
        else:
            self.B.color("yellow")
        self.B.end_fill()
        self.B.penup()

        self.C = turtle.Turtle()
        self.C.penup()
        self.C.setpos(120, -150)
        self.C.begin_fill()
        self.C.shape("square")
        self.C.turtlesize(5)
        if self.localizacion["C"] == 0:
            self.C.color("green")
        else:
            self.C.color("red")
        self.C.end_fill()
        self.C.penup()

        self.D = turtle.Turtle()
        self.D.penup()
        self.D.setpos(-120, -150)
        self.D.begin_fill()
        self.D.shape("square")
        self.D.turtlesize(5)
        if self.localizacion["D"] == 0:
            self.D.color("green")
        else:
            self.D.color("pink")
        self.D.end_fill()
        self.D.penup()


class IAspirador(Ambiente):
    def __init__(self, Ambiente):
        self.contador_movimientos = 0
        print("*" * 40)
        print("El ambiente está:", Ambiente.localizacion)

        self.contador_turtle = turtle.Turtle()
        self.contador_turtle.penup()
        self.contador_turtle.setpos(0, -120)
        self.contador_turtle.write("Movimientos: {}".format(self.contador_movimientos), align="center", font=("Arial", 12, "normal"))

        self.verifica_estado_aspirador(Ambiente)
        self.verifica_estado_ambiente(Ambiente)

    def mover_a_habitacion(self, habitacion):
        posiciones = {"A": (-120, 0), "B": (120, 0), "C": (120, -150), "D": (-120, -150)}
        Asp.goto(posiciones[habitacion])

    def limpiar_habitacion(self, habitacion):
        Ambiente.localizacion[habitacion] = 0
        sleep(1.5)
        print("La habitación {} ha sido limpiada".format(habitacion))
        if habitacion == "A":
            self.A.color("green")
        elif habitacion == "B":
            self.B.color("green")
        elif habitacion == "C":
            self.C.color("green")
        elif habitacion == "D":
            self.D.color("green")

    def verifica_estado_aspirador(self, Ambiente):
        for habitacion, estado in Ambiente.localizacion.items():
            if estado == 1:
                print("El aspirador se coloca en la habitación", habitacion)
                self.contador_movimientos += 1
                self.contador_turtle.clear()
                self.contador_turtle.write("Movimientos: {}".format(self.contador_movimientos), align="center", font=("Arial", 12, "normal"))
                Asp.speed(10)
                self.mover_a_habitacion(habitacion)
                break

    def verifica_estado_ambiente(self, Ambiente):
        sucio = True
        while sucio:
            habitaciones_sucias = [habitacion for habitacion, estado in Ambiente.localizacion.items() if estado == 1]
            if not habitaciones_sucias:
                print("¡Todas las habitaciones están limpias!")
                return

            distancia_minima = float('inf')
            habitacion_mas_cercana = None

            for habitacion in habitaciones_sucias:
                posiciones = {"A": (-120, 0), "B": (120, 0), "C": (120, -150), "D": (-120, -150)}
                distancia = abs(Asp.xcor() - posiciones[habitacion][0]) + abs(Asp.ycor() - posiciones[habitacion][1])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    habitacion_mas_cercana = habitacion

            if habitacion_mas_cercana:
                self.mover_a_habitacion(habitacion_mas_cercana)
                self.limpiar_habitacion(habitacion_mas_cercana)

            sucio = False
            for habitacion, estado in Ambiente.localizacion.items():
                if estado == 1:
                    sucio = True
                    break

# Inicialización de la ventana de la interfaz gráfica
turtle.setup(width=600, height=600)
Asp = turtle.Turtle()
Asp.penup()

# Creación de la instancia del ambiente
ElAmbiente = Ambiente()

# Creación de la instancia del aspirador
ElAspirador = IAspirador(ElAmbiente)

# Esperar unos segundos antes de cerrar la ventana
sleep(5)
turtle.done()
