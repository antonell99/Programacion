import time
import tkinter as tk
ventana = tk.Tk()
ventana.title("Ejemplo")

boton = tk.Button(ventana, text="Presiona aqui")
boton.config(fg="white", bg="green", font=("Arial", 12)) 
boton.pack()

etiqueta = tk.Label(ventana, text="Hola, soy un label")
etiqueta.pack()

# def boton_presionado(): # Definir funcion que se llama boton_presionado
    # print("Boton Presionado!") # Cada vez que se llame la funcion se imprime boton presionado!
    
def cambiar_texto():
    etiqueta.config(text="Boton presionado!!") # Para cambiar texto de la etiqueta
    
boton.config(command=cambiar_texto) # Para que boton cumpla la funcion

ventana.mainloop()