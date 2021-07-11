import pygame
import sys


class Formulaire:

    def __init__(self):
        self.ecran = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choix des formulaires par Karis')
        self.choix = ''
        self.formulairevoeu = []

    # Création de message texte
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
        self.ecran.blit(message, message_rectangle)  # message_rectangle correspond à la position (x,y) de mon message


    def fonction_principale(self):

        # SE
        SE = pygame.image.load('images/SE.png').convert()
        SErect = SE.get_rect(
            midleft=self.ecran.get_rect().center)  # prends la position du milieu de l'écran, la mets dans "midleft" car get_rect() ne prend que des mots-clés
        SErect.x += 260  # midleft est le milieu gauche donc on rajoute 75 pour mettre à droite
        SErect.y += 190

        # DT
        DT = pygame.image.load('images/DT.png').convert()
        DTrect = DT.get_rect(
            midleft=self.ecran.get_rect().center)  # prends la position du milieu de l'écran, la mets dans "midleft" car get_rect() ne prend que des mots-clés
        DTrect.x += 260  # midleft est le milieu gauche donc on rajoute 75 pour mettre à droite

        # BI
        BI = pygame.image.load('images/BI.png').convert()
        BIrect = BI.get_rect(
            midleft=self.ecran.get_rect().center)  # prends la position du milieu de l'écran, la mets dans "midleft" car get_rect() ne prend que des mots-clés
        BIrect.x += 260  # midleft est le milieu gauche donc on rajoute 75 pour mettre à droite
        BIrect.y -= 120

        # Feuilles
        CYBER = pygame.image.load('images/CYBER.png').convert()
        CYBERrect = CYBER.get_rect(center=self.ecran.get_rect().center)  # coordonnées du centre de la page
        CYBERrect.y += 200
        CYBERrect.x += 70

        # NC
        NC = pygame.image.load('images/NC.png').convert()
        NCrect = NC.get_rect(center=self.ecran.get_rect().center)  # coordonnées du centre de la page
        NCrect.x += 70

        # IR
        IR = pygame.image.load('images/IR.png').convert()
        IRrect = IR.get_rect(center=self.ecran.get_rect().center)  # coordonnées du centre de la page
        IRrect.y -= 150
        IRrect.x += 70

        # BD
        BD = pygame.image.load('images/BD.png').convert()
        BDrect = BD.get_rect(midright=self.ecran.get_rect().center)
        BDrect.x -= 140
        BDrect.y += 200

        # ITF
        ITF = pygame.image.load('images/ITF.png').convert()
        ITFrect = ITF.get_rect(midright=self.ecran.get_rect().center)
        ITFrect.x -= 140
        ITFrect.y += 20

        # BIO
        BIO = pygame.image.load('images/BIO.png').convert()
        BIOrect = BIO.get_rect(midright=self.ecran.get_rect().center)
        BIOrect.x -= 140
        BIOrect.y -= 120

        # AVE
        AVE = pygame.image.load('images/AVE.png').convert()
        AVErect = AVE.get_rect(midright=self.ecran.get_rect().center)
        AVErect.x -= 340
        AVErect.y -= 120

        # SRD
        SRD = pygame.image.load('images/SRD.png').convert()
        SRDrect = SRD.get_rect(midright=self.ecran.get_rect().center)
        SRDrect.x -= 340
        SRDrect.y += 20

        # ENS
        ENS = pygame.image.load('images/ENS.png').convert()
        ENSrect = ENS.get_rect(midright=self.ecran.get_rect().center)
        ENSrect.x -= 340
        ENSrect.y += 200


        Encours = True
        estinscrit = [False,False,False,False,False,False,False,False,False,False,False,False]
        color_touche_active = pygame.Color('red')
        while Encours and len(self.formulairevoeu) < 4:  # tant que la fenêtre sera ouverte
            if (len(self.formulairevoeu) == 3):
                return self.formulairevoeu
            for evenement in pygame.event.get():  # pour chaque evenement situé des évènements du module pygame
                if evenement.type == pygame.QUIT:  # s'il appuie sur la croix rouge
                    sys.exit()

                # Sélection du joueur
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if SErect.collidepoint(position) and estinscrit[0]==False:  # s'il y a collision, càd si les coordonnées de l'image des ciseaux = celle de là où à lieu le clic
                        self.choix = 'SE'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[0] = True
                    elif DTrect.collidepoint(position) and estinscrit[1]==False:
                        self.choix = 'DT'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[1] = True
                    elif BIrect.collidepoint(position) and estinscrit[2]==False:
                        self.choix = 'BI'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[2] = True
                    elif CYBERrect.collidepoint(position) and estinscrit[3]==False:
                        self.choix = 'CYBER'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[3] = True
                    elif NCrect.collidepoint(position) and estinscrit[4]==False:
                        self.choix = 'NC'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[4] = True
                    elif IRrect.collidepoint(position) and estinscrit[5]==False:
                        self.choix = 'IR'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[5] = True
                    elif BDrect.collidepoint(position) and estinscrit[6]==False:
                        self.choix = 'BD'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[6] = True
                    elif ITFrect.collidepoint(position) and estinscrit[7]==False:
                        self.choix = 'ITF'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[7] = True
                    elif BIOrect.collidepoint(position) and estinscrit[8]==False:
                        self.choix = 'BIO'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[8] = True
                    elif ENSrect.collidepoint(position) and estinscrit[9]==False:
                        self.choix = 'ENS'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[9] = True
                    elif SRDrect.collidepoint(position) and estinscrit[10]==False:
                        self.choix = 'SRD'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[10] = True
                    elif AVErect.collidepoint(position) and estinscrit[11]==False:
                        self.choix = 'AVE'
                        self.formulairevoeu.append(self.choix)
                        estinscrit[11] = True


                # Afficher les images
                self.ecran.fill((0, 0, 0))
                self.creer_message('moyenne','Choisis ton voeu : '+str(len(self.formulairevoeu)),(400, 50, 90, 50), (255, 255, 255))
                self.ecran.blit(SE, (SErect))  # on colle l'image ciseaux à la position ciseauxrect
                self.ecran.blit(DT, (DTrect))
                self.ecran.blit(BI, (BIrect))
                self.ecran.blit(CYBER, (CYBERrect))
                self.ecran.blit(NC, (NCrect))
                self.ecran.blit(IR, (IRrect))
                self.ecran.blit(BD, (BDrect))
                self.ecran.blit(ITF, (ITFrect))
                self.ecran.blit(BIO, (BIOrect))
                self.ecran.blit(AVE, (AVErect))
                self.ecran.blit(SRD, (SRDrect))
                self.ecran.blit(ENS, (ENSrect))

                pygame.display.flip()