import time
from pygame import *
from math import *
import random


init()
mixer.init()
fenetre = display.set_mode((1148, 688), RESIZABLE)
fond = image.load("pong.png").convert()
balle = image.load("balle.png").convert_alpha()
raquette1 = image.load("raquette.png").convert_alpha()
font = font.SysFont("broadway", 24, bold=False, italic=False)
fond3 = image.load("pong3.png").convert()
fond2 = image.load("pong2.png").convert()
fond1 = image.load("pong1.png").convert()
start1 = image.load("start1.png").convert()
optionmenu = image.load("options.png").convert()
optionmenu2 = image.load("optionmenu.png").convert()
difficultyoptions = image.load("difficultyoptions.png").convert()
bounce = mixer.Sound("bounce.mp3")
gamemodebg = image.load("gamemodebg.png").convert()

difficulty = 4
difficultymenu = False
changedifficulty = False
xp = 574
yp = 344
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
gamemodemenu = False
gamemode = 0

while continuer == 2:
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    keyb1 = key.get_pressed()
    if keyb1[K_RETURN]:
        continuer = 1
    if keyb1[K_o]:
        menu = True
        while menu:
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0
            keyb2 = key.get_pressed()
            if keyb2[K_y]:
                optionmenu = image.load("optionsia.png").convert()
                changedifficulty = True
                IA = True
            if keyb2[K_a] and gamemode != 2:
                changemenu = True
                while changemenu:
                    for evenements in event.get():
                        if evenements.type == QUIT:
                            continuer = 0
                    keyb2 = key.get_pressed()
                    fenetre.blit(optionmenu2, (0, 0))
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
                time.wait(200)
            if changedifficulty == True:
                if keyb2[K_e]:
                    difficultymenu = True
                    while difficultymenu == True:
                        for evenements in event.get():
                            if evenements.type == QUIT:
                                continuer = 0
                        keyb2 = key.get_pressed()
                        fenetre.blit(difficultyoptions, (0, 0))
                        display.flip()
                        if keyb2[K_1]:
                            difficulty = 1
                            difficultymenu = False
                        if keyb2[K_2]:
                            difficulty = 2
                            difficultymenu = False
                        if keyb2[K_3]:
                            difficulty = 3
                            difficultymenu = False
                        if keyb2[K_4]:
                            difficulty = 4
                            difficultymenu = False
                        if keyb2[K_5]:
                            difficulty = 5
                            difficultymenu = False
                        if keyb2[K_6]:
                            difficulty = 6
                            difficultymenu = False
                        if keyb2[K_7]:
                            difficulty = 7
                            difficultymenu = False
                        if keyb2[K_8]:
                            difficulty = 8
                            difficultymenu = False
                        if keyb2[K_9]:
                            difficulty = 9
                            difficultymenu = False

            fenetre.blit(optionmenu, (0, 0))
            display.flip()
    if keyb1[K_m]:
        gamemodemenu = True
        while gamemodemenu:
            fenetre.blit(gamemodebg, (0, 0))
            display.flip()
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0
            keyb2 = key.get_pressed()
            if keyb2[K_1]:
                gamemode = 1
                gamemodemenu = False
            if keyb2[K_2]:
                victory = 1
                gamemode = 2
                gamemodemenu = False
            if keyb2[K_RETURN]:
                gamemodemenu = False
                time.wait(200)

    fenetre.blit(start1, (0, 0))
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
    if gamemode == 1:
        deplacement_x = random.choice([-10,10])
        while continuer == 1:
            time.Clock().tick(500)
            collision = False
            vitesse = int(vitesse)
            j1 = int(j1)
            j2 = int(j2)
            if j1 == victory:
                bg1 = image.load("bg1.png")
                fenetre.blit(bg1, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
                display.flip()
                time.wait(5000)
                break
            if j2 == victory:
                bg2 = image.load("bg2.png")
                fenetre.blit(bg2, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
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
                deplacement_x = random.choice([-10, 10])
                speed = 0
                vitesse = 10
                deplacement_y = 1

            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0

            if yp <= 688 - raquette1.get_size()[1]:
                if ry2 < yp:
                    ry2 += 1 + (difficulty / 10)
                if ry2 > yp:
                    ry2 -= 1 + (difficulty / 10)
            elif yp > 688 - raquette1.get_size()[1]:
                if ry2 < 688 - raquette1.get_size()[1] and yp > 688 - raquette1.get_size()[1]:
                    ry2 += 1 + (difficulty / 10)

            keyb = key.get_pressed()

            if yp <= 688 - raquette1.get_size()[1]:
                if ry2 < yp:
                    ry2 += 1 + (difficulty/10)
                if ry2 > yp:
                    ry2 -= 1 + (difficulty/10)
            elif yp > 688 - raquette1.get_size()[1]:
                if ry2 < 688 - raquette1.get_size()[1] and yp > 688 - raquette1.get_size()[1]:
                    ry2 += 1 + (difficulty/10)

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
            if yp > fond.get_size()[1] - balle.get_size()[1]:
                yp = fond.get_size()[1] - balle.get_size()[1]
            if yp <= 0:
                yp = 0
            if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                deplacement_x = 10
                collision = True
                if yp > ry1:
                    deplacement_y = -0.75 - (0.0075 * abs(((yp - ry1) - 134))) if ((yp - ry1) - 134) < 0 else 0.75 + (
                            0.0075 * ((yp - ry1) - 134))
                mixer.Sound.play(bounce)
            if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                deplacement_x = -10
                collision = True
                if yp > ry2:
                    deplacement_y = -0.75 - (0.0075 * abs(((yp - ry2) - 134))) if ((yp - ry2) - 134) < 0 else 0.75 + (
                            0.0075 * ((yp - ry2) - 134))
                mixer.Sound.play(bounce)

            fenetre.blit(fond, (0, 0))
            fenetre.blit(balle, (xp, yp))
            fenetre.blit(raquette1, (rx1, ry1))
            fenetre.blit(raquette1, (rx2, ry2))
            j1 = str(j1)
            j2 = str(j2)
            vitesse = str(abs(deplacement_x))
            chaine = str(
                "                           Joueur 1 : " + j1 + "                           Vitesse : " + vitesse + "                                   IA : " + j2)
            text = font.render(chaine, True, (255, 255, 255))
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
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - "+j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630,435))
                display.flip()
                time.wait(5000)
                break
            if j2 == victory:
                bg2 = image.load("bg2.png")
                fenetre.blit(bg2, (0,0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
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

            speed += 1
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0

            ### IA
            if yp <= 688 - raquette1.get_size()[1]:
                if ry2 < yp:
                    ry2 += 1 + (difficulty/10)
                if ry2 > yp:
                    ry2 -= 1 + (difficulty/10)
            elif yp > 688 - raquette1.get_size()[1]:
                if ry2 < 688 - raquette1.get_size()[1] and yp > 688 - raquette1.get_size()[1]:
                    ry2 += 1 + (difficulty/10)

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
            if yp > fond.get_size()[1] - balle.get_size()[1]:
                yp = fond.get_size()[1] - balle.get_size()[1]
            if yp <= 0:
                yp = 0
            if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                if speed >= 3000:
                    deplacement_x = speed // 1000
                else:
                    deplacement_x = 2
                collision = True
                if yp > ry1:
                    deplacement_y = -0.75-(0.0075 * abs(((yp - ry1)-134))) if ((yp - ry1)-134) < 0 else 0.75+(0.0075 * ((yp - ry1)-134))

                mixer.Sound.play(bounce)
            if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                if speed >= 3000:
                    deplacement_x = -(speed // 1000)
                else:
                    deplacement_x = -2
                collision = True
                if yp > ry2:
                    deplacement_y = -0.75-(0.0075 * abs(((yp - ry2)-134))) if ((yp - ry2)-134) < 0 else 0.75+(0.0075 * ((yp - ry2)-134))
                mixer.Sound.play(bounce)
            if speed >= 3000:
                if deplacement_x != -deplacement_x and collision == False:
                    if deplacement_x < 0:
                        deplacement_x = -(speed // 1000)
                        vitesse = abs(deplacement_x)
                    else:
                        deplacement_x = speed // 1000
                        vitesse = abs(deplacement_x)

            fenetre.blit(fond, (0, 0))
            fenetre.blit(balle, (xp, yp))
            fenetre.blit(raquette1, (rx1, ry1))
            fenetre.blit(raquette1, (rx2, ry2))
            j1 = str(j1)
            j2 = str(j2)
            vitesse = str(vitesse)
            chaine = str("                           Joueur 1 : " + j1 + "                           Vitesse : " + vitesse + "                                   IA : " + j2)
            text = font.render(chaine, True, (255, 255, 255))
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
    if gamemode == 1:
        deplacement_x = random.choice([-10,10])
        while continuer == 1:
            time.Clock().tick(500)
            collision = False
            vitesse = int(vitesse)
            j1 = int(j1)
            j2 = int(j2)
            if j1 == victory:
                bg1 = image.load("bg1.png")
                fenetre.blit(bg1, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
                display.flip()
                time.wait(5000)
                break
            if j2 == victory:
                bg2 = image.load("bg2.png")
                fenetre.blit(bg2, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
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
                deplacement_x = random.choice([-10, 10])
                speed = 0
                vitesse = 10
                deplacement_y = 1

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
            if ry1 >= 688 - raquette1.get_size()[1]:
                ry1 -= 2
            if ry2 >= 688 - raquette1.get_size()[1]:
                ry2 -= 2

            xp += deplacement_x
            yp += deplacement_y
            if yp > fond.get_size()[1] - balle.get_size()[1] or yp <= 0:
                deplacement_y = -deplacement_y
            if yp > fond.get_size()[1] - balle.get_size()[1]:
                yp = fond.get_size()[1] - balle.get_size()[1]
            if yp <= 0:
                yp = 0
            if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                deplacement_x = 10
                collision = True
                if yp > ry1:
                    deplacement_y = -0.75 - (0.0075 * abs(((yp - ry1) - 134))) if ((yp - ry1) - 134) < 0 else 0.75 + (
                            0.0075 * ((yp - ry1) - 134))
                mixer.Sound.play(bounce)
            if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp, yp), balle.get_size())):
                deplacement_x = -10
                collision = True
                if yp > ry2:
                    deplacement_y = -0.75 - (0.0075 * abs(((yp - ry2) - 134))) if ((yp - ry2) - 134) < 0 else 0.75 + (
                            0.0075 * ((yp - ry2) - 134))
                mixer.Sound.play(bounce)

            fenetre.blit(fond, (0, 0))
            fenetre.blit(balle, (xp, yp))
            fenetre.blit(raquette1, (rx1, ry1))
            fenetre.blit(raquette1, (rx2, ry2))
            j1 = str(j1)
            j2 = str(j2)
            vitesse = str(abs(deplacement_x))
            chaine = str(
                "                           Joueur 1 : " + j1 + "                           Vitesse : " + vitesse + "                                   Joueur 2 : " + j2)
            text = font.render(chaine, True, (255, 255, 255))
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
                fenetre.blit(bg1, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
                display.flip()
                time.wait(5000)
                break
            if j2 == victory:
                bg2 = image.load("bg2.png")
                fenetre.blit(bg2, (0, 0))
                j1 = str(j1)
                j2 = str(j2)
                chaine1 = str(j1 + " - " + j2)
                text1 = font.render(chaine1, True, (255, 255, 255))
                fenetre.blit(text1, (630, 435))
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
            if yp > fond.get_size()[1] - balle.get_size()[1]:
                yp = fond.get_size()[1] - balle.get_size()[1]
            if yp <= 0:
                yp = 0
            if Rect((rx1, ry1), raquette1.get_size()).colliderect(Rect((xp,yp),balle.get_size())):
                if speed >= 3000:
                    deplacement_x = speed//1000
                else:
                    deplacement_x = 2
                collision = True
                if yp > ry1:
                    deplacement_y = -0.75-(0.0075 * abs(((yp - ry1)-134))) if ((yp - ry1)-134) < 0 else 0.75+(0.0075 * ((yp - ry1)-134))
                mixer.Sound.play(bounce)
            if Rect((rx2, ry2), raquette1.get_size()).colliderect(Rect((xp,yp),balle.get_size())):
                if speed >= 3000:
                    deplacement_x = -(speed//1000)
                else:
                    deplacement_x = -2
                collision = True
                if yp > ry2:
                    deplacement_y = -0.75-(0.0075 * abs(((yp - ry2)-134))) if ((yp - ry2)-134) < 0 else 0.75+(0.0075 * ((yp - ry2)-134))
                mixer.Sound.play(bounce)
            if speed >= 3000:
                if deplacement_x != -deplacement_x and collision == False:
                    if deplacement_x < 0:
                        deplacement_x = -(speed // 1000)
                        vitesse = abs(deplacement_x)
                    else:
                        deplacement_x = speed // 1000
                        vitesse = abs(deplacement_x)

            fenetre.blit(fond, (0, 0))
            fenetre.blit(balle, (xp, yp))
            fenetre.blit(raquette1, (rx1, ry1))
            fenetre.blit(raquette1, (rx2, ry2))
            j1 = str(j1)
            j2 = str(j2)
            vitesse = str(vitesse)
            chaine = str("                           Joueur 1 : " + j1 + "                           Vitesse : " + vitesse + "                                   Joueur 2 : " + j2)
            text = font.render(chaine, True, (255, 255, 255))
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
