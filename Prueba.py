import tkinter as tk
from tkinter import messagebox

def accion():
    msg = messagebox.showinfo("mensaje", "Esto es una prueba de GITHUD.")

root  = tk.Tk()
boton = tk.Button(root, text="Press", command=accion)
boton.pack()
root.mainloop()