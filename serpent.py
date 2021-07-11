import sys,random
import pygame, pygame.mixer

class JeuDuSerpent: #contient toutes les variables et les fonctions utiles pour le déroulement du jeu

    def __init__(self):
        self.ecran = pygame.display.set_mode((1000, 600)) #ce sera ma fenêtre
        pygame.display.set_caption('Jeu du Snake par Karis')
        self.Encours = True
        self.affichage_debut = True

        #mouvement du joueur

        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.direction_x = 0
        self.direction_y = 0
        self.serpent_corps = 20

        #la pomme qui va apparaître au hasard
        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,490,10)

        #taille pomme
        self.pomme_taille = 20
        #fixer les fps
        self.clock = pygame.time.Clock()

        #on crée une liste pour les positions du serpent
        self.position_serpent = []

        #variable en rapport avec la taille du serpent
        self.taille_du_serpent = 1

    def fonction_principale(self):
        while self.affichage_debut:  #while loop pour faire l'affichage du début
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN: #si le joueur appuie sur la touche Entrée pour jouer
                        self.affichage_debut = False
                self.ecran.fill((0,0,0))

                #Ecran d'accueil et explication du jeu
                imageaccueil = pygame.image.load('images/imagesnake.png').convert()
                self.ecran.blit(imageaccueil,(300,100))
                self.creer_message('petite', 'Ce jeu est basé sur le jeu du serpent', (360, 350, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Il faut ramasser 5 pommes pour gagner. Vous perdez si vous sortez des limites ou si vous mangez votre queue',
                                   (150, 370, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Vous vous déplacez avec les flèches du clavier, haut/bas/gauche/droite',
                                   (250, 390, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Appuyez sur votre touche ENTREE pour commencer !', (300, 480, 200, 5), (255, 255, 255))
                self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (360,550,200,5), (255,255,255))

                pygame.display.flip()

        son = pygame.mixer.Sound('son.wav')
        #permet de gérer les évènements, d'afficher certains composants du jeu grâce au while loop
        while self.Encours:
            son.play()
            for evenement in pygame.event.get():  #pour chaque évènement sur le jeu
                if evenement.type == pygame.QUIT:  #si jamais on ferme la fenêtre
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:  #cette partie sert juste à savoir où va bouger le serpent
                    if evenement.key == pygame.K_RIGHT:
                        self.direction_x = 10
                        self.direction_y = 0
                    if evenement.key == pygame.K_LEFT:
                        self.direction_x = -10
                        self.direction_y = 0
                    if evenement.key == pygame.K_UP:
                        self.direction_y = -10
                        self.direction_x = 0
                    if evenement.key == pygame.K_DOWN:
                        self.direction_y = 10
                        self.direction_x = 0
                    #print("SX:", self.serpent_position_x, "SY:", self.serpent_position_x, "PX:", self.pomme_position_x, "PY:", self.pomme_position_y)

            #pour pas qu'il dépasse les limites
            if self.serpent_position_x <= 90 or self.serpent_position_x >= 690 or self.serpent_position_y <= 90 or self.serpent_position_y >= 590:
                son.stop()
                return False


            self.serpent_mouvement()
            #si le serpent mange la pomme
            if self.serpent_position_x == self.pomme_position_x and self.serpent_position_y == self.pomme_position_y:

                self.pomme_position_x = random.randrange(110, 600, 10)
                self.pomme_position_y = random.randrange(110, 500, 10)
                self.taille_du_serpent+=1
                if self.taille_du_serpent > 5:
                    son.stop()
                    return True


            #on crée une liste qui stocke la position de la tête du serpent
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            #on la met dans la liste des positions du serpent
            self.position_serpent.append(la_tete_du_serpent)



            #pour résoudre les problèmes des positions avec la taille du serpent
            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)
                #print(self.position_serpent)

            self.afficher_les_elements()
            semord = self.se_mord(la_tete_du_serpent)
            if semord == False:
                son.stop()
                return False

            self.creer_message('moyenne', 'Votre score est de : ' + str(self.taille_du_serpent-1) + ' !',
                               (390, 10, 100, 50), (255, 255, 255))
            if self.taille_du_serpent > 4:
                self.creer_message('moyenne', 'Encore une !',
                                   (390, 30, 100, 50), (255, 255, 255))


            #cadre blanc
            pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

            #fps
            self.clock.tick(30)
            pygame.display.flip()  #mettre à jour le fond d'écran

    def serpent_mouvement(self):
        self.serpent_position_x += self.direction_x
        self.serpent_position_y += self.direction_y

    def afficher_les_elements(self):

        # mettre un fond noir
        self.ecran.fill((0, 0, 0))

        # afficher le serpent
        pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps,
                                                   self.serpent_corps))  # carré vert qui rpz le serpent
        self.afficher_serpent()

    def afficher_serpent(self):
        #et le reste de son corps
        for partie_du_serpent in self.position_serpent:
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

        # afficher la pomme
        pygame.draw.rect(self.ecran, (255, 0, 0),
                         (self.pomme_position_x, self.pomme_position_y, self.pomme_taille, self.pomme_taille))


    def se_mord(self,la_tete_du_serpent):
        for partie_serpent in self.position_serpent[:-1]:
            if partie_serpent == la_tete_du_serpent:
                return False


    def creer_message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20, False) #pour choisir la police, la taille, et si on met en gras ou non
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True) #True pour que ce soit un texte en gras
        elif font == 'minuscule':
            font = pygame.font.SysFont('Lato', 10, True)

        message = font.render(message,True,couleur) #cette fonction sert à créer l'objet texte
        self.ecran.blit(message,message_rectangle) #message_rectangle correspond à la position (x,y) de mon message