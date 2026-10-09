import tkinter as tk
ventana = tk.Tk()
ventana.title("Entry")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

entrada= tk.Entry(ventana) # Creamos un entry que es un espacio para que el usuario escriba algo en pantalla y lo recoja o guarde
entrada.config(fg="white", bg="black", font=("Arial", 14))
entrada.pack()

entrada.insert(0, "Nombre")
texto = entrada.get() # Obten

ventana.mainloop()