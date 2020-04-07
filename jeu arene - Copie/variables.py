import pygame

    #icone du jeu
icone = pygame.image.load("img/hero/stand/standR.png")
pygame.display.set_icon(icone)

ennemi_image = pygame.image.load("img/enemy/stand/stand1.png")
ennemi_vitesse = 20
ennemi_hauteur = 80
ennemi_longueur = 48

coupL = False

    #taille de l'écran
ecran_hauteur = 720
ecran_largeur = 1288
ecran = pygame.display.set_mode((ecran_largeur, ecran_hauteur))

    #taille de l'arene
arene_hauteur = ecran_hauteur
arene_largeur = 3*ecran_hauteur

p_hauteur = 100

joueur_tombe = True

#saut_pas = vitesse du saut
saut_pas = 10
saut = False
saut_possible = False

    #fond d'ecran
fond_image = pygame.image.load("img/decor/decor/neonsky.png").convert()
building3_image = pygame.image.load("img/decor/decor/building3.png")
building1_image = pygame.image.load("img/decor/decor/building1.png")
building2_image = pygame.image.load("img/decor/decor/building2.png")
Platform_image = pygame.image.load("img/decor/decor/Plateforme.png")





    #zone libre
dans_zone_libre = True
zone_libre_taille = 300
zone_libre_x = ecran_largeur/2 - zone_libre_taille/2

    #joueur
joueur_image = pygame.image.load("img/hero/stand/standR.png")
joueur_largeur_courir = 100
joueur_largeur_debout = 50
joueur_largeur_coup = 70
joueur_hauteur = 130


ecran_milieu = ecran_largeur/2 - joueur_largeur_debout/2

joueur_vitesse_x = 40
joueur_vitesse_y_min = 5
joueur_vitesse_y_max = 70
joueur_vitesse_y = joueur_vitesse_y_min
joueur_y = 200
joueur_x = ecran_milieu

image_stand = [pygame.image.load("img/hero/stand/standR.png")]
image_standL = [pygame.image.load("img/hero/stand/standL.png")]
position_image_stand = 0
image_droite = [pygame.image.load("img/hero/runR/runR1.png"),
pygame.image.load("img/hero/runR/runR2.png"),
pygame.image.load("img/hero/runR/runR3.png"),
pygame.image.load("img/hero/runR/runR4.png"),
pygame.image.load("img/hero/runR/runR5.png"),
pygame.image.load("img/hero/runR/runR6.png"),
pygame.image.load("img/hero/runR/runR7.png"),
pygame.image.load("img/hero/runR/runR8.png")]
position_image_droite = 0
image_gauche = [pygame.image.load("img/hero/runL/runL1.png"),
pygame.image.load("img/hero/runL/runL2.png"),
pygame.image.load("img/hero/runL/runL3.png"),
pygame.image.load("img/hero/runL/runL4.png"),
pygame.image.load("img/hero/runL/runL5.png"),
pygame.image.load("img/hero/runL/runL6.png"),
pygame.image.load("img/hero/runL/runL7.png"),
pygame.image.load("img/hero/runL/runL8.png")]
position_image_gauche = 0
image_coup = [pygame.image.load("img/hero/hitL/hitL1.png"),
pygame.image.load("img/hero/hitL/hitL2.png"),
pygame.image.load("img/hero/hitL/hitL3.png"),
pygame.image.load("img/hero/hitL/hitL4.png"),
pygame.image.load("img/hero/hitL/hitL5.png"),
pygame.image.load("img/hero/hitL/hitL6.png"),
pygame.image.load("img/hero/hitL/hitL7.png"),
pygame.image.load("img/hero/hitL/hitL8.png")]

image_coupR = [pygame.image.load("img/hero/hitR/hitR1.png"),
pygame.image.load("img/hero/hitR/hitR2.png"),
pygame.image.load("img/hero/hitR/hitR3.png"),
pygame.image.load("img/hero/hitR/hitR4.png"),
pygame.image.load("img/hero/hitR/hitR5.png"),
pygame.image.load("img/hero/hitR/hitR6.png"),
pygame.image.load("img/hero/hitR/hitR7.png"),
pygame.image.load("img/hero/hitR/hitR8.png")]
position_image_coup = 0
#jtest = [0,1,2,3,4,5,6,7,8]
commencer = False
boutonstart_x = 400
boutonstart_y = 500
boutonstart_largeur = 200
boutonstart_hauteur = 100
boutonquitte_x = 800
boutonquitte_y = 500
boutonquitte_largeur = 200
boutonquitte_hauteur = 100
boutonpause_x = 1050
boutonpause_y = 50
boutonpause_largeur = 100
boutonpause_hauteur = 50

zonestart = pygame.Rect(boutonstart_x, boutonstart_y, boutonstart_largeur, boutonquitte_hauteur)
zonequitte = pygame.Rect(boutonquitte_x, boutonquitte_y, boutonquitte_largeur, boutonquitte_hauteur)
zonepause = pygame.Rect(boutonpause_x,boutonpause_y, boutonpause_largeur, boutonpause_hauteur)