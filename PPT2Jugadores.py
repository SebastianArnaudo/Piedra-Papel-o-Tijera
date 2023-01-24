import tkinter as tk
from tkinter import Frame
import random

def main():

    vInicio=tk.Tk()
    vInicio.title("Inicio")
    vInicio.geometry("300x200")


    def UnJugador():
        
        vUnJugador=tk.Toplevel()
        vUnJugador.title("Piedra, Papel o Tijera")
        vUnJugador.geometry("300x350")

        def piedra():
        
            computadora = random.randint(0,4)
            
            ganador = ""

            empate = ""
        

            eleccionJ= "Jugador eligio Piedra"
            eleccionC=""

            if computadora == 1:

                empate = "Empate"
                eleccionC = "Computadora eligio Piedra"
            elif computadora == 2:

                ganador = "Gana Computador"
                eleccionC = "Computadora eligio Papel"
                
            else:
                ganador = "Gana Jugador"
                eleccionC = "Computadora eligio Tijera"
            
            lJugadas["text"]= eleccionJ + "\n" + eleccionC
            lGanador["text"] = ganador
            lEmpate["text"] = empate
            

        def papel():

            computadora = random.randint(0,4)
            
            ganador = ""

            empate = ""


            eleccionJ= "Jugador eligio Papel"
            eleccionC=""

            if computadora == 1:

                ganador = "Gana Jugador"
                eleccionC = "Computadora eligio Piedra"
                

                
            elif computadora == 2:

                empate = "Empate"
                eleccionC = "Computadora eligio Papel"
            
            else:
                ganador = "Gana Computadora"
                eleccionC = "Computadora eligio Tijera"
                
            lJugadas["text"]= eleccionJ + "\n" + eleccionC
            lGanador["text"] = ganador
            lEmpate["text"] = empate

        def tijera():
            
            computadora = random.randint(0,4)
            
            ganador = ""

            empate = ""

            eleccionJ= "Jugador eligio Tijera"
            eleccionC=""

            if computadora == 1:

                ganador = "Gana Computadora"
                eleccionC = "Computadora eligio Piedra"
                
            elif computadora == 2:

                ganador = "Gana Jugador"
                eleccionC = "Computadora eligio Papel"
                        
            else:
                
                empate = "Empate"
                eleccionC = "Computadora eligio Tijera"
                
            
            

            lJugadas["text"] = eleccionJ + "\n" + eleccionC
            lGanador["text"] = ganador
            lEmpate["text"] = empate
            

    


        frameUnJugador=tk.Frame(vUnJugador,bg="Gray")
        frameUnJugador.pack(expand=True,fill="both")


        lBienvenida=tk.Label(frameUnJugador,text="Bienvenido\n Elija su jugada",bg="Gray")
        lBienvenida.place(x=100, y=10)

        bPiedra=tk.Button(frameUnJugador,text="Piedra",bg="Green1", command= piedra)
        bPiedra.place(x=100,y=60)

        bPapel=tk.Button(frameUnJugador,text="Papel",bg="Red1",fg="White",command= papel)
        bPapel.place(x=150,y=60)

        bTijera=tk.Button(frameUnJugador,text="Tijera",bg="Blue1",fg="white", command= tijera)
        bTijera.place(x=125,y=90)

        lJugadas=tk.Label(frameUnJugador,text="",bg="Gray")
        lJugadas.place(x=65,y=150)

        lGanador=tk.Label(frameUnJugador, text="",bg="Gray")
        lGanador.place(x=90,y=200)

        lEmpate=tk.Label(frameUnJugador, text="",bg="Gray")
        lEmpate.place(x=120, y=230)
    





        tk.mainloop()

    def dosJugadores():

        vDosJugadores=tk.Toplevel()
        vDosJugadores.title("Piedra, Papel o Tijeras")
        vDosJugadores.geometry("300x400")

        frameDosJugadores=Frame(vDosJugadores,bg="orange1")
        frameDosJugadores.pack(expand=True,fill="both")

        lJugador1=tk.Label(frameDosJugadores,text="Jugador1\n Elija su jugada",bg="orange")
        lJugador1.place(x=100, y=10)

        bPiedraJ1=tk.Button(frameDosJugadores,text="Piedra",bg="Green1")
        bPiedraJ1.place(x=100,y=60)

        bPapelJ1=tk.Button(frameDosJugadores,text="Papel",bg="Red1",fg="White")
        bPapelJ1.place(x=150,y=60)

        bTijeraJ1=tk.Button(frameDosJugadores,text="Tijera",bg="Blue1",fg="white")
        bTijeraJ1.place(x=125,y=90)

        lJugador2=tk.Label(frameDosJugadores,text="Jugador2\n Elija su jugada",bg="orange")
        lJugador2.place(x=100, y=150)

        bPiedraJ2=tk.Button(frameDosJugadores,text="Piedra",bg="Green1")
        bPiedraJ2.place(x=100,y=200)

        bPapelJ2=tk.Button(frameDosJugadores,text="Papel",bg="Red1",fg="White")
        bPapelJ2.place(x=150,y=200)

        bTijeraJ2=tk.Button(frameDosJugadores,text="Tijera",bg="Blue1",fg="white")
        bTijeraJ2.place(x=125,y=230)


        """lJugadas=tk.Label(frameDosJugadores,text="",bg="Gray")
        lJugadas.place(x=65,y=150)

        lGanador=tk.Label(frameDosJugadores, text="",bg="Gray")
        lGanador.place(x=90,y=200)

        lEmpate=tk.Label(frameDosJugadores, text="",bg="Gray")
        lEmpate.place(x=120, y=230)"""

        tk.mainloop()




    frameInicio=Frame(vInicio,bg="Purple")
    frameInicio.pack(expand=True,fill="both")

    lBienvenida = tk.Label(frameInicio,text="Bienvenido\n Por favor ingrese la modalidad de juego",bg="Purple")
    lBienvenida.place(x=40, y=10)

    bUnJugador = tk.Button(frameInicio,text="Un jugador",command=UnJugador,bg="blue1")
    bUnJugador.place(x=115,y=50)

    bDosJugadores = tk.Button(frameInicio,text="Dos Judadores",command= dosJugadores, bg="blue1")
    bDosJugadores.place(x=106,y=80)

    tk.mainloop()

if __name__ == "__main__":
    main()