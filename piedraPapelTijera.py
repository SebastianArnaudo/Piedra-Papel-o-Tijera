import tkinter as tk
from tkinter import Frame
import random

def main():

    ventana = tk.Tk()
    ventana.title("Piedra, Papel, Tijera")
    ventana.geometry("300x350")

    def piedra():
        
            computadora = random.randint(1,3)         
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
            

    


    framePrincipal=tk.Frame(ventana,bg="Purple")
    framePrincipal.pack(expand=True,fill="both")


    lBienvenida=tk.Label(framePrincipal,text="Bienvenido\n Elija su jugada",fg="White",bg="Purple")
    lBienvenida.place(x=100, y=10)

    bPiedra=tk.Button(framePrincipal,text="Piedra",bg="Green1", command= piedra)
    bPiedra.place(x=100,y=60)

    bPapel=tk.Button(framePrincipal,text="Papel",bg="Red1",fg="White",command= papel)
    bPapel.place(x=150,y=60)

    bTijera=tk.Button(framePrincipal,text="Tijera",bg="Blue1",fg="white", command= tijera)
    bTijera.place(x=125,y=90)

    lJugadas=tk.Label(framePrincipal,text="",fg="White",bg="Purple")
    lJugadas.place(x=65,y=150)

    lGanador=tk.Label(framePrincipal,text="",fg="White",bg="Purple")
    lGanador.place(x=90,y=200)

    lEmpate=tk.Label(framePrincipal,text="",fg="White",bg="Purple")
    lEmpate.place(x=120, y=230)
    





    tk.mainloop()

if __name__=="__main__":
    main()