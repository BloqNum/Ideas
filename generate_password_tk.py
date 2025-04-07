import random
import string
import tkinter as tk
def generador_contraseña():
    try:
        eleccion = integer.get()
    except ValueError:
        instr2.config(text="Enter a integer")
    contraseña = []
    ran = 0
    for i in range(int(eleccion)):
        ran=random.randint(1,3)
        if ran==1:
            contraseña.append(random.choice(string.ascii_lowercase))
        if ran==2:
            contraseña.append(random.choice(string.ascii_uppercase))
        if ran==3:
            contraseña.append(random.choice(string.digits))
    OUTPUT.config(text="".join(contraseña))
    instr2.config(text="OUTPUT")
def copy():
    if OUTPUT["text"]=="":
        instr2.config(text="Not Found")
    else:
        text=OUTPUT.cget("text")
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update
        instr2.config(text="Copy Successful")
window= tk.Tk()
window.resizable(width=False, height=False)
window.title("Generate Password")
integer= tk.IntVar()
OUTPUT=tk.Label(window,font="Arial, 12", justify=tk.CENTER, text="", width=20, bg="green")
INPUT=tk.Entry(window,font="Arial, 12", justify=tk.CENTER,text="Write here", textvariable=integer
                    )
SEÑAL=tk.Button(window,font="Arial, 12",bg="green", justify=tk.CENTER, text="GENERATE",
                    command= generador_contraseña)
instr=tk.Label(window, font=("Arial, 12"), justify=tk.CENTER, text="Enter the number of digits")
instr2=tk.Label(window, font=("Arial, 12"), justify=tk.CENTER, text="OUTPUT")
COPY=tk.Button(window, font="Arial, 12", bg="blue", justify=tk.CENTER, text="COPY", command=copy)
COPY.grid(column=2, row=2, rowspan=2)
instr.grid(column=1, row=0)
instr2.grid(column=1, row=2)
INPUT.grid(column=1, row=1)
OUTPUT.grid(column=1, row=3)
SEÑAL.grid(column=2, row=0, rowspan=2)
INPUT.focus()
OUTPUT.bind("<Button-1>")
window.mainloop()