import tkinter as tk

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, width=500, height=500, background="black")
mon_canvas.grid()


def on_click(event):
    if event.x < 250:
        mon_canvas.create_oval(event.x - 50, event.y - 50,
                           event.x + 50, event.y + 50, fill="blue")
    elif event.x > 250:
        mon_canvas.create_oval(event.x - 50, event.y - 50,
                           event.x + 50, event.y + 50, fill="red")
    return


mon_canvas.bind('<Button-1>', on_click)

mon_canvas.create_line(250, 0, 250, 500, fill="white")

racine.mainloop()
