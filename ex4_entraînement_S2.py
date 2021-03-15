import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, height=500, width=500, bg="white")
canvas.grid(row=0, column=0)

actif = True
abscisse_1 = 225
ordonnee_1 = 225
abscisse_2 = 275
ordonnee_2 = 275
cote_carre = 50

carre_rouge = canvas.create_rectangle(abscisse_1, ordonnee_1,
                                      abscisse_2, ordonnee_2, fill="red")


def diminue(event):
    global abscisse_1
    global ordonnee_1
    global abscisse_2
    global ordonnee_2
    global carre_rouge
    global cote_carre
    if actif:
        if (event.x >= abscisse_1) and (event.x <= abscisse_2) and
           (event.y >= ordonnee_1) and (event.y <= ordonnee_2) and (cote_carre >= 20):
            Canvas.itemconfigure(carre_rouge, abscisse_1 += 5, ordonnee_1 += 5,
                                 abscisse_2 -= 5, ordonnee_2 -= 5)
            cote_carre -= 10
    return


canvas.bind('<Button-1>', diminue)


def augmente(event):
    global abscisse_1
    global ordonnee_1
    global abscisse_2
    global ordonnee_2
    global carre_rouge
    global cote_carre
    if actif:
        if (event.x <= abscisse_1) and (event.x >= abscisse_2) and
        (event.y <= ordonnee_1) and (event.y >= ordonnee_2)
        and (cote_carre >= 100):
            canvas.itemconfigure(carre_rouge, abscisse_1 -= 5, ordonnee_1 -= 5,
                                 abscisse_2 += 5, ordonnee_2 += 5)
            cote_carre += 10
    return


canvas.bind('<Button-1>', augmente)


def pause():
    global actif
    if actif = True:
        actif = False
        canvas.itemconfigure(bouton_pause, text="Restart")
    else:
        actif = True
    canvas.itemconfigure(bouton_pause, text="Pause")


bouton_pause = tk.Button(racine, text="Pause", command=pause)
bouton_pause.grid(row=1, column=0)

racine.mainloop()
