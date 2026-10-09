import time
import tkinter as tk


ventana = tk.Tk()
ventana.title("Ejemplo reloj")

etiqueta = tk.Label(ventana, text="Hola Mundo")
etiqueta.config(fg="black", bg="green", font=("Arial", 14, "italic")) 
etiqueta.pack()

def actualizar_hora(): # Crear funcion que se va a llamar actualizar_hora
    etiqueta.config(text=time.strftime("%H:%M:%S")) # Cambiar texto y traer de la libreria time la hora actual
    ventana.after(1000, actualizar_hora) # Ejecutar una accion en este caso cada 1000 milisegundos(1 segundo)
    
    
    
actualizar_hora()

ventana.mainloop()