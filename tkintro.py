import tkinter as tk # Importar libreria tkinter

ventana = tk.Tk() # Creamos nuevo objeto de la clase Ventana

ventana.title("Primer ventana") # Para cambiar titulo de la ventana
ventana.geometry("600x400") # Para cambiar tamaNo de la ventana con x minuscula
ventana.minsize(400, 200) # Para ponerle tamaNo minimo a la ventana
ventana.maxsize(800, 600) # Para ponerle tamaNo maximo a la ventana
ventana.iconbitmap() # Para ponerle un icono a la ventana  
ventana.configure(bg="deep pink") # bg=background Para cambiar el color del fondo
#Para bloquear tamaNo de la ventana usar: ventana.resizable(False, False) (True(horizontal), False(vertical))
ventana.attributes("-alpha", 0.9) # Para poner ventana opaca o transparente (mientras menos mas transparente)

etiqueta = tk.Label(ventana, text="Hola Mundo") # Crear una etiqueta a la ventana
# etiqueta.config(text="Ciao") # Para cambiar texto de etiqueta
etiqueta.config(fg="black", bg="green", font=("Arial", 14, "italic")) # fg=fuente, font= fuente de tamaNo 12 arial en negritas
etiqueta.pack() # Mostrar etiqueta


frame1 = tk.Frame(ventana) # Cuadros o contenedores para poner cosas
frame1.configure(width=300, height=200, bg="lightblue", bd=5)     # width=ancho, height=alto, bd=borde, bg=background
frame2 = tk.Frame(frame1) # Coloque otro cuadro dentro del cuadro1
frame2.configure(width=100, height=100, bg="blue", bd=5)

boton = tk.Button(frame1, text="Hola") # Crear objeto boton de la clase tkinter, en cuadro1


frame1.pack() # Para colocarlo en la ventana
frame2.pack()
boton.pack() # Para mostrarlo 

# labelframe = tk.LabelFrame(ventana, text="Grupo de widgets", bg="grey", padx=10, pady=10) # Crear objeto de una clase labelframe de tkinter 
# labelframe.configure(width=300, height=200)
# labelframe.pack()





ventana.mainloop() # Necesitamos un bucle para que la ventana se muestre




