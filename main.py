
#--------------Import---------------------------------

import tkinter as tk
from tkinter import filedialog as fd
import os.path
from tkinter.filedialog import askopenfilename

#----------Création de la bar de menu-----------------


def bar_menu():
    menubar = tk.Menu()

    def openFile():
        file = askopenfilename(title="Choisir un fichier à ouvrir")
        filetypes = [("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")]
        print(file)

    menu1 = tk.Menu(menubar, tearoff=0)
    menubar.add_command(label="Ouvrir", command=openFile)
    menu1.add_separator()
    menubar.add_command(label="Quitter", command=quit)
    root.config(menu=menubar)


#-----------Menu----------------------

def scale1():
    lobby_scale = tk.Tk()
    lobby_scale.title("Caractéristiques")
    lobby_scale.geometry('500x300')
    lobby_scale.config(background="#AED6F1")

    l = tk.Label(lobby_scale, bg='#D6EAF8', fg='black', font=("Courrier", 15), text='Puissance')
    l.place(relx=0.300, rely=0.050, width=200, height=50)

    def print_selection(v):
        l.config(text='Vos dégâts : ' + v)

    s = tk.Scale(lobby_scale, label='Bougez le joystick', from_=0, to=10, orient=tk.HORIZONTAL, length=400, showvalue=0, tickinterval=2,
                 resolution=0.01, command=print_selection)
    s.place(relx=0.100, rely=0.300)

    bouton8 = tk.Button(lobby_scale, text="Enregistrer", width=10, font="Courrier", bg='#5499C7', fg='white')
    bouton8.place(relx=0.380, rely=0.700)

    lobby_scale.mainloop()


def menu_objet():
    lobby_objet = tk.Tk()
    lobby_objet.title("Lobby objet")
    lobby_objet.minsize(1000, 750)
    lobby_objet.config(background="#A3E4D7")

    texte3 = tk.Label(lobby_objet,text="Créez vos objets \n",font=("Courrier", 15), bg="#D1F2EB", fg="black")
    texte3.place(relx=0.360, rely=0.050, width=300, height=50)

    texte = tk.Text(lobby_objet, font=("Courrier", 15), bg="#AED6F1", fg="black", width=7, height=1)
    texte.place(relx=0.350, rely=0.280, width=300, height=40)

    texte4 = tk.Label(lobby_objet, text="Nom de l'objet :\n", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    texte4.place(relx=0.100, rely=0.280, width=200, height=40)

    bouton6 = tk.Button(lobby_objet, text="Enregistrer", width=10, font=("Courrier", 15), bg='#16A085', fg='white')
    bouton6.place(relx=0.700, rely=0.280, width=150, height=45)

    bouton6bis = tk.Button(lobby_objet, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_objet.destroy()])
    bouton6bis.place(relx=0.870, rely=0.010)

    bouton7 = tk.Button(lobby_objet, text="Caractéristiques de l'objet", font=("Courrier", 18), bg='#16A085', fg='white', command=lambda: [lobby_objet.quit, scale1()])
    bouton7.place(relx=0.100, rely=0.480, width=400, height=50)

def menu_edition():
    lobby_edition = tk.Tk()
    lobby_edition.title("Lobby édition")
    lobby_edition.minsize(1000, 650)
    lobby_edition.config(background="#A3E4D7")

    texte5 = tk.Label(lobby_edition, text="Que voulez-vous faire ?", font=("Courrier", 20), bg="#D1F2EB", fg="black")
    texte5.place(relx=0.330, rely=0.050, width=350, height=80)

    bouton8 = tk.Button(lobby_edition, text="Texte", width=10, font=("Courrier", 20), bg='#16A085', fg='white', command=lambda: [lobby_edition.quit, menu_texte()])
    bouton8.place(relx=0.350, rely=0.400, width=300, height=50)

    bouton9 = tk.Button(lobby_edition, text="Objet", width=10, font=("Courrier", 20), bg='#16A085', fg='white', command=lambda: [lobby_edition.quit, menu_objet()])
    bouton9.place(relx=0.350, rely=0.650, width=300, height=50)

    bouton10 = tk.Button(lobby_edition, text="Retour", width=10, font="Courrier", bg='white', fg='red',
                        command=lambda: [lobby_edition.destroy()])
    bouton10.place(relx=0.870, rely=0.010)


def menu_texte():
    lobby_texte = tk.Tk()
    lobby_texte.title("Lobby texte")
    lobby_texte.minsize(1000, 650)
    lobby_texte.config(background="#A3E4D7")

    texte0 = tk.Label(lobby_texte, text="Titre", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    texte0.place(relx=0.450, rely=0.050, width=100, height=40)

    titre0 = tk.Text(lobby_texte,font=("Courrier", 20), bg="#AED6F1", fg="black")
    titre0.place(relx=0.100, rely=0.150, width=800, height=50)

    texte2 = tk.Label(lobby_texte, text="Texte", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    texte2.place(relx=0.450, rely=0.250, width=100, height=40)

    texte1 = tk.Text(lobby_texte, font=("Courrier", 20), bg="#AED6F1", fg="black")
    texte1.place(relx=0.100, rely=0.350, width=800, height=330)

    def save1():
        texte = os.path.join(f"{titre0.get('1.0', 'end-1c')}.txt")
        txt = open(texte, "a+")
        txt.write(texte1.get('1.0', 'end-1c'))
        txt.close()

    bouton3 = tk.Button(lobby_texte, text="Enregistrer", width=10, font="Courrier", bg='#16A085', fg='white', command=save1())
    bouton3.place(relx=0.450, rely=0.900)

    bouton4 = tk.Button(lobby_texte, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_texte.destroy()])
    bouton4.place(relx=0.870, rely=0.010)


def menu_jeu():
    lobby_jeu = tk.Tk()
    lobby_jeu.title("Lobby")
    lobby_jeu.minsize(1000, 650)
    lobby_jeu.config(background="#A3E4D7")
    bouton4bis = tk.Button(lobby_jeu, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_jeu.destroy()])
    bouton4bis.place(relx=0.870, rely=0.010)

#-----------Création de la page-----------------------


def page_accueil():
    global root
    root = tk.Tk()
    root.geometry("1000x650")
    root.title("Écran de démarrage")
    root.iconbitmap("...")  # icone de la fenêtre
    root.config(background="#AED6F1")  # choisir un code couleur hexadecimal (rouge : #FF0000 / bleu : #0000FF / rose : #FFC0CB)
    root.resizable(width=True, height=True)  # autorisation de modification de la taille de la fenêtre

    texte1 = tk.Label(root, text="Bienvenue dans la partie !\n Vous êtes prêts ?", font=("Courrier", 20), bg="#D6EAF8", fg="black")
    texte1.place(relx=0.330, rely=0.050, width=400, height=100)

    bouton1 = tk.Button(root, text="Editer", width=10,font="Courrier 20", bg='#5499C7', fg='white', command=lambda: [root.quit, menu_edition()])
    bouton1.place(relx=0.300, rely=0.400)

    bouton1bis = tk.Button(root, text="Jouer", width=10,font="Courrier 20", bg='#5499C7', fg='white', command=lambda: [root.quit, menu_jeu()])
    bouton1bis.place(relx=0.570, rely=0.400)

    bouton2 = tk.Button(root, text="Quitter", width=10,font="Courrier", bg='white', fg='red', command=quit)
    bouton2.place(relx=0.450, rely=0.800)

    bar_menu()


page_accueil()

root.mainloop()