from tkinter import *


def main():

    ventana = Tk()
    ventana.title('Las Recetas')
    ventana.configure(bg = "sky blue")
    ventana.resizable(0,0)
    #ventana.iconbitmap("name")
    
    myframe = Frame()
    myframe.pack(side="left",anchor="n")
    myframe.config(width="600",height="350",bg="sky blue")

    titulo = Label(myframe, text="Las Recetas: ",bg="sky blue",font=("Georgia", 20))
    titulo.place(x=10,y=15)

    Buscador = Button(myframe, text="Buscar: ")
    Buscador.place(x=530,y=20)
    Lupa = Entry(myframe)
    Lupa.place(x=400,y=20)

    
    receta = Button(myframe,text="Nueva Receta")
    receta.place(x=250, y=20)

   
    Campo=Text(myframe,width="50",height="15",highlightthickness=2)
    Campo.place(x=90, y=70)
    scroll= Scrollbar(myframe)
    scroll.place(x=90, y=70)
    scroll.config(command=Campo.yview)
    Campo.config(yscrollcommand=scroll.set)

    ventana.mainloop()

if __name__ == "__main__":
    main()