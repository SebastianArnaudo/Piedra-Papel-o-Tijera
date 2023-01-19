import tkinter as tk
from tkinter import Frame

def main():

    ventana = tk.Tk()
    ventana.title("Piedra, Papel, Tijera")
    ventana.geometry("300x350")

    """Jugador eligio piedra\n Computadora eligio papel

    Gana computadora

    Jugador: 0  Computador: 1

    Ganador: Computadora"""

    framePrincipal=tk.Frame(ventana,bg="Gray")
    framePrincipal.pack(expand=True,fill="both")


    lBienvenida=tk.Label(framePrincipal,text="Bienvenido\n Elija su jugada",bg="Gray")
    lBienvenida.place(x=100, y=10)

    bTijera=tk.Button(framePrincipal,text="Tijera",bg="Green1")
    bTijera.place(x=90,y=60)

    bPiedra=tk.Button(framePrincipal,text="Piedra",bg="Red1",fg="White")
    bPiedra.place(x=140,y=60)

    bPapel=tk.Button(framePrincipal,text="Papel",bg="Blue1",fg="white")
    bPapel.place(x=115,y=90)

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