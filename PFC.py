import pygame
import sys
import random
import time

class PFC:

    def __init__(self):
        self.ecran = pygame.display.set_mode((1000,600))
        pygame.display.set_caption('Jeu Pierre-Feuille-Ciseaux par Karis')
        self.choix = ''
        self.PFC = ['Pierres', 'Feuilles', 'Ciseaux']
        self.ordinateur = ''
        self.scorejoueur = 0
        self.scoreordinateur = 0
        self.affichage_debut = True

    #Création de message texte
    def creer_message(self, font, message, message_rectangle, couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20,
                                       False)  # pour choisir la police, la taille, et si on met en gras ou non
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, True)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)  # True pour que ce soit un texte en gras
        elif font == 'minuscule':
            font = pygame.font.SysFont('Lato', 10, True)

        message = font.render(message, True, couleur)  # cette fonction sert à créer l'objet texte
        self.ecran.blit(message,message_rectangle)  # message_rectangle correspond à la position (x,y) de mon message





    def qui_gagne(self):
        # Savoir qui a gagné
        if (self.choix == 'Ciseaux' and self.ordinateur == 'Pierres'):
            self.scoreordinateur += 1
        elif (self.choix == 'Pierres' and self.ordinateur == 'Ciseaux'):
            self.scorejoueur += 1
        elif (self.choix == 'Papier' and self.ordinateur == 'Pierres'):
            self.scorejoueur += 1
        elif (self.choix == 'Pierres' and self.ordinateur == 'Papier'):
            self.scoreordinateur += 1
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Ciseaux'):
            self.scoreordinateur += 1
        elif (self.choix == 'Ciseaux' and self.ordinateur == 'Feuilles'):
            self.scorejoueur += 1
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Pierres'):
            self.scorejoueur += 1
        elif (self.choix == 'Pierres' and self.ordinateur == 'Feuilles'):
            self.scoreordinateur += 1
        elif (self.choix == 'Pierres' and self.ordinateur == 'Pierres'):
            self.creer_message('moyenne', 'Egalité',
                               (400, 200, 90, 50), (255, 255, 255))
            self.scoreordinateur += 0
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Feuilles'):
            self.creer_message('moyenne', 'Egalité',
                               (400, 200, 90, 50), (255, 255, 255))
            self.scoreordinateur += 0
        elif (self.choix == 'Ciseaux' and self.ordinateur == 'Ciseaux'):
            self.creer_message('moyenne', 'Egalité',
                               (400, 200, 90, 50), (255, 255, 255))
            self.scoreordinateur += 0

    def affiche_resultat(self):
        if (self.choix == 'Ciseaux' and self.ordinateur == 'Pierres'):
            self.creer_message('moyenne', 'Perdu ! Point pour Isabelle',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Pierres' and self.ordinateur == 'Ciseaux'):
            self.creer_message('moyenne', 'Gagné, point pour vous !',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Papier' and self.ordinateur == 'Pierres'):
            self.creer_message('moyenne', 'Gagné, point pour vous !',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Pierres' and self.ordinateur == 'Papier'):
            self.creer_message('moyenne', 'Perdu ! Point pour Isabelle',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Ciseaux'):
            self.creer_message('moyenne', 'Perdu ! Point pour Isabelle',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Ciseaux' and self.ordinateur == 'Feuilles'):
            self.creer_message('moyenne', 'Gagné, point pour vous !',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Pierres'):
            self.creer_message('moyenne', 'Gagné, point pour vous !',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Pierres' and self.ordinateur == 'Feuilles'):
            self.creer_message('moyenne', 'Perdu ! Point pour Isabelle',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Pierres' and self.ordinateur == 'Pierres'):
            self.creer_message('moyenne', 'Egalité',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Feuilles' and self.ordinateur == 'Feuilles'):
            self.creer_message('moyenne', 'Egalité',
                               (480, 250, 90, 50), (255, 255, 255))
        elif (self.choix == 'Ciseaux' and self.ordinateur == 'Ciseaux'):
            self.creer_message('moyenne', 'Egalité',
                               (480, 250, 90, 50), (255, 255, 255))


    def fonction_principale(self):
        Encours = True

        #Choix possibles

        #Ciseaux
        ciseaux = pygame.image.load('images/ciseaux.png').convert()
        ciseauxrect = ciseaux.get_rect(midleft = self.ecran.get_rect().center) #prends la position du milieu de l'écran, la mets dans "midleft" car get_rect() ne prend que des mots-clés
        ciseauxrect.x += 180 #midleft est le milieu gauche donc on rajoute 75 pour mettre à droite
        ciseauxrect.y += 190

        #Feuilles
        feuilles = pygame.image.load('images/feuilles.png').convert()
        feuillesrect = feuilles.get_rect(center = self.ecran.get_rect().center) #coordonnées du centre de la page
        feuillesrect.y += 190

        #Pierres
        pierres = pygame.image.load('images/pierres.png').convert()
        pierresrect = pierres.get_rect(midright = self.ecran.get_rect().center)
        pierresrect.x -= 180
        pierresrect.y += 200

        #Visage femme
        femmeemoji = pygame.image.load('images/femmeemoji.png')

        while self.affichage_debut:  #while loop pour faire l'affichage du début
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN: #si le joueur appuie sur la touche Entrée pour jouer
                        self.affichage_debut = False
                self.ecran.fill((0,0,0))

                #Ecran d'accueil et explication du jeu
                imageaccueil = pygame.image.load('images/PFC.png').convert()
                self.ecran.blit(imageaccueil,(350,100))
                self.creer_message('petite', 'Ce jeu est basé sur le principe du pierre-feuille-ciseaux', (320, 350, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Il faut gagner 3 fois contre Isabelle ',
                                   (380, 370, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Vous devez cliquer sur les images pour choisir votre coup',
                                   (290, 390, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Appuyez sur votre touche ENTREE pour commencer !', (300, 480, 200, 5), (255, 255, 255))
                self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (360,550,200,5), (255,255,255))

                pygame.display.flip()

        scorejoueur = 0
        scoreordinateur = 0
        #ordinateur = random.choice(PFC)
        while self.scorejoueur < 3 and self.scoreordinateur < 3:  # tant que la fenêtre sera ouverte
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()

                #Sélection du joueur
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if ciseauxrect.collidepoint(position): #s'il y a collision, càd si les coordonnées de l'image des ciseaux = celle de là où à lieu le clic
                        self.choix = 'Ciseaux'
                        self.ordinateur = random.choice(self.PFC)
                        self.qui_gagne()
                    elif feuillesrect.collidepoint(position):
                        self.choix = 'Feuilles'
                        self.ordinateur = random.choice(self.PFC)
                        self.qui_gagne()
                    elif pierresrect.collidepoint(position):
                        self.choix = 'Pierres'
                        self.ordinateur = random.choice(self.PFC)
                        self.qui_gagne()

            if self.scorejoueur == 3:
                return True
            if self.scoreordinateur == 3:
                return False


            # Afficher les images
            self.ecran.fill((0, 0, 0))
            self.ecran.blit(femmeemoji, (240, 30))
            if self.choix != '':
                self.creer_message('moyenne','Isabelle ouvre sa main et montre : ' + self.ordinateur + ' !', (450, 150, 90, 50), (255, 255, 255))
            else:
                self.creer_message('moyenne', 'Isabelle ouvre sa main et montre : rien !', (450, 150, 90, 50), (255, 255, 255))

            #Affiche le score
            self.creer_message('moyenne','Votre score est de ' + str(self.scorejoueur) + ' et celui de l ordinateur est de ' + str(self.scoreordinateur) + ' !',
                               (250, 330, 90, 50), (255, 255, 255))
            self.affiche_resultat()
            self.ecran.blit(ciseaux, (ciseauxrect))  # on colle l'image ciseaux à la position ciseauxrect
            self.ecran.blit(feuilles, (feuillesrect))
            self.ecran.blit(pierres, (pierresrect))

            pygame.display.flip()