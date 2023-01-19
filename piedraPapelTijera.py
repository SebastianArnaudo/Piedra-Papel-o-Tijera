import tkinter as tk
from tkinter import Frame
import random

def main():

    ventana = tk.Tk()
    ventana.title("Piedra, Papel, Tijera")
    ventana.geometry("300x350")

    def piedra():
        
        computadora = random.randint(0,4)
        
        ganador = ""

        puntosJ = 0
        puntosC = 0

        eleccionJ= "Jugador eligio Piedra"
        eleccionC=""

        if computadora == 1:

            ganador = "Empate"
            eleccionC = "Computadora eligio Piedra"
        elif computadora == 2:

            ganador = "Gana Computador"
            eleccionC = "Computadora eligio Papel"
            puntosC += 1  
        else:
            ganador = "Gana Jugador"
            eleccionC = "Computadora eligio Tijera"
            puntosJ += 1
            
        
        puntosC = str(puntosC)
        puntosJ = str(puntosJ)
        
        lJugadas["text"]= eleccionJ + "\n" + eleccionC
        lGanadorRonda["text"] = ganador
        lRondas["text"] = "Jugador " + puntosJ + ", " + " Computadora " + puntosC

    def papel():

        computadora = random.randint(0,4)
        
        ganador = ""

        puntosJ = 0
        puntosC = 0

        eleccionJ= "Jugador eligio Papel"
        eleccionC=""

        if computadora == 1:

            ganador = "Gana Jugador"
            eleccionC = "Computadora eligio Piedra"
            puntosJ += 1

            
        elif computadora == 2:

            ganador = "Empate"
            eleccionC = "Computadora eligio Papel"
           
        else:
            ganador = "Gana Computadora"
            eleccionC = "Computadora eligio Tijera"
            puntosC += 1
            
        
        puntosC = str(puntosC)
        puntosJ = str(puntosJ)

        lJugadas["text"]= eleccionJ + "\n" + eleccionC
        lGanadorRonda["text"] = ganador
        lRondas["text"] = "Jugador " + puntosJ + ", " + " Computadora " + puntosC

    def tijera():
        
        computadora = random.randint(0,4)
        
        ganador = ""

        puntosJ = 0
        puntosC = 0

        eleccionJ= "Jugador eligio Tijera"
        eleccionC=""

        if computadora == 1:

            ganador = "Gana Computadora"
            eleccionC = "Computadora eligio Piedra"
            puntosC += 1
        elif computadora == 2:

            ganador = "Gana Jugador"
            eleccionC = "Computadora eligio Papel"
            puntosJ += 1           
        else:
            
            ganador = "Empate"
            eleccionC = "Computadora eligio Tijera"
            
        
        puntosC = str(puntosC)
        puntosJ = str(puntosJ)

        lJugadas["text"]= eleccionJ + "\n" + eleccionC
        lGanadorRonda["text"] = ganador
        lRondas["text"] = "Jugador " + puntosJ + ", " + " Computadora " + puntosC   



    framePrincipal=tk.Frame(ventana,bg="Gray")
    framePrincipal.pack(expand=True,fill="both")


    lBienvenida=tk.Label(framePrincipal,text="Bienvenido\n Elija su jugada",bg="Gray")
    lBienvenida.place(x=100, y=10)

    bPiedra=tk.Button(framePrincipal,text="Piedra",bg="Green1", command= piedra)
    bPiedra.place(x=90,y=60)

    bPapel=tk.Button(framePrincipal,text="Papel",bg="Red1",fg="White",command= papel)
    bPapel.place(x=140,y=60)

    bTijera=tk.Button(framePrincipal,text="Tijera",bg="Blue1",fg="white", command= tijera)
    bTijera.place(x=115,y=90)

    lJugadas=tk.Label(framePrincipal,text="",bg="Gray")
    lJugadas.place(x=65,y=150)

    lGanadorRonda=tk.Label(framePrincipal,text="",bg="Gray")
    lGanadorRonda.place(x=80,y=200)

    lRondas=tk.Label(framePrincipal,text="",bg="Gray")
    lRondas.place(x=70,y=250)

    lGanador=tk.Label(framePrincipal,text="",bg="Gray")
    lGanador.place(x=75,y=300)




    tk.mainloop()

if __name__=="__main__":
    main()