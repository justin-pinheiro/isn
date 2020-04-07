#initialisation de pygame
import pygame
import random
import math

from variables import *

pygame.init()



            #CLASSES
#my_clock = pygame.time.Clock()
class Decor:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.vitesse = 0

    def actualiser(self):
        ecran.blit(self.image, (self.x,self.y))

#jtest = 8


class Joueur:

    def __init__(self):
        self.x = joueur_x
        self.y = joueur_y
        self.hauteur = joueur_hauteur
        self.largeur = joueur_largeur_courir

        self.vitesse_y = joueur_vitesse_y

        self.saut_pas = saut_pas
        self.saut = False

        self.left = True
        self.right = False

    def actualiser(self):

        #affichage du joueur
        pygame.time.wait(50)

        if coupL:
           ## joueur.x_coup = joueur.x + posimghit[position_image_coup]
            ecran.blit(joueur_image, (self.x_coup,self.y))
        else:
            ecran.blit(joueur_image, (self.x,self.y))

        self.hitbox = (self.x, self.y,self.largeur, self.hauteur)
        if (self.left):
            self.punch_hitbox = (self.x, self.y+50,123,20)
        if (self.right):
            self.punch_hitbox = (self.x +123 + self.largeur, self.y+50,123,20)
        if(joueur_tombe):
            #vitesse inferieure a vitesse max
            if (self.vitesse_y + self.saut_pas < joueur_vitesse_y_max):
                self.vitesse_y += self.saut_pas
                self.saut_pas += 1
            #vitesse max
            else: self.vitesse_y = joueur_vitesse_y_max

        #pour que le joueur saute si touche espace pressée
        if (self.saut == True):
            self.saut_pas = saut_pas
            self.y -= self.vitesse_y
            if (self.vitesse_y - self.saut_pas > joueur_vitesse_y_min):
                self.vitesse_y -= self.saut_pas
                if (self.saut_pas != 1):
                    self.saut_pas -= 1
            else: self.vitesse_y = joueur_vitesse_y_min

            if (self.vitesse_y == joueur_vitesse_y_min):
                self.saut = False
                self.saut_pas = saut_pas



class Ennemi:

    def __init__(self):
        self.collision = False
        self.y = 0
        self.creer()

    def actualiser(self):
        ecran.blit(ennemi_image, (self.x,self.y))
        self.hitbox = (self.x, self.y,self.longueur, self.hauteur)

    def creer(self):
        self.x = 0
        self.hauteur = ennemi_hauteur
        self.longueur = ennemi_longueur



class Plateforme:

    def __init__(self):
        self.collision = False

    def actualiser(self):

        pygame.draw.rect(ecran, (0,0,0), (self.x, self.y, self.longueur, self.hauteur))

        #le joueur touche la plateforme
        if (collision(self.x,self.y,self.longueur,self.hauteur)):
            #bloquer le joueur
            self.collision = True

        #le joueur ne touche pas la plateforme
        else:
            if(collision(self.x,self.y - joueur.vitesse_y ,self.longueur,self.hauteur)):
                self.collision = True
                joueur_tombe = False
                joueur.y = self.y - joueur.hauteur
            else:
                self.collision = False






            #FONCTIONS

def collision(x, y, longueur, hauteur):
    if (joueur.y <= y + hauteur and joueur.y + joueur.hauteur >= y and joueur.x + joueur.largeur >= x and joueur.x <= x + longueur ):
        return True
    else:
        return False

def a_droite_de_zone_limite():
    if (joueur.x > zone_libre_x + zone_libre_taille): return True
    else: return False

def a_gauche_de_zone_limite():
    if (joueur.x + joueur.largeur < zone_libre_x): return True
    else: return False

def joueur_avance_vers(direction):

    if (direction == "droite"):
        building1.x -= building1.vitesse
        Platform.x -= Platform.vitesse
        building2.x -= building2.vitesse/2
        e1.x -= joueur_vitesse_x
        e2.x -= joueur_vitesse_x
        e3.x -= joueur_vitesse_x
        p2.x -= joueur_vitesse_x

    elif (direction == "gauche"):
        building1.x += building1.vitesse
        Platform.x += Platform.vitesse
        building2.x += building2.vitesse/2
        e1.x += joueur_vitesse_x
        e2.x += joueur_vitesse_x
        e3.x += joueur_vitesse_x
        p2.x += joueur_vitesse_x

def camera_avance_vers(direction):

    if (direction == "droite"):

        joueur.x += joueur_vitesse_x/2
        building1.x += building1.vitesse/2
        Platform.x += Platform.vitesse/2
        building2.x += building2.vitesse/2
        e1.x += joueur_vitesse_x/2
        e2.x += joueur_vitesse_x/2
        e3.x += joueur_vitesse_x/2
        p2.x += joueur_vitesse_x/2

    elif (direction == "gauche"):

        joueur.x -= joueur_vitesse_x/2
        building1.x -= building1.vitesse/2
        Platform.x -= Platform.vitesse/2
        building2.x -= building2.vitesse/2
        e1.x -= joueur_vitesse_x/2
        e2.x -= joueur_vitesse_x/2
        e3.x -= joueur_vitesse_x/2
        p2.x -= joueur_vitesse_x/2

def actualiser():
    global joueur_tombe

    #le joueur touche le sol
    if(p1.collision or p2.collision): joueur_tombe = False
    #joueur ne touche pas le sol
    if (not p1.collision and not p2.collision and not joueur.saut): joueur_tombe = True

    if(joueur_tombe):
        joueur.y += joueur.vitesse_y







            #TITRE ET CREATION DES OBJECTS

    #titre du jeu
pygame.display.set_caption("Game")

joueur = Joueur()

p1 = Plateforme()
p1.longueur = ecran_largeur
p1.hauteur = p_hauteur
p1.y = ecran_hauteur - p_hauteur
p1.x = 0
p2 = Plateforme()
p2.longueur = 200
p2.hauteur = p_hauteur
p2.y = 500
p2.x = 100

e1 = Ennemi()
e1.x = 200
e1.y = p1.y - ennemi_hauteur
e2 = Ennemi()
e2.x = 300
e2.y = p1.y - ennemi_hauteur
e3 = Ennemi()
e3.x = 400
e3.y = p1.y - ennemi_hauteur



Platform = Decor()
Platform.x = 0 - ecran_largeur
Platform.vitesse = 25
Platform.image = pygame.image.load("img/decor/decor/Plateforme.png")
building1 = Decor()
building1.x = 0 - ecran_largeur
building1.vitesse = 25
building1.image = pygame.image.load("img/decor/decor/building1.png")
building2 = Decor()
building2.image = pygame.image.load("img/decor/decor/building2.png")
building2.x = 760 - ecran_largeur
building2.vitesse = 15
building3 = Decor()
building3.x = 25
building3.vitesse = 10
building3.image = pygame.image.load("img/decor/decor/building3.png")
fond = Decor()
fond.x = 0
fond.vitesse = 10
fond.image = pygame.image.load("img/decor/decor/neonsky.png")




            #BOUCLE

#booleen qui permet de faire fonctionner le jeu (true = jeu en cours, false = jeu arrété)
run = True
while run:

    # Jeu en pause
    while (commencer == False):
        pygame.draw.rect(ecran, (30,6,40), (0, 0, ecran_largeur, ecran_hauteur))
        #bouton start
        pygame.draw.rect(ecran, (250,250,250), (boutonstart_x, boutonstart_y, boutonstart_largeur, boutonstart_hauteur))
        #bouton quitter
        pygame.draw.rect(ecran, (250,250,250), (boutonquitte_x, boutonquitte_y, boutonquitte_largeur, boutonquitte_hauteur ))


        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                #on a appuye sur le bouton play
                if event.button == 1 and zonestart.collidepoint(event.pos):
                    print("start")
                    commencer = True
                    jeu = True

            if event.type==pygame.MOUSEBUTTONDOWN:
                #on a appuye sur le bouton quitte
                if event.button == 1 and zonequitte.collidepoint(event.pos):
                    print("quitte")
                    run = False
                    commencer = True
                    jeu = False

            if event.type == pygame.QUIT:
                run = False
                commencer = True
                jeu = False

        pygame.display.update()

    # Jeu en cours
    if jeu == True and commencer == True :


        #délai de renouvellement de la boucle
        pygame.time.delay(1)

        #ANIMATION DU JOUEUR

        keys = pygame.key.get_pressed()

        #mouvement gauche
        if (keys[pygame.K_LEFT]):
                #images du joueur
            #joueur.largeur = joueur_largeur_courir
            joueur_image = image_gauche[position_image_gauche]
            position_image_gauche = (position_image_gauche + 1)%8
            joueur.left = True
            joueur.right = False

            #si bord gauche n'est pas atteint
            if(building1.x + building1.vitesse < 0):
                #si joueur à gauche de la zone limite
                if(a_gauche_de_zone_limite()):
                    joueur_avance_vers("gauche")
                else:
                    joueur.x -= joueur_vitesse_x

            #si bord gauche atteint
            else:
                #si joueur ne touche pas le bord
                if(joueur.x  - joueur_vitesse_x >= 0):
                    joueur.x -= joueur_vitesse_x
                #si joueur touche le bord
                else:
                    joueur.x = 0

        #mouvement droite
        elif (keys[pygame.K_RIGHT]):
                #images du joueur
            #joueur.largeur = joueur_largeur_courir
            joueur_image = image_droite[position_image_droite]
            position_image_droite = (position_image_droite + 1)%8
            joueur.right = True
            joueur.left = False


            #si bord droit n'est pas atteint
            if(building1.x - building1.vitesse > 0-2*ecran_largeur):
                #si joueur à droite de la zone limite
                if(a_droite_de_zone_limite()):
                    joueur_avance_vers("droite")
                else:
                    joueur.x += joueur_vitesse_x
            #si bord droit atteint
            else:
                #si joueur ne touche pas le bord
                if(joueur.x + joueur.largeur + joueur_vitesse_x <= ecran_largeur):
                    joueur.x += joueur_vitesse_x
                #si joueur touche le bord
                else:
                    joueur.x = ecran_largeur - joueur.largeur

        #pas de mouvement
        else:
            #images du joueur
            #joueur.largeur = joueur_largeur_debout
            if(joueur.right):
                joueur_image = image_stand[position_image_stand]
                position_image_stand = (position_image_stand)

            else:
                joueur_image = image_standL[position_image_stand]
                position_image_stand = (position_image_stand)

            #si bord droit ou gauche ne sont pas atteints
            if(building1.x - building1.vitesse > 0-2*ecran_largeur and building1.x + building1.vitesse < 0 and building2.x - building2.vitesse > 0-2*ecran_largeur and building2.x + building2.vitesse < 0):
                #si joueur à gauche du milieu de l'ecran
                if(joueur.x + joueur_vitesse_x < ecran_milieu):
                    camera_avance_vers("droite")

                #si joueur à droite du milieu de l'ecran
                elif(joueur.x - joueur_vitesse_x > ecran_milieu):
                    camera_avance_vers("gauche")


        #saut
        if (keys[pygame.K_UP] and not joueur_tombe and not joueur.saut):
            joueur.saut = True

        #animation coup
        if (keys[pygame.K_SPACE]):
            #if joueur.position_image_coup == 0:
            #if jtest == 8:
             #   jtest = 0

              #  if jtest < 8:

            #images du joueur
                    if (joueur.left):
                        coupL == True
                        joueur_image = image_coup[position_image_coup]
                        position_image_coup = (position_image_coup + 1)%8
               #         jtest =+ 1

                    else:
                        joueur_image = image_coupR[position_image_coup]
                        position_image_coup = (position_image_coup + 1)%8
                #        jtest =+ 1








                    #AFFICHAGE & ACTUALISATION


        fond.actualiser()
        building3.actualiser()
        building2.actualiser()
        building1.actualiser()
        Platform.actualiser()

        #pygame.draw.rect(ecran, (0,200,0), (zone_libre_x, 0, zone_libre_taille, ecran_hauteur))
        pygame.draw.rect(ecran, (0,0,255), (joueur.x +120, joueur.y, 107, 120))

        e1.actualiser()
        e2.actualiser()
        e3.actualiser()

        joueur.actualiser()

        actualiser()

        #pygame.draw.rect(ecran, (0,0,255), (joueur.hitbox))
        pygame.draw.rect(ecran, (0,255,0), (joueur.punch_hitbox))

        p1.actualiser()
        p2.actualiser()

        #bouton pause
        pygame.draw.rect(ecran, (250,250,250), (boutonpause_x, boutonpause_y, boutonpause_largeur, boutonpause_hauteur))

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                #on a appuye sur le bouton pause
                if event.button == 1 and zonepause.collidepoint(event.pos):
                    print("pause")
                    commencer = False

            if event.type == pygame.QUIT:
                run = False


    #actualisation de l'écran
    pygame.display.update()
#my_clock.tick(60)

pygame.quit()