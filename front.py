from tkinter import*
import back as bck


ventana=Tk()
ventana.title("Proyecto M&S - G6")
ventana.resizable(0,0)
ventana.geometry("900x500")
ventana.config(bg="green")

miFrame=Frame(ventana, width=800, height=500)
miFrame.pack()
miImagen=PhotoImage(file="images\maiz3.png")
Label(miFrame, image=miImagen).place(x=470, y=200)
Label(miFrame, text="BIENVENIDOS", fg="green", font=("Verdana", 30)).place(x=270, y=10)
Label(miFrame, text="Seleccione el(los) cultivo(s)", fg="black", font=("Verdana", 18)).place(x=50, y=100)



def cambio4():
    ventana_mas=Tk()
    ventana_mas("Proyecto M&S - G6")
    ventana_mas.resizable(0,0)
    ventana_mas.geometry("900x500")
    ventana_mas.config(bg="green")

    miFrame5=Frame(ventana_mas, width=800, height=500)
    miFrame5.pack()
    Label(miFrame5, text="Datos de rendimiento", fg="green", font=("Verdana", 30)).place(x=270, y=10)
    Label(miFrame5, text="Maíz:", fg="black", font=("Verdana", 18)).place(x=800, y=100)
    Label(miFrame5, text="Tomate:", fg="black", font=("Verdana", 18)).place(x=50, y=200)
    Label(miFrame5, text="Frijol:", fg="black", font=("Verdana", 18)).place(x=50, y=300)


def cambio3():
    ventana_final=Tk()
    ventana_final.title("Proyecto M&S - G6")
    ventana_final.resizable(0,0)
    ventana_final.geometry("900x500")
    ventana_final.config(bg="green")
    #a='0laa'
    miFrame4=Frame(ventana_final, width=800, height=500)
    miFrame4.pack()
    Label(miFrame4, text="El resultado es", fg="green", font=("Verdana", 30)).place(x=270, y=10)
    Label(miFrame4, text="Cantidad de maíz:", fg="black", font=("Verdana", 18)).place(x=50, y=100)
    #Label(miFrame4, text="a", fg="black", font=("Verdana", 18)).place(x=20, y=100)
    Label(miFrame4, text="Cantidad de tomate:", fg="black", font=("Verdana", 18)).place(x=50, y=200)
    Label(miFrame4, text="Cantidad de frijol:", fg="black", font=("Verdana", 18)).place(x=50, y=300)
    Label(miFrame4, text="Ganancia total estimada:", fg="red", font=("Verdana", 18)).place(x=50, y=400)

    botonEnviar=Button(ventana_final, text="Más información", command= cambio4)
    botonEnviar.pack()
    botonEnviar.place(x=740, y=450)




def cambio2():
    ventana_hectareas=Tk()
    ventana_hectareas.title("Proyecto M&S - G6")
    ventana_hectareas.resizable(0,0)
    ventana_hectareas.geometry("900x500")
    ventana_hectareas.config(bg="green")

    miFrame3=Frame(ventana_hectareas, width=800, height=500)
    miFrame3.pack()
    Label(miFrame3, text="Finalmente...", fg="green", font=("Verdana", 30)).place(x=270, y=10)
    Label(miFrame3, text="Indique las hectareas disponibles para cultivar", fg="black", font=("Verdana", 18)).place(x=50, y=100)
    Label(miFrame3,text="Número de hectareas", fg="black", font=("Verdana", 18)).place(x=50, y=100)
    entrada=StringVar()
    Entry(ventana_hectareas,textvariable=entrada).place(x=100, y=150)

    botonEnviar=Button(ventana_hectareas, text="Enviar", command= cambio3)
    botonEnviar.pack()
    botonEnviar.place(x=250, y=150)



def cambio():
    ventana_region=Tk()
    ventana_region.title("Proyecto M&S - G6")
    ventana_region.resizable(0,0)
    ventana_region.geometry("900x500")
    ventana_region.config(bg="green")
    
    miFrame2=Frame(ventana_region, width=800, height=500)
    miFrame2.pack()
    #miImagen2=PhotoImage(file="mapa.png")
    #Label(miFrame2, image=miImagen2).place(x=470, y=200)

    Label(miFrame2, text="Seleccione la región donde desea cultivar", fg="black", font=("Verdana", 28)).place(x=20, y=50)
    ventana.destroy()

    botonValle=Button(ventana_region, text="Valle del Cauca", command=cambio2, height = 2, width = 20, font=("Verdana", 18))
    botonValle.pack()
    botonValle.place(x=275, y=150)

    botonSantander=Button(ventana_region, text="Santander", command=cambio2, height = 2, width = 20, font=("Verdana", 18))
    botonSantander.pack()
    botonSantander.place(x=275, y=250)

    botonHuila=Button(ventana_region, text="Huila", command=cambio2, height = 2, width = 20, font=("Verdana", 18))
    botonHuila.pack()
    botonHuila.place(x=275, y=350)


botonMaiz=Button(ventana, text="Maíz", command=cambio)
botonMaiz.pack()
botonMaiz.place(x=200, y=200)

botonTomate=Button(ventana, text="Tomate", command=cambio)
botonTomate.pack()
botonTomate.place(x=200, y=300)

botonFrijol=Button(ventana, text="Frijol", command=cambio)
botonFrijol.pack()
botonFrijol.place(x=200, y=400)


ventana.mainloop()