#initialisation de pygame
import pygame
import random
import math

from variables import *

pygame.init()

#booleen qui permet de faire fonctionner le jeu (true = jeu en cours, false = jeu arrété)
run = True


            #CLASSES

class Decor:

    def __init__(self, x, vitesse, image):
        self.x = x
        self.vitesse = vitesse
        self.image = image
        self.y = 0

    def actualiser(self):
        ecran.blit(self.image, (self.x,self.y))



class Joueur:

    def __init__(self):
        self.x = ecran_milieu
        self.y = joueur_y
        self.hauteur = joueur_hauteur
        self.largeur = joueur_largeur_debout

        self.vitesse_y = joueur_vitesse_y
        self.vitesse_x = 30

        self.saut_pas = 10
        self.saut = False

        self.left = True
        self.right = False

        self.hitbox = pygame.Rect(self.x , self.y , self.largeur , self.hauteur)

    def actualiser(self):
        #affichage du joueur
        pygame.time.wait(50)

        pygame.draw.rect(ecran, (0,0,255), (self.x, self.y, self.largeur, self.hauteur))

        ecran.blit(joueur_image, (self.x, self.y))

        self.punch_y = self.y
        self.punch_largeur = 100
        self.punch_hauteur = 100

        if (self.left):
            self.punch_x = self.x - 100
            self.punch_hitbox = pygame.Rect(self.punch_x , self.punch_y , self.punch_largeur, self.punch_hauteur)
        if (self.right):
            self.punch_x = self.x + self.largeur
            self.punch_hitbox = pygame.Rect(self.punch_x , self.punch_y, self.punch_largeur,self.punch_hauteur)

        if(joueur_tombe):
            #vitesse inferieure a vitesse max
            if (self.vitesse_y + self.saut_pas < Y_MAX):
                self.vitesse_y += self.saut_pas
                self.saut_pas += 1
            #vitesse max
            else: self.vitesse_y = Y_MAX

        #pour que le joueur saute si touche espace pressée
        if (self.saut == True):
            self.saut_pas = saut_pas
            self.y -= self.vitesse_y
            if (self.vitesse_y - self.saut_pas > Y_MIN):
                self.vitesse_y -= self.saut_pas
                if (self.saut_pas != 1):
                    self.saut_pas -= 1
            else: self.vitesse_y = Y_MIN

            if (self.vitesse_y == Y_MIN):
                self.saut = False
                self.saut_pas = saut_pas



class Ennemi:

    def __init__(self, x, y, comportement):
        self.collision = False
        self.image = ennemi_image
        self.x = x
        self.y = y
        self.comportement = comportement
        self.hauteur = ennemi_hauteur
        self.longueur = ennemi_longueur
        self.vitesse = random.randint(2,13)
        self.hitbox = pygame.Rect(self.x, self.y,self.longueur, self.hauteur)
        self.distance = random.randint(300,500)
        self.direction = "droite"

        self.temps_depart = random.randint(500,1000)
        self.temps = self.temps_depart
        self.pause = 0

    def actualiser(self):


        ecran.blit(self.image, (self.x,self.y))

        if self.comportement != "sauvage":
            if self.x > joueur.x + joueur.largeur :
                self.direction = "gauche"
            if self.x + self.longueur < joueur.x :
                self.direction = "droite"
        else:
            if (self.x + self.longueur/2 >= joueur.x - self.distance and self.x + self.longueur/2 <= joueur.x + joueur.largeur + self.distance):
                self.direction = self.direction
            else:
                if self.x > joueur.x + joueur.largeur :
                    self.direction = "gauche"
                if self.x + self.longueur < joueur.x :
                    self.direction = "droite"

        #DIFFERENTS ENNEMIS

        joueur_gauche = joueur.x
        joueur_droite = joueur.x + joueur.largeur

        ennemi_gauche = self.x
        ennemi_droite = self.x + self.longueur

        if(self.comportement == "aggressif"):
            if(joueur.x  + joueur.largeur/2 > self.x + self.longueur):
                self.x += self.vitesse
            if(joueur.x + joueur.largeur/2 < self.x):
                self.x -= self.vitesse
            if(collision(self.x,self.y,self.longueur,self.hauteur)):
                game_over()

        if(self.comportement == "distant"):
            #Ennemi trop loin = se rapproche
            if(ennemi_droite < joueur_gauche - self.distance):
                self.x += self.vitesse
            if(self.x > joueur.x + joueur.largeur + self.distance):
                self.x -= self.vitesse

            #Ennemi trop près = fuit
            if(self.x + self.longueur > joueur.x - self.distance - 100 and self.x + self.longueur < joueur.x):
                self.x -= self.vitesse
            if(self.x < joueur.x + joueur.largeur + self.distance - 100 and self.x > joueur.x + joueur.largeur):
                self.x += self.vitesse
            #tir
            self.temps -= 10
            if self.temps <= 0:
                self.temps = self.temps_depart
                listeProjectiles.append(Projectile(self.x,self.direction))

        if(self.comportement == "sauvage"):
            if(collision(self.x,self.y,self.longueur,self.hauteur)):
                game_over()
            if(self.x + self.longueur/2 >= joueur.x - self.distance and self.x + self.longueur/2 <= joueur.x + joueur.largeur + self.distance):
                self.pause = 500
                if self.direction == "droite":
                    self.x += self.vitesse*3
                if self.direction == "gauche":
                    self.x -= self.vitesse*3
            else:
                if self.pause > 0:
                    self.pause -= 10
                else:
                    if(joueur.x  + joueur.largeur/2 > ennemi_droite):
                        self.x += self.vitesse/2
                    if(joueur.x + joueur.largeur/2 < self.x):
                        self.x -= self.vitesse/2



class Projectile:
    def __init__(self, x, direction):
        self.x = x
        self.y = p1.y - random.randint(55,80)
        self.largeur = 20
        self.hauteur = 5
        self.direction = direction

    def actualiser(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        pygame.draw.rect(ecran, (200,50,50), (self.hitbox))

        if(self.direction == "droite"):
            self.x += 30
        if(self.direction == "gauche"):
            self.x -= 30


        if(collision(self.x,self.y,self.largeur,self.hauteur)):
            game_over()



class Plateforme:

    def __init__(self, longueur, hauteur, y, x):
        self.longueur = longueur
        self.hauteur = hauteur
        self.y = y
        self.x = x
        self.collision = False

        self.hitbox_apparence = pygame.Rect(self.x , self.y , self.longueur , self.hauteur)
        self.hitbox = pygame.Rect(self.x , self.y - joueur.vitesse_y , self.longueur , self.hauteur)

    def actualiser(self):
        pygame.draw.rect(ecran, (50,0,50), (self.hitbox_apparence))

        #collision haut de la plateforme
        if(collision(self.x,self.y - joueur.vitesse_y ,self.longueur,self.hauteur)):
            self.collision = True
            joueur.vitesse_y = Y_MIN
            joueur_tombe = False
            joueur.y = self.y - joueur.hauteur

        else:
            self.collision = False




            #FONCTIONS



def nouveau_round():
    global round
    global round1
    global round2
    global round3
    global round4
    global round5
    global round_liste
    global ennemis_vivants

    round += 1
    if round == 1:
        round_liste = [a,a,a,a,d]
        ennemis_vivants = [a,a,a,a,d]
    if round == 2:
        round_liste = [a,a,d,a,a,d,a,a,d,a]
        ennemis_vivants = [a,a,d,a,a,d,a,a,d,a]
    if round == 3:
        round_liste = [d,d,a,d,a,a,a,d,d,a]
        ennemis_vivants = [d,d,a,d,a,a,a,d,d,a]
    if round == 4:
        round_liste = [a,d,d,a,d,a,d,d,d,d,a,d,a,d,s]
        ennemis_vivants = [a,d,d,a,d,a,d,d,d,d,a,d,a,d,s]
    if round == 5:
        round_liste = [a,d,d,a,s,a,d,d,d,d,d,s,a,d,s]
        ennemis_vivants = [a,d,d,a,s,a,d,d,d,d,d,s,a,d,s]

def creer_ennemi():
    global round_liste

    alea = bool(random.getrandbits(1)) #True or False

    comportement = round_liste[0]

    if(alea): listeEnnemis.append(Ennemi(collines.x , p1.y - ennemi_hauteur, comportement))
    if(not alea): listeEnnemis.append(Ennemi(collines.x + 3800, p1.y - ennemi_hauteur, comportement))

    del round_liste[0]


def collision(x, y, longueur, hauteur):
    if (joueur.y <= y + hauteur and joueur.y + joueur.hauteur >= y and joueur.x + joueur.largeur >= x and joueur.x <= x + longueur ): return True
    else: return False

def punch_collision(x, y, longueur, hauteur):
    if (joueur.punch_y <= y + hauteur and joueur.punch_y + joueur.punch_hauteur >= y and joueur.punch_x + joueur.punch_largeur >= x and joueur.punch_x <= x + longueur ): return True
    else: return False

def a_droite_de_zone_limite():
    if (joueur.x > zone_libre_x + zone_libre_taille): return True
    else: return False

def a_gauche_de_zone_limite():
    if (joueur.x + joueur.largeur < zone_libre_x): return True
    else: return False

def joueur_avance_vers(direction):
    if (direction == "droite"):
        collines.x -= collines.vitesse
        fond.x -= fond.vitesse
        for i in range (len(listeEnnemis)):
            listeEnnemis[i].x -= joueur.vitesse_x
        for i in range (len(listeProjectiles)):
            listeProjectiles[i].x -= joueur.vitesse_x

    elif (direction == "gauche"):
        collines.x += collines.vitesse
        fond.x += fond.vitesse
        for i in range (len(listeEnnemis)):
            listeEnnemis[i].x += joueur.vitesse_x
        for i in range (len(listeProjectiles)):
            listeProjectiles[i].x += joueur.vitesse_x

def camera_avance_vers(direction):
    if (direction == "droite"):
        fond.x += fond.vitesse
        joueur.x += joueur_vitesse_x/2
        collines.x += collines.vitesse/2
        for i in range (len(listeEnnemis)):
            listeEnnemis[i].x += joueur.vitesse_x/2
        for i in range (len(listeProjectiles)):
            listeProjectiles[i].x += joueur.vitesse_x/2

    elif (direction == "gauche"):
        fond.x -= fond.vitesse
        joueur.x -= joueur_vitesse_x/2
        collines.x -= collines.vitesse/2
        for i in range (len(listeEnnemis)):
            listeEnnemis[i].x -= joueur.vitesse_x/2
        for i in range (len(listeProjectiles)):
            listeProjectiles[i].x -= joueur.vitesse_x/2

def actualiser():
    global joueur_tombe

    #le joueur touche le sol
    if(p1.collision): joueur_tombe = False
    #joueur ne touche pas le sol
    if (not p1.collision and not joueur.saut): joueur_tombe = True

    if(joueur_tombe):
        joueur.y += joueur.vitesse_y


def game_over():
    global listeEnnemis
    global listeProjectiles
    global jouer
    global perdu

    jouer = False
    perdu = True




            #TITRE ET CREATION DES OBJECTS

    #titre du jeu
pygame.display.set_caption("Game")

joueur = Joueur()
p1 = Plateforme(ecran_largeur, p_hauteur, ecran_hauteur - p_hauteur, 0)
collines = Decor(0 - ecran_largeur, 25, pygame.image.load("img/decor/fond2.png"))
fond = Decor(0 - ecran_largeur, 10, pygame.image.load("img/decor/fond.png").convert())
listeEnnemis = []
listeProjectiles = []





            #BOUCLE
while run:





    # Jeu en pause
    while (jouer == False):

        if commencer == False :
             pygame.draw.rect(ecran, (25,150,250), (0, 0, ecran_largeur, ecran_hauteur))

        if perdu == False :
            #bouton start
            pygame.draw.rect(ecran, (250,250,250), (zonestart))
            #bouton quitter
            pygame.draw.rect(ecran, (250,250,250), (zonequitte))


            for event in pygame.event.get():

                if event.type==pygame.MOUSEBUTTONDOWN:
                    #on a appuye sur le bouton play
                    if event.button == 1 and zonestart.collidepoint(event.pos):
                        print("start")
                        jouer = True
                        jeu = True
                        commencer = True

                if event.type==pygame.MOUSEBUTTONDOWN:
                    #on a appuye sur le bouton quitte
                    if event.button == 1 and zonequitte.collidepoint(event.pos):
                        print("quitte")
                        run = False
                        jouer = True
                        jeu = False

                if event.type == pygame.QUIT:
                    run = False
                    jouer = True
                    jeu = False

        if perdu == True:
            #bouton continuer
            pygame.draw.rect(ecran, (250,250,250), (zonecontinuer))

            myfont = pygame.font.SysFont("monospace", 100)
            texte = "Perdu"
            texte_display = myfont.render(str(texte), 1, (255,255,255))
            ecran.blit(texte_display, (550, 150))

            for event in pygame.event.get():

                if event.type==pygame.MOUSEBUTTONDOWN:
                    #on a appuye sur le bouton continuer
                    if event.button == 1 and zonecontinuer.collidepoint(event.pos):
                        commencer = False
                        perdu = False
                        temps = 500
                        listeEnnemis = []
                        listeProjectiles = []
                        round = 1
                        global round_liste
                        round_liste = [a,a,a,a,d]
                        global ennemis_vivants
                        ennemis_vivants = [a,a,a,a,d]
                        joueur.y = 200
                        joueur.x = ecran_milieu

        pygame.display.update()


    # Jeu en cours
    if jeu == True and jouer == True :





        #ANIMATION DU JOUEUR

        keys = pygame.key.get_pressed()

        #mouvement gauche
        if (keys[pygame.K_LEFT] and not joueur_baisse):

                #images du joueur
            #joueur.largeur = joueur_largeur_courir
            joueur_image = image_gauche[position_image_gauche]
            position_image_gauche = (position_image_gauche + 1)%6
            joueur.left = True
            joueur.right = False

            #si bord gauche n'est pas atteint
            if(collines.x + collines.vitesse < 0):
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
        elif (keys[pygame.K_RIGHT] and not joueur_baisse):
                #images du joueur
            #joueur.largeur = joueur_largeur_courir
            joueur_image = image_droite[position_image_droite]
            position_image_droite = (position_image_droite + 1)%6
            joueur.right = True
            joueur.left = False


            #si bord droit n'est pas atteint
            if(collines.x - collines.vitesse > 0-2*ecran_largeur):
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
                joueur_image = image_stand[position_image_stand//3]
                position_image_stand = (position_image_stand + 1)%15

            else:
                joueur_image = image_standL[position_image_stand//3]
                position_image_stand = (position_image_stand + 1)%15

            #si bord droit ou gauche ne sont pas atteints
            if(collines.x - collines.vitesse > 0-2*ecran_largeur and collines.x + collines.vitesse < 0):
                #si joueur à gauche du milieu de l'ecran
                if(joueur.x + joueur_vitesse_x < ecran_milieu):
                    camera_avance_vers("droite")

                #si joueur à droite du milieu de l'ecran
                elif(joueur.x - joueur_vitesse_x > ecran_milieu):
                    camera_avance_vers("gauche")


        #saut
        if (keys[pygame.K_UP] and not joueur_baisse and not joueur_tombe and not joueur.saut):
            joueur.saut = True
            joueur.vitesse_y = Y_MAX

        #se baisser
        if (keys[pygame.K_DOWN]):
            joueur_baisse = True
            if(not joueur.saut and joueur.y == p1.y - 80):
                joueur.hauteur = 40
                joueur.y = p1.y - 40
        else:
            joueur_baisse = False
            joueur.hauteur = 80
            if(not joueur.saut and joueur.y == p1.y - 40):
                joueur.y = p1.y - 80

        #animation coup
        if (keys[pygame.K_SPACE] and not joueur_baisse):

            #images du joueur
            #joueur.largeur = joueur_largeur_coup
            if (joueur.left):
                joueur_image = image_coup[position_image_coup]
                position_image_coup = (position_image_coup + 1)%5
                joueur.x -= 5
            else:
                joueur_image = image_coupR[position_image_coup]
                position_image_coup = (position_image_coup + 1)%5
                joueur.x += 5

            #detruire ennemi
            for i in range(len(listeEnnemis)-1,-1,-1):
                if(punch_collision(listeEnnemis[i].x,listeEnnemis[i].y,listeEnnemis[i].longueur,listeEnnemis[i].hauteur)):
                    del listeEnnemis[i]
                    del ennemis_vivants[0]






                    #AFFICHAGE & ACTUALISATION

        fond.actualiser()
        collines.actualiser()

        #pygame.draw.rect(ecran, (0,200,0), (zone_libre_x, 0, zone_libre_taille, ecran_hauteur))


        joueur.actualiser()

        actualiser()

        #pygame.draw.rect(ecran, (0,0,255), (joueur.hitbox))
        pygame.draw.rect(ecran, (0,255,0), (joueur.punch_hitbox))

        p1.actualiser()

        for i in range (len(listeEnnemis)-1,-1,-1):
            listeEnnemis[i].actualiser()

        for i in range (len(listeProjectiles)-1):
            listeProjectiles[i].actualiser()

        temps -= 10

        if len(round_liste) == 0 and len(ennemis_vivants) == 0:
            nouveau_round()

        myfont = pygame.font.SysFont("monospace", 50)
        texte = "Round " + str(round) + " : " + str(len(ennemis_vivants)) + " ennemis"
        texte_display = myfont.render(str(texte), 1, (255,255,255))
        ecran.blit(texte_display, (300, 50))

        if(temps < 0 and not len(round_liste) == 0):
            creer_ennemi()
            temps = 500

        print(len(round_liste))

        #bouton pause
        pygame.draw.rect(ecran, (250,250,250), (zonepause))

        #score
        myfont = pygame.font.SysFont("monospace", 60)
        score_display = myfont.render(str(score), 1, (255,255,0))
        ecran.blit(score_display, (50, 50))

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                #on a appuye sur le bouton pause
                if event.button == 1 and zonepause.collidepoint(event.pos):
                    print("pause")
                    jouer = False

            if event.type == pygame.QUIT:
                run = False


    #actualisation de l'écran
    pygame.display.update()

pygame.quit()
