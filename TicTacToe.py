import pygame
import sys
import random

class Grille:
    def __init__(self,ecran):
        self.lignes = [( (200,0), (200,600) ), #(200,0) point de départ de la 1ere ligne, (200,600) point de fin de la 1ere ligne
                       ( (400,0),(400,600) ),
                       ( (0,200),(600,200) ),
                        ( (0,400),(600,400))]
        self.ecran = ecran

        #on initie la grille
        self.grille = [[None for x in range(0,3)] for y in range(0,3)] #tableau 2D qui contient nos X et Y

    def afficher_lignes(self):
        for lignes in self.lignes:

            pygame.draw.line(self.ecran,(255,255,255),lignes[0],lignes[1],2)

        #Afficher les x et y:
        for y in range(0,len(self.grille)):
            for x in range(0,len(self.grille)):
                if self.grille[y][x] == 'X':
                    pygame.draw.line(self.ecran,(0,255,0),(x * 200,y * 200),(200 + ( x * 200),200 + (y*200)),3)#1ere barre
                    pygame.draw.line(self.ecran,(0,255,0),((x * 200), 200 + (y * 200 )),(200 +( x * 200),( y * 200)),3)#2eme barre
                elif self.grille[y][x] == 'O':
                    pygame.draw.circle(self.ecran,(255,0,0),(100 + (x * 200), 100 + (y * 200)),100,3)

    #afficher la grille
    def print_grille(self):
        print(self.grille)

    #on fixe les valeurs
    def fixer_la_valeur(self,x,y,valeur):
        if self.grille[y][x] == None:
            self.grille[y][x] = valeur
            return True

    def fixer_None(self,ligne,colonne,valeur):

        self.grille[ligne][colonne] = valeur

class JeuTicTacToe:
    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Jeu du Tic Tac Toe par Karis')
        self.Encours = True
        self.grille = Grille(self.ecran)
        self.joueur = 'X'
        self.ordinateur=  'O'
        #on fixe le compteur
        self.compteur = 0

        #voir si c'est occupé ou non
        self.pasoccupe = False
        self.affichage_debut = True

    # Création de message texte
    def creer_message(self, font, message, message_rectangle, couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)  # pour choisir la police, la taille, et si on met en gras ou non
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, True)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)  # True pour que ce soit un texte en gras
        elif font == 'minuscule':
            font = pygame.font.SysFont('Lato', 10, True)

        message = font.render(message, True, couleur)  # cette fonction sert à créer l'objet texte
        self.ecran.blit(message,
                        message_rectangle)  # message_rectangle correspond à la position (x,y) de mon message


    def recommencer(self):
        for ligne in range(0,len(self.grille.grille)):
            for colonne in range(0,len(self.grille.grille)):
                self.grille.fixer_None(ligne,colonne,None)



    def fonction_principale(self):
        #Logo
        logo = pygame.image.load('images/TicTacToe.png')
        self.ecran = pygame.display.set_mode((1000, 600))
        while self.affichage_debut:  #while loop pour faire l'affichage du début
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN: #si le joueur appuie sur la touche Entrée pour jouer
                        self.affichage_debut = False
                self.ecran.fill((0,0,0))

                #Ecran d'accueil et explication du jeu
                self.ecran.blit(logo,(350,100))
                self.creer_message('petite', 'Ce mini-jeu est basé sur le principe du Tic Tac Toe', (320, 310, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Il faut aligner 3 croix à l horizontale, verticale, ou diagonale', (280, 340, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Il faut appuyer sur le clic gauche de votre souris pour placer votre pion', (280, 360, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Appuyez sur votre touche ENTREE pour commencer !', (300, 480, 200, 5), (255, 255, 255))
                self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (360,550,200,5), (255,255,255))

                pygame.display.flip()

        self.ecran = pygame.display.set_mode((600, 600))
        while self.Encours:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                elif evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_SPACE:
                        self.recommencer()
                #on ajoute l'évènement qui correspond au clic gauche
                elif evenement.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    #position de la souris
                    position = pygame.mouse.get_pos() #position de la souris (x,y)
                    position_x, position_y = position[0]//200, position[1]//200 #on prend la position[0] et on la divise par 200
                                                                                # et on prend la partie entière, et la mettre dans position_x
                    #print(position)
                    #print(position_x,position_y)
                    #si compteur pair, l'utilisateur joue, sinon non
                    if self.compteur%2 == 0:
                        self.pasoccupe = self.grille.fixer_la_valeur(position_x, position_y, self.joueur) #on met le pion du joueur et on l'affiche
            if self.compteur%2 == 1: #si c'est le tour de l'ordinateur
                    position_x = random.randint(0, 2) #on prend sa position x
                    position_y = random.randint(0, 2) #on prend sa position y
                    self.pasoccupe = self.grille.fixer_la_valeur(position_x, position_y, self.ordinateur) #on met son pion dans la grille
            if self.pasoccupe:
                self.compteur += 1
                self.pasoccupe = False

                #self.grille.print_grille() #afficher ma liste qui contient des listes qui contient des valeurs (pour X et O)
                liste_X = []
                liste_O = []

                for ligne in range(0,len(self.grille.grille)):
                    for colonne in range(0,len(self.grille.grille)):

                        if self.grille.grille[ligne][colonne] == 'X': #Si on retrouve un X dans la liste
                            X_position = (ligne,colonne) #on stocke sa position
                            liste_X.append(X_position) #et on l'ajoute dans la liste qui contient tous les X
                        elif self.grille.grille[ligne][colonne] == 'O':
                            O_position = (ligne,colonne)
                            liste_O.append(O_position)


                if len(liste_X) >= 3: #si il y a plus de 3 X dans le jeu
                    # test verticale     # si dans la liste liste_lignes_X, il y a 3 valeurs 0 ( donc la 1ere ligne ) ou 3 valeurs 1 ( donc 2eme ligne.. )
                    if self.grille.grille[0][0] == self.grille.grille[0][1] and self.grille.grille[0][1] == self.grille.grille[0][2] and self.grille.grille[0][2] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    if self.grille.grille[1][0] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[1][2] and self.grille.grille[1][2] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    if self.grille.grille[2][0] == self.grille.grille[2][1] and self.grille.grille[2][1] == self.grille.grille[2][2] and self.grille.grille[2][2] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    # test horizontale mais c'est liste_colonnes car c'est inversé
                    if self.grille.grille[0][0] == self.grille.grille[1][0] and self.grille.grille[1][0] == self.grille.grille[2][0] and self.grille.grille[2][0] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    if self.grille.grille[0][1] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][1] and self.grille.grille[2][1] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    if self.grille.grille[0][2] == self.grille.grille[1][2] and self.grille.grille[1][2] == self.grille.grille[2][2] and  self.grille.grille[2][2] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    #test diagonale
                    if self.grille.grille[0][2] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][0] and self.grille.grille[2][0] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True
                    if self.grille.grille[0][0] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][2] and self.grille.grille[2][2] == 'X':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return True

#Pour les O
                if len(liste_O) >= 3:  # si il y a plus de 3 O dans le jeu
                    # test verticale
                    if self.grille.grille[0][0] == self.grille.grille[0][1] and self.grille.grille[0][1] == self.grille.grille[0][2] and self.grille.grille[0][2] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    if self.grille.grille[1][0] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[1][2] and self.grille.grille[1][2] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    if self.grille.grille[2][0] == self.grille.grille[2][1] and self.grille.grille[2][1] == self.grille.grille[2][2] and self.grille.grille[2][2] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    # test horizontale mais c'est liste_colonnes car c'est inversé
                    if self.grille.grille[0][0] == self.grille.grille[1][0] and self.grille.grille[1][0] == self.grille.grille[2][0] and self.grille.grille[2][0] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    if self.grille.grille[0][1] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][1] and self.grille.grille[2][1] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    if self.grille.grille[0][2] == self.grille.grille[1][2] and self.grille.grille[1][2] == self.grille.grille[2][2] and self.grille.grille[2][2] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    #test diagonale
                    if self.grille.grille[0][2] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][0] and self.grille.grille[2][0] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False
                    if self.grille.grille[0][0] == self.grille.grille[1][1] and self.grille.grille[1][1] == self.grille.grille[2][2] and self.grille.grille[2][2] == 'O':
                        self.ecran = pygame.display.set_mode((1000, 600))
                        return False


            self.ecran.fill((0, 0, 0))
            self.grille.afficher_lignes()  # pour afficher les lignes de la grille
            pygame.display.flip()