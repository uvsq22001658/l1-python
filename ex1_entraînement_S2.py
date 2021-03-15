import tkinter as tk

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, width=500, height=500, bg="black")
mon_canvas.grid(row=0, column=0)

rectangle = mon_canvas.create_rectangle(100, 200, 400, 300, fill="red")

rouge = True
actif = True


def clic(event):
    global rectangle
    global rouge
    global actif
    if actif:
        if event.x > 100 and event.x < 400 and event.y > 200 and event.y < 300:
            if rouge:
                mon_canvas.itemconfigure(rectangle, fill="blue")
                rouge = False
            else:
                mon_canvas.itemconfigure(rectangle, fill="red")
                rouge = True
        else:
            actif = False
    return


mon_canvas.bind('<Button-1>', clic)


def recommencer():
    global rectangle
    global actif
    global rouge
    mon_canvas.itemconfigure(rectangle, fill="red")
    actif = True
    rouge = True
    return


bouton_recommencer = tk.Button(racine, text="Recommencer", command=recommencer)
bouton_recommencer.grid(row=1, column=0)

racine.mainloop()
