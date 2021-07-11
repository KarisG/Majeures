import pygame
import random
import sys
import re
from serpent import JeuDuSerpent
from formulaire import Formulaire
from PFC import PFC
from captcha import Captcha
from TicTacToe import JeuTicTacToe

class Jeu:
    def __init__(self):  #Constructeur

        #Ecran du début
        self.affichage_debut = True

        # Ma fenêtre
        self.longeur = 1000
        self.largeur = 600
        self.ecran = pygame.display.set_mode((self.longeur, self.largeur))  # ce sera ma fenêtre, sa résolution, et je stocke dans une variable "ecran"
        pygame.display.set_caption('Forum des majeurs par Karis')  # Nom du jeu

        #Creation du joueur
        self.joueur = Joueur()

        # Etat du jeu
        self.Encours = True  # la fenêtre est ouverte
        self.v = False

        #Score
        self.score = 0

    #Pour écrire dans une zone de texte
    def message_entree(self,action,nbrs):
        font = pygame.font.Font(None, 32)  # module des polices, pour avoir toutes les polices possible
        input_box = pygame.Rect(380, 380, 140, 32)
        color_inactive = pygame.Color('red')
        color_active = pygame.Color('white')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            if action < 5:
                imageaccueil = pygame.image.load('images/imageaccueil.png').convert()
            if action == 1:
                self.ecran.fill((0, 0, 0))
                self.ecran.blit(imageaccueil, (220, 20))
                self.creer_message('grande', 'Rentrez votre nom', (350, 330, 100, 50), (255, 255, 255))
            elif action == 2:
                self.ecran.fill((0, 0, 0))
                self.ecran.blit(imageaccueil, (220, 20))
                self.creer_message('grande', 'Rentrez votre prénom', (350, 330, 100, 50), (255, 255, 255))
            elif action == 3:
                self.ecran.fill((0, 0, 0))
                self.ecran.blit(imageaccueil, (220, 20))
                self.creer_message('grande', 'Rentrez votre classement', (310, 330, 100, 50), (255, 255, 255))
            elif action == 4:
                imagequestions = pygame.image.load('images/questions.png').convert()
                self.ecran.fill((0,0,0))
                self.ecran.blit(imagequestions, (320, 90))
                self.creer_message('grande', 'Combien vaut ' + nbrs[0] + ' * ' + nbrs[1] + ' ?', (300, 330, 100, 50), (255, 255, 255))
            elif action == 5:
                imagequestions = pygame.image.load('images/questions.png').convert()
                self.ecran.fill((0, 0, 0))
                self.ecran.blit(imagequestions, (270, 80))
                self.creer_message('grande', 'En quelle année a été créé le premier robot ?', (240, 320, 100, 50), (255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Si l'utilisateur clique sur la box.
                    if input_box.collidepoint(event.pos):
                        # Donc la boite devient active.
                        active = not active
                    else:
                        active = False
                    # On change la couleur actuelle de la box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN: #Si on appuie sur le bouton entrer
                            return text
                        if event.key == pygame.K_BACKSPACE:  # Si on efface des lettres
                            text = text[:-1] #mon texte prend la valeur du texte sans le dernier caractère
                            self.ecran.fill((0, 0, 0))
                        else:
                            text += event.unicode #caractères spéciaux et tout le reste

            # Pour créer le texte en cours.
            txt_surface = font.render(text, True, color)

            # Si le texte est trop long, alors la surface de la box va s'aggrandir.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width #on donne à la taille de l'entrée la taille nécessaire

            # Coller/Afficher le texte.

            self.ecran.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Coller/Afficher la box qui contient le texte.
            pygame.draw.rect(self.ecran, color, input_box, 2)

            #Copyright
            self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (380, 550, 200, 5), (255, 255, 255))

            pygame.display.flip()



    #Pour savoir les informations sur le joueur
    def informations_du_joueur(self):
        while self.joueur.nomjoueur=='' or type(self.joueur.nomjoueur) != str : #s'il ne rentre rien du tout ou qqch qui n'est pas un str
            self.joueur.nomjoueur = self.message_entree(1,None)
        while self.joueur.prenomjoueur=='' or type(self.joueur.prenomjoueur) != str:
            self.joueur.prenomjoueur = self.message_entree(2,None)
        while self.joueur.classementjoueur=='':
            self.joueur.classementjoueur = self.message_entree(3,None)
        self.joueur.classementjoueur = int(self.joueur.classementjoueur)



    #Pour avoir des calculs mentaux au hasard
    def calcul_au_hasard(self):

        nombre1 = random.randint(0,500)
        nombre2 = random.randint(0,500)
        resultat = nombre1 * nombre2
        nombre1 = str(nombre1)
        nombre2 = str(nombre2)
        nbrs = [nombre1,nombre2]
        reputilisateur = self.message_entree(4,nbrs)
        resultat = str(resultat) #car reputilisateur est considéré comme une chaine de caractere
        if reputilisateur == resultat:
            reponse=True
            self.score+=1
        else:
           reponse=False
        return reponse

    def questions(self):
        resultat = "1920"
        reputilisateur = self.message_entree(5,None)
        while reputilisateur == '':
            reputilisateur = self.message_entree(5, None)
        if resultat == reputilisateur:
            reponse = True
            self.score+=1
        else:
            reponse = False
        return reponse

    #Pour créer un message texte
    def creer_message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20, False) #pour choisir la police, la taille, et si on met en gras ou non
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40 , True) #True pour que ce soit un texte en gras

        message = font.render(message , True, couleur) #cette fonction sert à créer l'objet texte
        self.ecran.blit(message,message_rectangle) #message_rectangle correspond à la position (x,y) de mon message



    # Si le joueur arrive sur les cases blanches
    def joueur_sur_case_blanche(self,tab):
                    nbr = tab[0]
                    reponse = tab[1]
                    self.creer_message('moyenne','Votre score est de : '+str(self.score)+' !',(390,10,100,50),(255,255,255))
                    self.creer_message('moyenne', 'Joueur : '+self.joueur.nomjoueur+' '+self.joueur.prenomjoueur,(390, 40, 100, 50),
                                       (255, 255, 255))
                    self.creer_message('moyenne', 'Classement : ' + str(self.joueur.classementjoueur), (390, 60, 100, 50),
                                       (255, 255, 255))
                    if self.joueur.joueurposition_x == 50 and self.joueur.joueurposition_y == 100:
                            while reponse[0] == False:
                                self.ecran.fill((0,0,0))
                                reponse[0] = JeuDuSerpent().fonction_principale()
                                if reponse[0] == True:
                                    self.score+=1

                            #Si il a bien répondu
                            self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner', (290, 150, 100, 50), (255, 255, 255))
                            self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                               (290, 550, 100, 50), (255, 255, 255))
                            # Image pour afficher la zone de texte
                            if nbr == 1 or nbr == 5:
                                 nbr = 1
                                 majeureBI = pygame.image.load('images/majeureBI.png').convert()
                            elif nbr == 2:
                                majeureBI = pygame.image.load('images/majeureBI2.png').convert()
                            elif nbr == 3:
                                majeureBI = pygame.image.load('images/majeureBI3.png').convert()
                            elif nbr == 4:
                                majeureBI = pygame.image.load('images/majeureBI4.png').convert()
                            self.ecran.blit(majeureBI, (250, 200))
                    elif self.joueur.joueurposition_x == 50 and self.joueur.joueurposition_y == 200:
                        while reponse[1] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[1] = PFC().fonction_principale()
                            if reponse[1] == True:
                                self.score += 1
                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner', (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureDT = pygame.image.load('images/majeureDT.png').convert()
                        elif nbr == 2:
                            majeureDT = pygame.image.load('images/majeureDT2.png').convert()
                        elif nbr == 3:
                            majeureDT = pygame.image.load('images/majeureDT3.png').convert()
                        elif nbr == 4:
                            majeureDT = pygame.image.load('images/majeureDT4.png').convert()
                        self.ecran.blit(majeureDT, (250, 200))
                    elif self.joueur.joueurposition_x == 50 and self.joueur.joueurposition_y == 300:
                        while reponse[2] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[2] = JeuTicTacToe().fonction_principale()
                            if reponse[2] == True:
                                self.score += 1
                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureSE = pygame.image.load('images/majeureSE.png').convert()
                        elif nbr == 2:
                            majeureSE = pygame.image.load('images/majeureSE2.png').convert()
                        elif nbr == 3:
                            majeureSE = pygame.image.load('images/majeureSE3.png').convert()
                        elif nbr == 4:
                            majeureSE = pygame.image.load('images/majeureSE4.png').convert()
                        self.ecran.blit(majeureSE, (250, 200))
                    elif self.joueur.joueurposition_x == 50 and self.joueur.joueurposition_y == 400:
                        while reponse[3] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[3] = Captcha().fonction_principale()
                            if reponse[3] == True:
                                self.score += 1
                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureCS = pygame.image.load('images/majeureCS.png').convert()
                        elif nbr == 2:
                            majeureCS = pygame.image.load('images/majeureCS2.png').convert()
                        elif nbr == 3:
                            majeureCS = pygame.image.load('images/majeureCS3.png').convert()
                        elif nbr == 4:
                            majeureCS = pygame.image.load('images/majeureCS4.png').convert()
                        self.ecran.blit(majeureCS, (250, 200))
                    elif self.joueur.joueurposition_x == 50 and self.joueur.joueurposition_y == 500:
                        while reponse[4] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[4] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureNWC = pygame.image.load('images/majeureNWC.png').convert()
                        elif nbr == 2:
                            majeureNWC = pygame.image.load('images/majeureNWC2.png').convert()
                        elif nbr == 3:
                            majeureNWC = pygame.image.load('images/majeureNWC3.png').convert()
                        elif nbr == 4:
                            majeureNWC = pygame.image.load('images/majeureNWC4.png').convert()
                        self.ecran.blit(majeureNWC, (250, 200))
                    elif self.joueur.joueurposition_x == 500 and self.joueur.joueurposition_y == 100:
                        while reponse[5] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[5] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureIRV = pygame.image.load('images/majeureIRV.png').convert()
                        elif nbr == 2:
                            majeureIRV = pygame.image.load('images/majeureIRV2.png').convert()
                        elif nbr == 3:
                            majeureIRV = pygame.image.load('images/majeureIRV3.png').convert()
                        elif nbr == 4:
                            majeureIRV = pygame.image.load('images/majeureIRV4.png').convert()
                        self.ecran.blit(majeureIRV, (250, 200))
                    elif self.joueur.joueurposition_x == 500 and self.joueur.joueurposition_y == 500:
                        while reponse[6] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[6] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureBDML = pygame.image.load('images/majeureBDML.png').convert()
                        elif nbr == 2:
                            majeureBDML = pygame.image.load('images/majeureBDML2.png').convert()
                        elif nbr == 3:
                            majeureBDML = pygame.image.load('images/majeureBDML3.png').convert()
                        elif nbr == 4:
                            majeureBDML = pygame.image.load('images/majeureBDML4.png').convert()
                        self.ecran.blit(majeureBDML, (250, 200))
                    elif self.joueur.joueurposition_x == 900 and self.joueur.joueurposition_y == 100:
                        while reponse[7] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[7] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureITF = pygame.image.load('images/majeureITF.png').convert()
                        elif nbr == 2:
                            majeureITF = pygame.image.load('images/majeureITF2.png').convert()
                        elif nbr == 3:
                            majeureITF = pygame.image.load('images/majeureITF3.png').convert()
                        elif nbr == 4:
                            majeureITF = pygame.image.load('images/majeureITF4.png').convert()
                        self.ecran.blit(majeureITF, (250, 200))
                    elif self.joueur.joueurposition_x == 900 and self.joueur.joueurposition_y == 200:
                        while reponse[8] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[8] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureBIO = pygame.image.load('images/majeureBIO.png').convert()
                        elif nbr == 2:
                            majeureBIO = pygame.image.load('images/majeureBIO2.png').convert()
                        elif nbr == 3:
                            majeureBIO = pygame.image.load('images/majeureBIO3.png').convert()
                        elif nbr == 4:
                            majeureBIO = pygame.image.load('images/majeureBIO4.png').convert()
                        self.ecran.blit(majeureBIO, (250, 200))
                    elif self.joueur.joueurposition_x == 900 and self.joueur.joueurposition_y == 300:
                        while reponse[9] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[9] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureAE = pygame.image.load('images/majeureAE.png').convert()
                        elif nbr == 2:
                            majeureAE = pygame.image.load('images/majeureAE2.png').convert()
                        elif nbr == 3:
                            majeureAE = pygame.image.load('images/majeureAE3.png').convert()
                        elif nbr == 4:
                            majeureAE = pygame.image.load('images/majeureAE4.png').convert()
                        self.ecran.blit(majeureAE, (250, 200))
                    elif self.joueur.joueurposition_x == 900 and self.joueur.joueurposition_y == 400:
                        while reponse[10] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[10] = self.questions()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))
                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureSRD = pygame.image.load('images/majeureSRD.png').convert()
                        elif nbr == 2:
                            majeureSRD = pygame.image.load('images/majeureSRD2.png').convert()
                        elif nbr == 3:
                            majeureSRD = pygame.image.load('images/majeureSRD3.png').convert()
                        elif nbr == 4:
                            majeureSRD = pygame.image.load('images/majeureSRD4.png').convert()
                        self.ecran.blit(majeureSRD, (250, 200))
                    elif self.joueur.joueurposition_x == 900 and self.joueur.joueurposition_y == 500:
                        while reponse[11] == False:
                            self.ecran.fill((0, 0, 0))
                            reponse[11] = self.calcul_au_hasard()

                        self.creer_message('moyenne', 'Bonne réponse ! Tu es digne de pouvoir te renseigner',
                                           (290, 150, 100, 50), (255, 255, 255))
                        self.creer_message('moyenne', 'Appuie sur espace pour passer à une autre slide',
                                           (290, 550, 100, 50), (255, 255, 255))

                        if nbr == 1 or nbr == 5:
                            nbr = 1
                            majeureENSG = pygame.image.load('images/majeureENSG.png').convert()
                        elif nbr == 2:
                            majeureENSG = pygame.image.load('images/majeureENSG2.png').convert()
                        elif nbr == 3:
                            majeureENSG = pygame.image.load('images/majeureENSG3.png').convert()
                        elif nbr == 4:
                            majeureENSG = pygame.image.load('images/majeureENSG4.png').convert()
                        self.ecran.blit(majeureENSG, (250, 200))
                    else:
                        nbr = 1
                    tab[0] = nbr
                    tab[1] = reponse
                    return tab

    def fonction_principale(self):
        nbr = 1
        stop = 0
        reponse = [False,False,False,False,False,False,False,False,False,False,False,False]
        tab = [nbr,reponse]
        self.informations_du_joueur()  # demande les coordonnées du joueur
        while self.affichage_debut: #while loop pour faire l'affichage du début
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()
                if evenement.type == pygame.KEYDOWN: #si le joueur appuie sur la touche Entrée pour jouer
                    if evenement.key == pygame.K_RETURN:
                        self.affichage_debut = False
                self.ecran.fill((0,0,0))

                #Ecran d'accueil et explication du jeu

                imageaccueil = pygame.image.load('images/imageaccueil.png').convert()
                self.ecran.blit(imageaccueil,(250,10))
                self.creer_message('moyenne',
                                   'Bienvenue ' + self.joueur.nomjoueur + ' ' + self.joueur.prenomjoueur + '!',
                                   (360, 300, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Ce jeu est basé sur le principe des forums ou journées internationales à EFREI Paris ', (270, 350, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Avant de découvrir une majeure, il est nécessaire de réussir une question ou un jeu, pour voir si vous êtes digne de découvrir cette majeure !',
                                   (100, 370, 100, 50), (255, 255, 255))
                self.creer_message('petite', 'Vous vous déplacez avec les flèches du clavier, haut/bas/gauche/droite',
                                   (280, 390, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Au bout de 10 points, vous montez de 10 rang dans le classement',
                                   (280, 410, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Appuyez sur la touche ECHAP pour revenir à l accueil, votre touche F pour vous inscrire, et sur la touche V pour voir vos acceptations de voeux',
                                   (50, 430, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'Appuyez sur votre touche ENTREE pour commencer !', (310, 480, 200, 5), (255, 255, 255))
                self.creer_message('petite', 'Copyright © Karis Gwet - 2020', (380,550,200,5), (255,255,255))

                pygame.display.flip()

        cestfait = False
        while self.Encours:  # tant que la fenêtre sera
                peutsinscrire = False
                if self.score == 10 and self.joueur.classementjoueur >= 11 and cestfait == False: #Si le score du joueur est de 10, il gagne 10 places dans le classement
                    self.joueur.classementjoueur-= 10
                    cestfait = True
                for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                    if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                        sys.exit()

                    # Déplacement du joueur
                    elif evenement.type == pygame.KEYDOWN:
                        if evenement.key == pygame.K_UP:
                            self.joueur.joueurposition_y -= 50
                        elif evenement.key == pygame.K_DOWN:
                            self.joueur.joueurposition_y += 50
                        elif evenement.key == pygame.K_LEFT:
                            self.joueur.joueurposition_x -= 50
                        elif evenement.key == pygame.K_RIGHT:
                            self.joueur.joueurposition_x += 50
                        elif evenement.key == pygame.K_SPACE:
                            tab[0] += 1
                        elif evenement.key == pygame.K_f:
                            self.joueur.formulaire = Formulaire().fonction_principale() #Je donne la liste des voeux
                            #Le joueur choisit ses 3 majeures
                        elif evenement.key == pygame.K_v and len(self.joueur.formulaire) == 3:
                            self.v = True
                            self.verification_voeux()
                        elif evenement.key == pygame.K_ESCAPE:  # Recommencer le jeu
                            stop = 0
                            Jeu().fonction_principale()


                        # Ne pas dépasser les limites
                        if self.joueur.joueurposition_x < 30:
                            self.joueur.joueurposition_x += 50
                        if self.joueur.joueurposition_x > 900:
                            self.joueur.joueurposition_x -= 50
                        if self.joueur.joueurposition_y < 80:
                            self.joueur.joueurposition_y += 50
                        if self.joueur.joueurposition_y > 530:
                            self.joueur.joueurposition_y -= 50


                # Pour ne pas avoir des cases rouges d'affilés
                pygame.draw.rect(self.ecran, (0, 0, 0), (0, 0, 1000, 600))

                # Affichage et placement des carrés blancs
                # Partie gauche
                pygame.draw.rect(self.ecran, (255, 255, 255), (50, 100, 20, 20))  # x,y,longueur,largeur(50,50,20,20)
                pygame.draw.rect(self.ecran, (255, 255, 255), (50, 200, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (50, 300, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (50, 400, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (50, 500, 20, 20))

                # Partie droite
                pygame.draw.rect(self.ecran, (255, 255, 255), (900, 100, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (900, 200, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (900, 300, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (900, 400, 20, 20))
                pygame.draw.rect(self.ecran, (255, 255, 255), (900, 500, 20, 20))

                # Partie milieu haut
                pygame.draw.rect(self.ecran, (255, 255, 255), (500, 100, 20, 20))

                # Partie milieu bas
                pygame.draw.rect(self.ecran, (255, 255, 255), (500, 500, 20, 20))

                # Afficher le joueur
                pygame.draw.rect(self.ecran, (255, 0, 0), (self.joueur.joueurposition_x, self.joueur.joueurposition_y, 20, 20))

                # Afficher les limites, le cadre blanc
                pygame.draw.rect(self.ecran, (255, 255, 255), (30, 80, 920, 460), 3)

                tab = self.joueur_sur_case_blanche(tab)

                if self.v == True and stop == 0:
                    self.verification_voeux()
                    stop = 1

                if stop == 0:
                    pygame.display.flip()


    #Valider les voeux
    def verification_voeux(self):
        #["AVE", "SE", "DT", "BI", "CYBER", "NC", "IR", "BD", "ITF", 'BIO', 'SRD', 'ENS']
        appartenance = [0,0,0,0,0,0,0,0,0,0,0,0]
        nbVoeu = 0
        if self.joueur.classementjoueur > 1:
            liste = generer_classement(int(self.joueur.classementjoueur)-1)
            conversion = Individus(self.joueur.nomjoueur,self.joueur.prenomjoueur) #je convertis mon joueur en individu
            conversion.listevoeu = self.joueur.formulaire
            liste.append(conversion) #j'ajoute le joueur à mon classement
            for individu in liste: #chaque individu dans le classement
                insertion = 0
                nbVoeu = 0
                while insertion == 0:
                    if individu.listevoeu[nbVoeu] == "AVE":
                        if appartenance[0] < 26 :
                            appartenance[0] += 1 #nombre de place dans la majeure
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "SE":
                        if appartenance[1] < 26:
                            appartenance[1] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "DT":
                        if appartenance[2] < 26 :
                            appartenance[2] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "BI":
                        if appartenance[3] < 26 :
                            appartenance[3] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "CYBER":
                        if appartenance[4] < 26 :
                            appartenance[4] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "NC":
                        if appartenance[5] < 26 :
                            appartenance[5] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "IR":
                        if appartenance[6] < 26 :
                            appartenance[6] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "BD":
                        if appartenance[7] < 26 :
                            appartenance[7] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "ITF":
                        if appartenance[8] < 26 :
                            appartenance[8] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "BIO":
                        if appartenance[9] < 26 :
                            appartenance[9] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "SRD":
                        if appartenance[10] < 26 :
                            appartenance[10] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

                    elif individu.listevoeu[nbVoeu] == "ENS":
                        if appartenance[11] < 26 :
                            appartenance[11] += 1
                            insertion = 1
                        elif nbVoeu < 3:
                            nbVoeu += 1
                        else:
                            insertion = 1

        dico = {"AVE":appartenance[0],"SE":appartenance[1],"DT":appartenance[2],"BI":appartenance[3],"CYBER":appartenance[4],"NC":appartenance[5],
                "IR":appartenance[6],"BD":appartenance[7],"ITF":appartenance[8],"BIO":appartenance[9],"SRD":appartenance[10],"ENS":appartenance[11]}

        self.ecran.fill((0,0,0))
        voeux = pygame.image.load('images/voeux.png').convert()
        succes = self.joueur.formulaire[nbVoeu]
        self.ecran.blit(voeux,(350,70))
        self.creer_message('moyenne',
                           'Nom de famille : '+self.joueur.nomjoueur,(350, 290, 200, 5), (240, 240, 240))
        self.creer_message('moyenne',
                           'Prénom : '+self.joueur.prenomjoueur,(350, 340, 200, 5), (240, 240, 240))
        self.creer_message('moyenne',
                           'Classement : '+str(self.joueur.classementjoueur),(350, 390, 200, 5), (240, 240, 240))
        self.creer_message('moyenne', 'Vous avez obtenu la majeure : ' +succes+ ' en position numéro '+str(dico[succes]), (350, 440, 200, 5),
                           (240, 240, 240))
        self.creer_message('moyenne',
                           'Félicitations, vous pourrez accéder à cette majeure !', (350, 490, 200, 5),
                           (240, 240, 240))
        pygame.display.flip()


#Classe joueur
class Joueur:
    # Données du joueur
    def __init__(self):
        self.nomjoueur = ""
        self.prenomjoueur = ""
        self.classementjoueur = ""
        self.joueurposition_x = 500
        self.joueurposition_y = 300
        self.joueurdirection_x = 0
        self.joueurdirection_y = 0
        self.formulaire = []

class Individus:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        self.listevoeu = []


def generer_classement(position_classement):
    classement = []
    appartenance = ["AVE","SE","DT","BI","CYBER","NC","IR","BD","ITF",'BIO','SRD','ENS']

    fichier = open("nomprenomgens.txt","r")
    lignes = fichier.readlines()
    lignes = lignes[0:position_classement] #je prends les lignes du début jusqu'à ma position
    fichier.close()
    lignes = [i.strip() for i in lignes] #strip() pour enlever tous les "\n"
    print(lignes[0])
    for individu in lignes[0:]:
        i = 0
        match = re.match(r"([A-Z]+)([ ])([A-Za-z'-]+)",individu,re.I) #match contient le nom et le prénom
        objet = match.groups() #prends le nom l'espace et le prénom séparement
        perso = Individus(objet[0],objet[2]) #je stocke dans une liste perso le nom et le prénom
        for i in range(0,3):
            rando = random.randint(0,11)
            while appartenance[rando] in perso.listevoeu: #je cherche parmi ma liste appartenance la majeure
                rando = random.randint(0, 11)
            perso.listevoeu.append(appartenance[rando]) #je vais l'ajouter dans listevoeu de l'individu
        classement.append(perso) #j'ajoute dans ma liste classement
    return classement





if __name__ == '__main__':
    #list = generer_classement(2)
    #print(list)
    pygame.init()  # j'initialise le module pygame
    Jeu().fonction_principale()  # j'appelle la fonction_principale
    pygame.quit()  # je quitte