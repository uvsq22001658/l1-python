import tkinter as tk

racine = tk.Tk()
canevas = tk.Canvas(racine, height=500, width=500, bg="black")
canevas.grid(row=0, column=0)

bouton_redemarrer = tk.Button(racine, text="Redémarrer")
bouton_redemarrer.grid(row=1, column=0)

canevas.create_line(500 / 3, 0, 500 / 3, 500, fill="white")
canevas.create_line(2 * 500 / 3, 0, 2 * 500 / 3, 500, fill="white")



def croix(event):
    ligne_1 = canevas.create_line()
    ligne_2 = canevas.create_line()
    return


canevas.bind('<Button-1>', croix)

racine.mainloop()
