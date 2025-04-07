import tkinter as tk
import time
def actualizar_hora():
    hora.config(text=time.strftime("%H:%M:%S"))
    window.after(ms=1000, func=actualizar_hora)
window= tk.Tk()
window.geometry("200x25")
window.title("Reloj")
hora= tk.Label(window,text="", bg="black",fg="forest green", width=200, height=25, font=("Arial", 20))
hora.pack()
window.after(ms=1000, func=actualizar_hora)
window.mainloop()