
# On notera :
#      " b_ " pour l'affichage de boutons
#      " l_ " ou " l " pour l'affichage de labels (messages)



#--------------Import---------------------------------

import tkinter as tk
from tkinter import filedialog as fd
import os.path
from tkinter.filedialog import askopenfilename



#----------CREATION BARRE DE MENU-----------------

def bar_menu():
    menu_bar = tk.Menu()

    def openFile():
        file = askopenfilename(title="Choisir un fichier à ouvrir")
        filetypes = [("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")]
        print(file)

    menu1 = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_command(label="Ouvrir", command=openFile)
    menu1.add_separator()
    menu_bar.add_command(label="Quitter", command=quit)
    root.config(menu=menu_bar)


#-----------CREATION PAGE EDITION----------------------

def menu_edition():
    lobby_edition = tk.Tk()
    lobby_edition.title("Lobby édition")
    lobby_edition.minsize(1000, 650)
    lobby_edition.config(background="#A3E4D7")

    l1 = tk.Label(lobby_edition, text="Que voulez-vous faire ?", font=("Courrier", 20), bg="#D1F2EB", fg="black")
    l1.place(relx=0.330, rely=0.050, relwidth=0.35, relheight=0.08)

    b_texte = tk.Button(lobby_edition, text="Texte", width=10, font=("Courrier", 20), bg='#16A085', fg='white', command=lambda: [lobby_edition.quit, menu_texte()])
    b_texte.place(relx=0.350, rely=0.400, relwidth=0.3, relheight=0.08)

    b_objet = tk.Button(lobby_edition, text="Objet", width=10, font=("Courrier", 20), bg='#16A085', fg='white', command=lambda: [lobby_edition.quit, menu_objet()])
    b_objet.place(relx=0.350, rely=0.650, relwidth=0.3, relheight=0.08)

    b_retour1 = tk.Button(lobby_edition, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_edition.destroy()])
    b_retour1.place(relx=0.870, rely=0.010, relwidth=0.12, relheight=0.07)




#-----Edition------CREATION PAGE TEXTE----------------------

def menu_texte():
    lobby_texte = tk.Tk()
    lobby_texte.title("Lobby texte")
    lobby_texte.minsize(1000, 650)
    lobby_texte.config(background="#A3E4D7")

    l_titre = tk.Label(lobby_texte, text="Titre", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    l_titre.place(relx=0.450, rely=0.050, relwidth=0.1, relheight=0.07)

    titre = tk.Text(lobby_texte,font=("Courrier", 20), bg="#AED6F1", fg="black")
    titre.place(relx=0.100, rely=0.150, relwidth=0.8, relheight=0.07)

    l_texte = tk.Label(lobby_texte, text="Texte", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    l_texte.place(relx=0.450, rely=0.250, relwidth=0.1, relheight=0.07)

    texte = tk.Text(lobby_texte, font=("Courrier", 20), bg="#AED6F1", fg="black")
    texte.place(relx=0.100, rely=0.350, relwidth=0.8, relheight=0.5)

    b_retour2 = tk.Button(lobby_texte, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_texte.destroy()])
    b_retour2.place(relx=0.870, rely=0.010, relwidth=0.12, relheight=0.07)

    def save1():
        save_texte = os.path.join(f"{titre.get('1.0', 'end-1c')}.txt")
        txt = open(save_texte, "a+")
        txt.write(texte.get('1.0', 'end-1c'))
        txt.close()

    b_enregistrer1 = tk.Button(lobby_texte, text="Enregistrer", width=10, font="Courrier", bg='#16A085', fg='white', command=save1())
    b_enregistrer1.place(relx=0.450, rely=0.900, relwidth=0.12, relheight=0.07)



#-----Edition------CREATION PAGE OBJET----------------------

def menu_objet():
    lobby_objet = tk.Tk()
    lobby_objet.title("Lobby objet")
    lobby_objet.minsize(1000, 750)
    lobby_objet.config(background="#A3E4D7")

    l_objet1 = tk.Label(lobby_objet,text="Créez vos objets \n",font=("Courrier", 15), bg="#D1F2EB", fg="black")
    l_objet1.place(relx=0.360, rely=0.050, relwidth=0.25, relheight=0.07)

    l_nom = tk.Label(lobby_objet, text="Nom de l'objet :\n", font=("Courrier", 15), bg="#D1F2EB", fg="black")
    l_nom.place(relx=0.100, rely=0.280, relwidth=0.2, relheight=0.07)

    nom = tk.Text(lobby_objet, font=("Courrier", 15), bg="#AED6F1", fg="black", width=7, height=1)
    nom.place(relx=0.350, rely=0.280, relwidth=0.25, relheight=0.07)

    b_enregistrer2 = tk.Button(lobby_objet, text="Enregistrer", width=10, font=("Courrier", 15), bg='#16A085', fg='white')
    b_enregistrer2.place(relx=0.700, rely=0.280, relwidth=0.12, relheight=0.07)

    b_retour3 = tk.Button(lobby_objet, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_objet.destroy()])
    b_retour3.place(relx=0.870, rely=0.010, relwidth=0.12, relheight=0.07)

    b_cara = tk.Button(lobby_objet, text="Caractéristiques de l'objet", font=("Courrier", 18), bg='#16A085', fg='white', command=lambda: [lobby_objet.quit, scale1()])
    b_cara.place(relx=0.100, rely=0.480, relwidth=0.3, relheight=0.07)


# Création d'une scale pour gérer la puissance de l'objet :

def scale1():
    lobby_scale = tk.Tk()
    lobby_scale.title("Caractéristiques")
    lobby_scale.geometry('500x300')
    lobby_scale.config(background="#AED6F1")

    l_puissance = tk.Label(lobby_scale, bg='#D6EAF8', fg='black', font=("Courrier", 15), text='Puissance')
    l_puissance.place(relx=0.350, rely=0.050, relwidth=0.3, relheight=0.1)


    def print_selection(v):
        l_puissance.config(text='Vos dégâts : ' + v)

    scale = tk.Scale(lobby_scale, label='Bougez le joystick', from_=0, to=10, orient=tk.HORIZONTAL, length=400, showvalue=0, tickinterval=2,
                 resolution=0.01, command=print_selection)
    scale.place(relx=0.200, rely=0.300, relwidth=0.6, relheight=0.25)

    b_enregistrer3 = tk.Button(lobby_scale, text="Enregistrer", width=10, font="Courrier", bg='#5499C7', fg='white')
    b_enregistrer3.place(relx=0.350, rely=0.700, relwidth=0.3, relheight=0.1)

    lobby_scale.mainloop()



#-----Jeu------Création de la page de jeu-----------------------

def menu_jeu():
    lobby_jeu = tk.Tk()
    lobby_jeu.title("Lobby")
    lobby_jeu.minsize(1000, 650)
    lobby_jeu.config(background="#A3E4D7")
    b_retour4 = tk.Button(lobby_jeu, text="Retour", width=10, font="Courrier", bg='white', fg='red', command=lambda: [lobby_jeu.destroy()])
    b_retour4.place(relx=0.870, rely=0.010, relwidth=0.12, relheight=0.07)



#-----Accueil------CREATION PAGE D'ACCUEIL-----------------------

def page_accueil():
    global root
    root = tk.Tk()
    root.geometry("1000x650")
    root.title("Écran de démarrage")
    root.iconbitmap("...")  # icone de la fenêtre
    root.config(background="#AED6F1")  # choisir un code couleur hexadecimal (rouge : #FF0000 / bleu : #0000FF / rose : #FFC0CB)
    root.resizable(width=True, height=True)  # autorisation de modification de la taille de la fenêtre

    l2 = tk.Label(root, text="Bienvenue dans la partie !\n Vous êtes prêts ?", font=("Courrier", 20), bg="#D6EAF8", fg="black")
    l2.place(relx=0.350, rely=0.050, relwidth=0.35, relheight=0.2)

    b_editer = tk.Button(root, text="Editer", width=10,font="Courrier 20", bg='#5499C7', fg='white', command=lambda: [root.quit, menu_edition()])
    b_editer.place(relx=0.270, rely=0.400, relwidth=0.2, relheight=0.1)

    b_jouer = tk.Button(root, text="Jouer", width=10,font="Courrier 20", bg='#5499C7', fg='white', command=lambda: [root.quit, menu_jeu()])
    b_jouer.place(relx=0.570, rely=0.400, relwidth=0.2, relheight=0.1)

    b_quitter = tk.Button(root, text="Quitter", width=10,font="Courrier", bg='white', fg='red', command=quit)
    b_quitter.place(relx=0.450, rely=0.800,  relwidth=0.15, relheight=0.07)

    bar_menu()


page_accueil()

root.mainloop()
