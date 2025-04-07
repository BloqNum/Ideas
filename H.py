import tkinter as tk
def km():
    valor=va.get()
    f = float(ent.get())
    if valor==0:
        f=f/1.60934
        resultado.config(text=f)
    if valor==1:
        f=f/3600*1000
        resultado.config(text=f)
    if valor==2:
        f=f/1.852
        resultado.config(text=f)
    if valor==3:
        f=f/3600
        resultado.config(text=f)
window=tk.Tk()
window.title("Conversor")
window.geometry("300x125")
window.resizable(width=False, height=False)
va=tk.IntVar()
mph=tk.Radiobutton(window,text="MP/H",font="Arial", variable=va, value=0, padx=5, pady=5)
ms=tk.Radiobutton(window,text="MT/S",font="Arial", variable=va, value=1, padx=5, pady=5)
mnh=tk.Radiobutton(window, text="MN/H", font="Arial", variable=va, value=2, padx=5, pady=5)
kms=tk.Radiobutton(window, text="Km/S", font="Arial", variable=va, value=3, padx=5, pady=5)
et=tk.Label(window,text="KM/H a ....", font="Arial",  padx=5, pady=5)
va2=tk.IntVar()
ent=tk.Entry(window, justify=tk.CENTER, textvariable=va2)
resultado=tk.Label(window, bg="gray", width=17)
calcular=tk.Button(window, text="Calcular", font="Arial", command=km,  padx=5)
ent.focus()
calcular.bind("<Return>")
kms.grid(column=2, row=1)
resultado.grid(column=0,row=2)
ent.grid(column=0, row=1)
et.grid(column=0, row=0)
mnh.grid(column=2, row=0)
mph.grid(column=1,row=0)
ms.grid(column=1, row=1)
calcular.grid(column=1, row=2, columnspan=2)
window.mainloop()