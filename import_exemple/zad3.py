import tkinter

def funkcja():
    pod_cena = int(cena.get())
    pod_dystans = int(dystans.get())
    wartosc = pod_cena * pod_dystans
    label1.config(text=wartosc)
    return wartosc



root = tkinter.Tk()
root.columnconfigure(1)

cena = tkinter.Entry(master=root)
cena.grid(row=0,column= 0)


label = tkinter.Label(master=root, text="Cena")
label.grid(row=0,column=1)

dystans = tkinter.Entry(master=root)
dystans.grid(row=1,column= 0)

dystans_label = tkinter.Label(master=root, text="Dystans")
dystans_label.grid(row=1,column=1)

label1 = tkinter.Label(master=root, text="Wynik")
label1.grid(row=2,column=0)

button_cena = tkinter.Button(master=root, text="Policz", command = funkcja)
button_cena.grid(row=4,column= 0)

#print(f'{wartosc}')

root.mainloop()