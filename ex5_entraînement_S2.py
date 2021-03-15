import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, height=600, width=600, bg="white")
canvas.grid(row=0, column=0)

abs_rouge = 200
abs_bleue = 400
ligne_rouge = canvas.create_line(abs_rouge, 0, abs_rouge, 600, fill="red")
ligne_bleue = canvas.create_line(abs_bleue, 0, abs_bleue, 600, fill="blue")
rouge = True


def deplace(event):
    global ligne_rouge
    global ligne_bleue
    global abs_rouge
    global abs_bleue
    global rouge
    if event.x <= abs_rouge and event.x <= abs_bleue:
        abs_rouge = abs_rouge - 10
        abs_bleue = abs_bleue - 10
        canvas.move(ligne_rouge, -10, 0)
        canvas.move(ligne_bleue, -10, 0)
    elif event.x >= abs_rouge and event.x >= abs_bleue:
        abs_rouge += 10
        abs_bleue += 10
        canvas.move(ligne_rouge, 10, 0)
        canvas.move(ligne_bleue, 10, 0)
    else:
        abs_rouge += 10
        abs_bleue = abs_bleue - 10
        canvas.move(ligne_rouge, 10, 0)
        canvas.move(ligne_bleue, -10, 0)
    if rouge:
        canvas.itemconfigure(ligne_rouge, fill="blue")
        canvas.itemconfigure(ligne_bleue, fill="red")
        rouge = False
    else:
        canvas.itemconfigure(ligne_rouge, fill="red")
        canvas.itemconfigure(ligne_bleue, fill="blue")
        rouge = True
    return


canvas.bind('<Button-1>', deplace)


def recommencer():
    global ligne_rouge
    global ligne_bleue
    global abs_rouge
    global abs_bleue
    global rouge
    canvas.delete(ligne_rouge)
    canvas.delete(ligne_bleue)
    abs_rouge = 200
    abs_bleue = 400
    ligne_rouge = canvas.create_line(abs_rouge, 0, abs_rouge, 600, fill="red")
    ligne_bleue = canvas.create_line(abs_bleue, 0, abs_bleue, 600, fill="blue")
    rouge = True
    return


bouton_recommencer = tk.Button(racine, text="Recommencer", command=recommencer)
bouton_recommencer.grid(row=1, column=0)

racine.mainloop()
