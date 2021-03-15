import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog


mat=[[0]*5 for k in range(3)]
print(mat)


def nbrCol(matrice):
    return(len(matrice[0]))


def nbrLig(matrice):
    return(len(matrice))


def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)


def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat


def filtre_vert():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j] = (0, mat[i][j][1], 0, 255)
    modify(mat)
    
            
def negatif():
    mat = loading(nomImgCourante)   
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j] = (255-mat[i][j][0], 255-mat[i][j][1], 255-mat[i][j][2], 255)
    modify(mat)


def symetrique():
    mat = loading(nomImgCourante)   
    matSym = [[(0, 0, 0, 0)] * nbrCol(mat) for k in range(nbrLig(mat))]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            matSym[i][nbrCol(mat)-1-j] = mat[i][j]
    modify(matSym)


def gris():
    mat = loading(nomImgCourante)
    teinte_gris = 0
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            teinte_gris = int(mat[i][j][0]*0.2125 + mat[i][j][1]*0.7154 + mat[i][j][2]*0.0721)
            mat[i][j] = (teinte_gris, teinte_gris, teinte_gris, 255)
    modify(mat)


create = True
nomImgCourante = ""


def charger():
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global racine
    filename = filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(racine, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)
        create = False    
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(racine, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)


def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"


def quitter():
    global racine
    racine.destroy()


racine = tk.Tk()

mon_canvas = tk.Canvas(racine, width=300, height=300, background="white")
mon_canvas.grid(row=0, column=1, rowspan=4)
racine.title("Mon petit Photoshop")

bouton_fitre_vert = tk.Button(racine, text="Filtre vert", command=filtre_vert)
bouton_fitre_vert.grid(row=0, column=0)

bouton_negatif = tk.Button(racine, text="Négatif", command=negatif)
bouton_negatif.grid(row=1, column=0)

bouton_symetrique = tk.Button(racine, text="Symétrique", command=symetrique)
bouton_symetrique.grid(row=2, column=0)

bouton_gris = tk.Button(racine, text="Gris", command=gris)
bouton_gris.grid(row=3, column=0)

bouton_charger = tk.Button(racine, text="Charger", command=charger)
bouton_charger.grid(row=4, column=0)

bouton_quitter = tk.Button(racine, text="Quitter", command=quitter)
bouton_quitter.grid(row=4, column=2)

nom = tk.Label(racine, text="VALBERT Julie, numéro étudiant 22001658")
nom.grid(row=4, column=1)

racine.mainloop()
