
#%% Dependences
import random
import turtle
from time import sleep

#%% Variables
global t1,t2,t3,t4
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()

#%%main
t1.penup()
t1.begin_fill()
t1.setpos(-140,60)
t1.write("Lado A", align="center",font=("Arial",15,"normal"))
t1.end_fill()
t1.penup()

t2.penup()
t2.begin_fill()
t2.setpos(140,60)
t2.write("Lado B", align="center",font=("Arial",15,"normal"))
t2.end_fill()
t2.penup()

t3.penup()
t3.begin_fill()
t3.setpos(140,-90)
t3.write("Lado C", align="center",font=("Arial",15,"normal"))
t3.end_fill()
t3.penup()

t4.penup()
t4.begin_fill()
t4.setpos(-140,-90)
t4.write("Lado D", align="center",font=("Arial",15,"normal"))
t4.end_fill()
t4.penup()


class Ambiente(object):
    def __init__(self):
        # Estado limpio: 0   Estado Sucio: 1
        # Condic iniciales (Sucio, Sucio) ---- Aleatorio 
        self.posiciones = {"A": [-120, 0], "B": [120, 0], "C": [120, -150], "D": [-120, -150]}
        self.localizacion={"A":"1","B":"1","C":"1","D":"1"}
        # Las condiciones de la localizacion inicial son aleatorias
        self.localizacion["A"]=random.choice([0,1])
        self.localizacion["B"]=random.choice([0,1])
        self.localizacion["C"]=random.choice([0,1])
        self.localizacion["D"]=random.choice([0,1])
        print(40*"=")
        print('esta es la inicial ',self.localizacion)

        self.A=turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120,0)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        if self.localizacion["A"]==0:
            self.A.color("green")
        else:
            self.A.color("blue")
        self.A.end_fill()
        self.A.penup()

        self.B=turtle.Turtle()
        self.B.penup()
        self.B.setpos(120,0)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        if self.localizacion["B"]==0:
            self.B.color("green")
        else:
            self.B.color("yellow")
        self.B.end_fill()
        self.B.penup()

        self.C=turtle.Turtle()
        self.C.penup()
        self.C.setpos(120,-150)
        self.C.begin_fill()
        self.C.shape("square")
        self.C.turtlesize(5)
        if self.localizacion["C"]==0:
            self.C.color("green")
        else:
            self.C.color("gray")
        self.C.end_fill()
        self.C.penup()
        

        self.D=turtle.Turtle()
        self.D.penup()
        self.D.setpos(-120,-150)
        self.D.begin_fill()
        self.D.shape("square")
        self.D.turtlesize(5)
        if self.localizacion["D"]==0:
            self.D.color("green")
        else:
            self.D.color("pink")
        self.D.end_fill()
        self.D.penup()




class IAspirador(Ambiente):
    def __init__(self,Ambiente):
        # Localización del aspirador, si el salon es A o B
        global localizacionAspirador
        localizacionAspirador= None
        self.contador_movimientos = 0
        print(40*"*")
        print("El ambiente esta: ",Ambiente.localizacion)
        
        global Asp
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,-80)
        Asp.begin_fill()
        Asp.shape("triangle")
        #Asp.turtlesize(5)
        Asp.color("red")
        Asp.end_fill()
        Asp.penup()

        self.contador_turtle = turtle.Turtle()
        self.contador_turtle.penup()
        self.contador_turtle.setpos(0, -120)
        self.contador_turtle.write("Movimientos: {}".format(self.contador_movimientos), align="center", font=("Arial", 12, "normal"))
    def sumar_movimiento(self):
        self.contador_movimientos += 1
        self.contador_turtle.clear()
        self.contador_turtle.write("Movimientos: {}".format(self.contador_movimientos), align="center", font=("Arial", 12, "normal"))
    def verifica_estado_aspirador(self, Ambiente):

        if Ambiente.localizacion["A"]==1:
            result1="El aspirador es colocado en el local A \n"
            self.sumar_movimiento()
            Asp.speed(10)
            Asp.setpos(-120,0)
            return print(result1)
        elif Ambiente.localizacion["B"]==1:
            result2="El aspirador es colocado en el local B \n"
            self.sumar_movimiento()
            Asp.speed(10)
            Asp.setpos(120,0)
            return print(result2)
        elif Ambiente.localizacion["C"]==1:
            result3="El aspirador es colocado en el local C \n"
            self.sumar_movimiento()
            Asp.setpos(120,-150)
            return print(result3)
        elif Ambiente.localizacion["D"]==1:
            result4="El aspirador es colocado en el local D \n"
            self.sumar_movimiento()
            Asp.speed(10)
            Asp.setpos(-120,-150)
            return print(result4)
    
    def verifica_estado_ambiente(self,Ambiente):
        sucio = False

        ambientes = ["A", "B", "C", "D"]
        for habitacion in ambientes:
            if Ambiente.localizacion[habitacion] == 1:
                print("El aspirador se coloca en la habitación", habitacion)
                IAspirador.mover_aspiradora(self, Ambiente, habitacion)
                sleep(3)
                IAspirador.aspirar(self, Ambiente, habitacion)
                sucio = True
        # while sucio:
        #     # Si el lado A estuviese sucio
        #     if Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==0:
        #         print("El lado A esta sucio...")
        #         IAspirador.aspiraA(self,Ambiente)
        #         print("El lado B ya esta limpio")
        #     elif Ambiente.localizacion["A"]==0 and Ambiente.localizacion["B"]==1:
        #         print("El lado B esta sucio...")
        #         IAspirador.aspiraB(self,Ambiente)
        #         print("El lado A ya esta limpio")
        #     elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==1:
        #         print("El lado A esta sucio...")
        #         IAspirador.aspiraA(self,Ambiente)
        #         IAspirador.moverse(self,Ambiente)
        #         self.contador_movimientos += 1
        #         self.contador_turtle.clear()
        #         self.contador_turtle.write("Movimientos: {}".format(self.contador_movimientos), align="center", font=("Arial", 12, "normal"))
        #         IAspirador.aspiraB(self,Ambiente)
        #     else:
        #         print("Todo esta limpio")
        #         return False
        Asp.setpos(0, -80)
    
    def aspiraA(self, Ambiente):
        Ambiente.localizacion["A"]=0
        sleep(1.5)
        print("El lado A fue limpiado")
        Ambiente.A.color("green")   
    
    def aspiraB(self,Ambiente):
        Ambiente.localizacion["B"]=0
        sleep(1.5)
        print("El lado B fue limpiado")
        Ambiente.B.color("green")
    
    def aspiraC(self,Ambiente):
        Ambiente.localizacion["C"]=0
        sleep(1.5)
        print("El lado C fue limpiado")
        Ambiente.C.color("green")
        
    def aspiraD(self,Ambiente):
        Ambiente.localizacion["D"]=0
        sleep(1.5)
        print("El lado D fue limpiado")
        Ambiente.D.color("green")
        
    def aspirar(self, Ambiente, habitacion):
        Ambiente.localizacion[habitacion] = 0
        sleep(1.5)
        print("La habitación", habitacion, "fue limpiada.")
        getattr(Ambiente, habitacion).color("green")

    def mover_aspiradora(self, Ambiente, habitacion):
        x_objetivo, y_objetivo = Ambiente.posiciones[habitacion]
        Asp.setpos(x_objetivo, y_objetivo)

       
    def moverse(self,Ambiente):
        posiciones = [[-120, 0], [120, 0], [120, -150], [-120, -150]]
        ambientes = ["A", "B", "C", "D"]
        for ambiente in ambientes:
            if Ambiente.locazacion[ambiente] == 1:
                localizacionAspirador=ambiente
                
        # if Ambiente.localizacion["B"]==1:
        #     print("\nSe mueve para el lado B..\n.")
        #     localizacionAspirador="B"
        #     Asp.forward(240)
        # elif Ambiente.localizacion["A"]==1:
        #     print("\n Se mueve para el lado A...")
        #     localizacionAspirador="A"
        #     Asp.back(240)



#####   LIMPIAR
ElAmbiente=Ambiente()
ElAspirador=IAspirador(ElAmbiente)
sleep(3)
ElAspirador.verifica_estado_aspirador(ElAmbiente)
sleep(3)
ElAspirador.verifica_estado_ambiente(ElAmbiente)



#### Al terminar muestra los dos lados limpios
print("\nDespues de la accion del  aspirador, el ambiente esta:  ", ElAmbiente.localizacion)
sleep(5)
#quit()