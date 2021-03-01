import tkinter as tk

racine = tk.Tk()
mon_canvas = tk.Canvas(racine, width=500, height=500, background="black")
mon_canvas.grid()


def on_click(event):
    mon_canvas.create_line(event.x, event.y, event.x + 1, event.y, fill="red")
    return


mon_canvas.bind('<Button-1>', on_click)

racine.mainloop()
