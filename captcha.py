import pygame
import sys

class Captcha:

    def __init__(self):
        self.ecran = pygame.display.set_mode((1000,600))
        pygame.display.set_caption('Jeu Captcha par Karis')
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


    def fonction_principale(self):
        Encours = True

        #Choix possibles

        #Enigma
        Enigma = pygame.image.load('images/Enigma.png').convert()
        Enigmarect = Enigma.get_rect(midleft = self.ecran.get_rect().center) #prends la position du milieu de l'écran, la mets dans "midleft" car get_rect() ne prend que des mots-clés
        Enigmarect.x += 180 #midleft est le milieu gauche donc on rajoute 75 pour mettre à droite
        Enigmarect.y += 160

        #Petites enigmes
        petitesenigmes = pygame.image.load('images/petitesenigmes.png').convert()
        petitesenigmesrect= petitesenigmes.get_rect(center = self.ecran.get_rect().center) #coordonnées du centre de la page
        petitesenigmesrect.x += 250
        petitesenigmesrect.y -= 100

        #Engin
        Engin = pygame.image.load('images/engin.png').convert()
        Enginrect = Engin.get_rect(midright = self.ecran.get_rect().center)
        Enginrect.x -= 60
        Enginrect.y += 170

        #Machine à écrire
        machineaecrire = pygame.image.load('images/machineaecrire.png').convert()
        machineaecrirerect = machineaecrire.get_rect(midright = self.ecran.get_rect().center)
        machineaecrirerect.x -= 130
        machineaecrirerect.y -= 100

        #Logo
        imagequestions = pygame.image.load('images/questions.png')

        while self.affichage_debut:  #while loop pour faire l'affichage du début
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN: #si le joueur appuie sur la touche Entrée pour jouer
                        self.affichage_debut = False
                self.ecran.fill((0,0,0))

                #Ecran d'accueil et explication du jeu
                self.ecran.blit(imagequestions,(350,100))
                self.creer_message('petite', 'Ce mini-jeu est basé sur le principe du captcha', (320, 350, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Il faut appuyer sur la bonne image', (360, 370, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Appuyez sur votre touche ENTREE pour commencer !', (300, 480, 200, 5), (255, 255, 255))
                self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (360,550,200,5), (255,255,255))

                pygame.display.flip()

        while Encours:  # tant que la fenêtre sera ouverte
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()

                #Sélection du joueur
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if Enigmarect.collidepoint(position): #s'il y a collision, càd si les coordonnées de l'image des ciseaux = celle de là où à lieu le clic
                        return True
                    elif petitesenigmesrect.collidepoint(position):
                        return False
                    elif Enginrect.collidepoint(position):
                        return False
                    elif machineaecrirerect.collidepoint(position):
                        return False

            # Afficher les images
            self.ecran.fill((0, 0, 0))
            self.creer_message('moyenne','Appuie sur la machine Enigma !', (320, 40, 90, 50), (255, 255, 255))
            self.ecran.blit(Enigma, (Enigmarect))  # on colle l'image ciseaux à la position ciseauxrect
            self.ecran.blit(petitesenigmes, (petitesenigmesrect))
            self.ecran.blit(Engin, (Enginrect))
            self.ecran.blit(machineaecrire, (machineaecrirerect))
            pygame.display.flip()