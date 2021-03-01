import tkinter as tk

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, width=500, height=500, background="black")
mon_canvas.grid()

nb_clic = 0
x_precedent = 0
y_precedent = 0

def on_click(event):
    global nb_clic
    nb_clic += 1
    global x_precedent
    global y_precedent
    if nb_clic % 2 == 0:
        if (x_precedent < 250 and event.x < 250) or (x_precedent > 250 and event.x > 250):
            mon_canvas.create_line(x_precedent, y_precedent, event.x, event.y, fill="blue")
        else:
            mon_canvas.create_line(x_precedent, y_precedent, event.x, event.y, fill="red")
    x_precedent = event.x
    y_precedent = event.y
    return


mon_canvas.bind('<Button-1>', on_click)

mon_canvas.create_line(250, 0, 250, 500, fill="white")

racine.mainloop()
