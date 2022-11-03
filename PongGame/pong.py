import time

from pygame import *
from math import *
import random

# ia : ry2 = yp, faut quil soit pas imbattable,
# [DONE] barres qui ne dépassent pas
# [DONE] barres plus petites
# [DONE] balle qui accélère
# [DONE] score apres 5 points
# [DONE] jouer a la souris
# [DONE] meilleurs angles
# angles selon la position de la balle sur la barre
# [DONE] choisir combien de points max avant la fin de la partie

init()
fenetre = display.set_mode((1148, 688), RESIZABLE)

fond = image.load("pong.png").convert()

balle = image.load("balle.png").convert_alpha()

raquette1 = image.load("raquette.png").convert_alpha()

font = font.SysFont("broadway", 24, bold=True, italic=False)

fond3 = image.load("pong3.png").convert()
fond2 = image.load("pong2.png").convert()
fond1 = image.load("pong1.png").convert()

start1 = image.load("start1.png").convert()
optionmenu = image.load("options.png").convert()
optionmenu2 = image.load("optionmenu.png").convert()

xp = 574
yp = 344
comp = 0
continuer = 2
deplacement_x = random.choice([-2,2])
deplacement_y = 1
rx1 = 20
ry1 = 200
rx2 = 1100
ry2 = 200
speed = 0
j1 = 0
j2 = 0
victory = 5
z = 0
vitesse = 2
IA = False
menu = False
while continuer == 2:
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    keyb1 = key.get_pressed()
    if keyb1[K_RETURN]:
        IA = False
        continuer = 1
    if keyb1[K_o]:
        menu = True
        continuer = 0
    fenetre.blit(start1, (0, 0))
    display.flip()

while menu:
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    keyb2 = key.get_pressed()
    if keyb2[K_y]:
        IA = True
        print(IA)
    if keyb2[K_a]:
        changemenu = True
        print("a")
        while changemenu:
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0
            keyb2 = key.get_pressed()
            fenetre.blit(optionmenu2, (0,0))
            display.flip()
            if keyb2[K_1]:
                victory = 1
                changemenu = False
            if keyb2[K_2]:
                victory = 2
                changemenu = False
            if keyb2[K_3]:
                victory = 3
                changemenu = False
            if keyb2[K_4]:
                victory = 4
                changemenu = False
            if keyb2[K_5]:
                victory = 5
                changemenu = False
            if keyb2[K_6]:
                victory = 6
                changemenu = False
            if keyb2[K_7]:
                victory = 7
                changemenu = False
            if keyb2[K_8]:
                victory = 8
                changemenu = False
            if keyb2[K_9]:
                victory = 9
                changemenu = False
    if keyb2[K_RETURN]:
        menu = False
        continuer = 1
    fenetre.blit(optionmenu, (0,0))
    display.flip()



fenetre.blit(fond3, (0,0))
display.flip()
time.wait(1000)

fenetre.blit(fond2, (0, 0))
display.flip()
time.wait(1000)

fenetre.blit(fond1, (0,0))
display.flip()
time.wait(1000)

fenetre.blit(fond, (0,0))
display.flip()
time.wait(1000)

if IA == True:
    while continuer == 1:
        time.Clock().tick(500)
        collision = False
        vitesse = int(vitesse)
        j1 = int(j1)
        j2 = int(j2)
        if j1 == victory:
            bg1 = image.load("bg1.png")
            fenetre.blit(bg1, (0,0))
            display.flip()
            time.wait(5000)
            break
        if j2 == victory:
            bg2 = image.load("bg2.png")
            fenetre.blit(bg2, (0,0))
            display.flip()
            time.wait(5000)
            break
        if ((j1 != 0 and j1 < victory) or (j2 != 0 and j2 < victory)) and z > 0:
            del balle
            time.wait(1000)

            fenetre.blit(fond3, (0, 0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond2, (0, 0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond1, (0, 0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond, (0, 0))
            display.flip()
            time.wait(1000)
            balle = image.load("balle.png").convert_alpha()
            fenetre.blit(balle, (0, 0))
            rx1 = 20
            ry1 = 200
            rx2 = 1100
            ry2 = 200
            display.flip()
            z = 0
            deplacement_x = random.choice([-2,2])
            speed = 0
            vitesse = 2
            deplacement_y = 1

        comp += 1
        speed += 1
        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0

        ### IA
        if yp <= 688 - raquette1.get_size()[1]:
            ry2 = yp
        elif yp > 688 - raquette1.get_size()[1]:
            ry2 = 688 - raquette1.get_size()[1]

        keyb = key.get_pressed()


        if mouse.get_pressed()[0] == True:
            if ry1 >= 0 and mouse.get_pos()[1] <= 688 - raquette1.get_size()[1]:
                ry1 = mouse.get_pos()[1]
            elif ry1 < 0:
                ry1 = 0
            elif mouse.get_pos()[1] > 688 - raquette1.get_size()[1]:
                ry1 = 688 - raquette1.get_size()[1]

        if keyb[K_w]:
            ry1 -= 2
        if keyb[K_s]:
            ry1 += 2
        if ry1 <= 0:
            ry1 += 2
        if ry2 <= 0:
            ry2 += 2
        if ry1 >= 688 - raquette1.get_size()[1]:
            ry1 -= 2
        if ry2 >= 688 - raquette1.get_size()[1]:
            ry2 -= 2


        xp += deplacement_x
        yp += deplacement_y
        if yp > fond.get_size()[1] - balle.get_size()[1] or yp <= 0:
            deplacement_y = -deplacement_y

        if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
            if speed >= 3000:
                deplacement_x = speed // 1000
            else:
                deplacement_x = 2
            collision = True
            deplacement_y = random.uniform(-2, 2)
            while -1 <= deplacement_y <= 1:
                deplacement_y = random.uniform(-2, 2)
        if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
            if speed >= 3000:
                deplacement_x = -(speed // 1000)
            else:
                deplacement_x = -2
            collision = True
            deplacement_y = random.uniform(-2, 2)
            while -1 <= deplacement_y <= 1:
                deplacement_y = random.uniform(-2, 2)
        if speed >= 3000:
            if deplacement_x != -deplacement_x and collision == False:
                if deplacement_x < 0:
                    deplacement_x = -(speed // 1000)
                    vitesse = abs(deplacement_x)
                else:
                    deplacement_x = speed // 1000
                    vitesse = abs(deplacement_x)
        #            print(speed // 1000)
        #            print("__________\n")
        #            print(deplacement_x)
        #        print(deplacement_x)

        fenetre.blit(fond, (0, 0))
        fenetre.blit(balle, (xp, yp))
        fenetre.blit(raquette1, (rx1, ry1))
        fenetre.blit(raquette1, (rx2, ry2))
        j1 = str(j1)
        j2 = str(j2)
        vitesse = str(vitesse)
        chaine = str(
            "                                                     Joueur 1 : " + j1 + "                           Vitesse : " + vitesse + "                                   IA : " + j2)
        # chaine = str(
        #    "                                                                  Joueur 1 : " + j1 + "                                                 Joueur 2 : " + j2)

        text = font.render(chaine, True, (255, 255, 255))  # pour créer l'objet texte qui est une surface pygame
        fenetre.blit(text, (30, 30))
        display.flip()
        if xp < (0 - balle.get_size()[0]):
            j2 = int(j2)
            j2 += 1
            xp = 574
            yp = 344
            z = 1
            continue
        if xp >= 1148:
            j1 = int(j1)
            j1 += 1
            xp = 574
            yp = 344
            z = 1
            continue
else:
    while continuer == 1:
        time.Clock().tick(500)
        collision = False
        vitesse = int(vitesse)
        j1 = int(j1)
        j2 = int(j2)
        if j1 == victory:
            bg1 = image.load("bg1.png")
            fenetre.blit(bg1, (0,0))
            display.flip()
            time.wait(5000)
            break
        if j2 == victory:
            bg2 = image.load("bg2.png")
            fenetre.blit(bg2, (0,0))
            display.flip()
            time.wait(5000)
            break
        if ((j1 !=0 and j1 <victory) or (j2 !=0 and j2<victory)) and z>0:
            del balle
            time.wait(1000)

            fenetre.blit(fond3, (0,0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond2, (0, 0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond1, (0,0))
            display.flip()
            time.wait(1000)

            fenetre.blit(fond, (0,0))
            display.flip()
            time.wait(1000)
            balle = image.load("balle.png").convert_alpha()
            fenetre.blit(balle, (0,0))
            rx1 = 20
            ry1 = 200
            rx2 = 1100
            ry2 = 200
            display.flip()
            z = 0
            deplacement_x = random.choice([-2,2])
            speed = 0
            vitesse = 2
            deplacement_y = 1

        comp += 1
        speed += 1
        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0

        keyb = key.get_pressed()

        if mouse.get_pressed()[0] == True:
            if ry1 >= 0 and mouse.get_pos()[1] <= 688 - raquette1.get_size()[1]:
                ry1 = mouse.get_pos()[1]
            elif ry1 < 0:
                ry1 = 0
            elif mouse.get_pos()[1] > 688 - raquette1.get_size()[1]:
                ry1 = 688 - raquette1.get_size()[1]
        if keyb[K_w]:
            ry1 -= 2
        if keyb[K_s]:
            ry1 += 2
        if keyb[K_UP]:
            ry2 -= 2
        if keyb[K_DOWN]:
            ry2 += 2
        if ry1 <= 0:
            ry1 += 2
        if ry2 <= 0:
            ry2 += 2
        if ry1 >= 688-raquette1.get_size()[1]:
            ry1 -= 2
        if ry2 >= 688-raquette1.get_size()[1]:
            ry2 -= 2

        xp += deplacement_x
        yp += deplacement_y
        if yp > fond.get_size()[1] - balle.get_size()[1] or yp <= 0:
            deplacement_y = -deplacement_y

        if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp,yp),balle.get_size())):
            if speed >= 3000:
                deplacement_x = speed//1000
            else:
                deplacement_x = 2
            collision = True
            deplacement_y = random.uniform(-2, 2)
            while -1 <= deplacement_y <= 1:
                deplacement_y = random.uniform(-2, 2)
        if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp,yp),balle.get_size())):
            if speed >= 3000:
                deplacement_x = -(speed//1000)
            else:
                deplacement_x = -2
            collision = True
            deplacement_y = random.uniform(-2, 2)
            while -1 <= deplacement_y <= 1:
                deplacement_y = random.uniform(-2, 2)
        if speed >= 3000:
            if deplacement_x != -deplacement_x and collision == False:
                if deplacement_x < 0:
                    deplacement_x = -(speed // 1000)
                    vitesse = abs(deplacement_x)
                else:
                    deplacement_x = speed // 1000
                    vitesse = abs(deplacement_x)
    #            print(speed // 1000)
    #            print("__________\n")
    #            print(deplacement_x)
    #        print(deplacement_x)

        fenetre.blit(fond, (0, 0))
        fenetre.blit(balle, (xp, yp))
        fenetre.blit(raquette1, (rx1, ry1))
        fenetre.blit(raquette1, (rx2, ry2))
        j1 = str(j1)
        j2 = str(j2)
        vitesse = str(vitesse)
        chaine = str(
            "                                                     Joueur 1 : " + j1 + "                           Vitesse : " +vitesse+"                                   Joueur 2 : " + j2)
        #chaine = str(
        #    "                                                                  Joueur 1 : " + j1 + "                                                 Joueur 2 : " + j2)

        text = font.render(chaine, True, (255, 255, 255))  # pour créer l'objet texte qui est une surface pygame
        fenetre.blit(text, (30, 30))
        display.flip()


        if xp < (0-balle.get_size()[0]):
            j2 = int(j2)
            j2 += 1
            xp = 574
            yp = 344
            z = 1
            continue

        if xp >= 1148:
            j1 =  int(j1)
            j1 += 1
            xp = 574
            yp = 344
            z = 1
            continue

quit()
