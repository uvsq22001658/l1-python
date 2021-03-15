import tkinter as tk

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, width=500, height=500, bg="white")
mon_canvas.grid(row=0, column=0)

nb_clic = 0
x_precedent = 0
y_precedent = 0
objets = []
actif = True


def effacer():
    if len(objets) > 0:
        dernier_objet = objets[len(objets) - 1]
        mon_canvas.delete(dernier_objet)
        del objets[len(objets) - 1]
    return


def pause():
    global actif
    global bouton_pause
    if actif:
        actif = False
        mon_canvas.itemconfigure(bouton_pause, text="Restart")
    else:
        actif = True
        mon_canvas.itemconfigure(bouton_pause, text="Pause")
    return


def clic(event):
    global nb_clic
    nb_clic += 1
    global x_precedent
    global y_precedent
    global objets
    if actif:
        if nb_clic == 2:
            ligne_bleue = mon_canvas.create_line(x_precedent, y_precedent, event.x, event.y, fill="blue")
            objets.append(ligne_bleue)
        elif nb_clic == 4:
            ligne_rouge = mon_canvas.create_line(x_precedent, y_precedent, event.x, event.y, fill="red")
            objets.append(ligne_rouge)
        elif nb_clic == 5:
            effacer()
            effacer()
            nb_clic = 0
        else:
            x_precedent = event.x
            y_precedent = event.y
    return


mon_canvas.bind('<Button-1>', clic)

bouton_pause = tk.Button(racine, text="Pause", command=pause)
bouton_pause.grid(row=1, column=0)

racine.mainloop()
