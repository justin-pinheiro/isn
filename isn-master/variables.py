import pygame

    #icone du jeu
icone = pygame.image.load("stand/straightR.png")
pygame.display.set_icon(icone)
ennemi_image = pygame.image.load("img/enemy/stand/stand1.png")
ennemi_vitesse = 20
ennemi_hauteur = 80
ennemi_longueur = 48


    #plateforme
p_hauteur = 100


temps = 1000

    #saut
#saut_pas = vitesse du saut
saut_pas = 10
saut = False
saut_possible = False

    #écran
ecran_hauteur = 720
ecran_largeur = 1278
ecran = pygame.display.set_mode((ecran_largeur, ecran_hauteur))
ecran_milieu = ecran_largeur/2 - 50/2

    #taille de l'arene
arene_hauteur = ecran_hauteur
arene_largeur = 3*ecran_hauteur

    #fond d'ecran
fond_image = pygame.image.load("img/herobackground/decor/neonsky.png").convert_alpha()
collines_image = pygame.image.load("img/herobackground/decor/Plateforme.png").convert_alpha()
building1_image = pygame.image.load("img/herobackground/decor/building1.png").convert_alpha()
building2_image = pygame.image.load("img/herobackground/decor/building2.png").convert_alpha()
building3_image = pygame.image.load("img/herobackground/decor/building3.png").convert_alpha()
fond_x = 0 - ecran_largeur
fond_vitesse = 8

    #zone libre
dans_zone_libre = True
zone_libre_taille = 300
zone_libre_x = ecran_largeur/2 - zone_libre_taille/2

    #joueur
joueur_image = pygame.image.load("stand/straightR.png")
joueur_largeur_courir = 100
joueur_largeur_debout = 50
joueur_largeur_coup = 70
joueur_hauteur = 0
joueur_tombe = True
coup = False
joueur_vitesse_x = 30
Y_MIN = 5
Y_MAX = 70
joueur_vitesse_y = Y_MIN
joueur_y = 0
joueur_x = ecran_milieu
joueur_baisse = False


    #images
image_stand = pygame.image.load("stand/straightR.png")
image_standL = pygame.image.load("stand/straightL.png")
image_droite = [pygame.image.load("img/herobackground/hero/runR/runR1.png"),
pygame.image.load("img/herobackground/hero/runR/runR2.png"),
pygame.image.load("img/herobackground/hero/runR/runR3.png"),
pygame.image.load("img/herobackground/hero/runR/runR4.png"),
pygame.image.load("img/herobackground/hero/runR/runR5.png"),
pygame.image.load("img/herobackground/hero/runR/runR6.png"),
pygame.image.load("img/herobackground/hero/runR/runR7.png"),
pygame.image.load("img/herobackground/hero/runR/runR8.png")]
position_image_droite = 0
image_gauche = [pygame.image.load("img/herobackground/hero/runL/runL1.png"),
pygame.image.load("img/herobackground/hero/runL/runL2.png"),
pygame.image.load("img/herobackground/hero/runL/runL3.png"),
pygame.image.load("img/herobackground/hero/runL/runL4.png"),
pygame.image.load("img/herobackground/hero/runL/runL5.png"),
pygame.image.load("img/herobackground/hero/runL/runL6.png"),
pygame.image.load("img/herobackground/hero/runL/runL7.png"),
pygame.image.load("img/herobackground/hero/runL/runL8.png")]
position_image_gauche = 0
image_coup = [pygame.image.load("img/herobackground/hero/hitR/hitR1.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR2.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR3.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR4.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR5.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR6.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR7.png"),
pygame.image.load("img/herobackground/hero/hitR/hitR8.png")]
image_coupR = [pygame.image.load("img/herobackground/hero/hitL/hitL1.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL2.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL3.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL4.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL5.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL6.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL7.png"),
pygame.image.load("img/herobackground/hero/hitL/hitL8.png")]
position_image_coup = 0

perdu = False
commencer = False

zonestart = pygame.Rect(400, 500, 200, 100)
zonequitte = pygame.Rect(800, 500, 200, 100)
zonepause = pygame.Rect(1050, 50, 100, 50)
zonecontinuer = pygame.Rect(600, 300, 200, 100)

jouer = False #pour bouton
score = 0
texte = "Perdu"


round = 1
a = "aggressif"
d = "distant"
s = "sauvage"
round1 = [a,a,a,a,d]
round2 = [a,a,d,a,a,d,a,a,d,a]
round3 = [d,d,a,d,a,a,a,d,d,a]
round4 = [a,d,d,a,d,a,d,d,d,d,a,d,a,d,s]
round5 = [a,d,d,a,s,a,d,d,d,d,d,s,a,d,s]

round_liste = [a,a,a,a,d]
ennemis_vivants = [a,a,a,a,d]

