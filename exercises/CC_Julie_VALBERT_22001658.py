import tkinter as tk
racine = tk.Tk()

mon_canvas = tk.Canvas(racine, width=600, height=600, background="white")
mon_canvas.grid(row=2, column=0)

bouton_annuler = tk.Button(racine, text="Annuler")
bouton_annuler.grid(row=1, column=0)

objets = []


def carres():
    carre_vert = mon_canvas.create_rectangle(0, 0, 50, 50, fill="green")
    carre_bleu = mon_canvas.create_rectangle(50, 0, 100, 50, fill="blue")
    carre_blanc = mon_canvas.create_rectangle(100, 0, 150, 50, fill="white")
    return

carres()
cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="red")


def clic(event):
    global cercle
    if event.y < 50:
        if event.x < 50:
            cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="green")
            objets.append(cercle)
        elif event.x > 50 and event.x < 100:
            cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="blue")
            objets.append(cercle)
        elif event.x > 100 and event.x < 150:
            cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="white")
            objets.append(cercle)
        else :
            cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="red")
    else :
        cercle = mon_canvas.create_oval(200, 200, 400, 400, fill="red")
    return

mon_canvas.bind('<Button-1>', clic)


racine.mainloop()
