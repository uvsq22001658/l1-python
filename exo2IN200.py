import tkinter as tk
import random as rd

clic = 0
# x2, y2, x3, y3 = 0, 0, 150, 100
n, m = 4, 4
compteur_balle = 0


def creer_rectangle(x2, y2, x3, y3):
   canvas.create_rectangle((x2, y2, x3, y3), fill="pink")

   print()

   balle = creer_balle(x2, y2, x3, y3)

   return[balle, x2, y2, x3, y3]


def quadrillage(n, m):
   liste = []
   x2, y2, x3, y3 = 0, 0, 150, 100

   for i in range(n):
       if i != 0:
           x2 += 150
           x3 += 150
       for j in range(m):
           y2 += 100
           y3 += 100

           if j == (m-1):
               y2 = 0
               y3 = 100

           liste.append(creer_rectangle(x2, y2, x3, y3))

   return liste


def demarrer(rectangle):
   global clic, after_balle

   if clic == 0:
       mouvement(rectangle)
       bouton["text"] = "Arreter"
       clic = 1

   elif clic == 1:
       canvas.after_cancel(after_balle)
       bouton["text"] = "Démarrer"
       clic = 0


def creer_balle(x2, y2, x3, y3):

   cercle = canvas.create_oval(((x3-75) - 5), ((y3-50) - 5), ((x3-75) + 5),\
                               ((y3-50) + 5), fill="blue")

   aleatoire1 = rd.randint(1, 7)
   aleatoire2 = rd.randint(1, 7)

   return[cercle, aleatoire1, aleatoire2]


def mouvement(rectangle):
   global after_balle
   for i in range(len(rectangle)):
       canvas.move(rectangle[i][0][0], rectangle[i][0][1], rectangle[i][0][2])
       rebond1(rectangle, i)
   after_balle = canvas.after(20, lambda: mouvement(rectangle))


def rebond1(rectangle, i):

   x0, y0, x1, y1 = canvas.coords(rectangle[i][0][0])

   if x0 <= rectangle[i][1] or x1 >= rectangle[i][3]:
       rectangle[i][0][1] = -rectangle[i][0][1]

   if y0 <= rectangle[i][2] or y1 >= rectangle[i][4]:
       rectangle[i][0][2] = -rectangle[i][0][2]


racine = tk.Tk()

canvas = tk.Canvas(racine, width=600, height=400, bg="black")
canvas.grid(row=0)

rectangle = quadrillage(n, m)

bouton = tk.Button(racine, text="Démarrer", command=lambda: demarrer(rectangle))
bouton.grid(row=1)


racine.mainloop()

