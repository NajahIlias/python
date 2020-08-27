import pygame
import random
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")
gameStarted = False

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
    if hahmot:
        for hahmo in hahmot:
            if hahmo[3] == True:
                kuva = pygame.image.load(hahmo[0]).convert()
                naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset):
    if hahmot:
        x1 = hahmot[0][1]
        x2 = hahmot[0][1] + 100
        y1 = hahmot[0][2]
        y2 = hahmot[0][2] + 100
        hahRect = pygame.Rect(x1, y1, x2-x1, y2-y1)
    for vihollinen in viholliset:
        vx1 = vihollinen[1]
        vx2 = vihollinen[1] + 75
        vy1 = vihollinen[2]
        vy2 = vihollinen[2] + 75
        vihRect = pygame.Rect(vx1, vy1, vx2-vx1, vy2-vy1)
        if hahmot: 
            if hahRect.colliderect(vihRect):
                print("lol")
                del hahmot[0]
            else:
                print("no collision")
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            if vihollinen[1] > 640:
                vihollinen[1] = 0
                vihollinen[2] = random.randint(0, 400)
            else:
                    vihollinen[1] += 4
    if hahmot:
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_SPACE and gameStarted == False:
                hahmot[0][3] = True
                for vihollinen in viholliset:
                    vihollinen[3] = True
            elif tapahtuma.key == pygame.K_RIGHT:
                päähahmo = hahmot[0]
                if päähahmo[1] >= 540:
                    print("cant go further")
                else:
                    päähahmo[1] += 50
            elif tapahtuma.key == pygame.K_LEFT:
                päähahmo = hahmot[0]
                if päähahmo[1] <= 0:
                    print("cant go further")
                else:
                    päähahmo[1] -= 50
            elif tapahtuma.key == pygame.K_UP:
                päähahmo = hahmot[0]
                if päähahmo[2] <= 0:
                    print("cant go further")
                else:
                    päähahmo[2] -= 50
            elif tapahtuma.key == pygame.K_DOWN:
                päähahmo = hahmot[0]
                if päähahmo[2] >= 300:
                    print("cant go further")
                else:
                    päähahmo[2] += 50


def main():
    kissahahmo = ["cat.png", 300, 100, False]
    alienhahmo = ["alien.png", 0, 200, False]
    alienhahmo2 = ["alien.png", 0, 300, False]
    alienhahmo3 = ["alien.png", 0, 100, False]



    hahmot = [kissahahmo]
    viholliset = [alienhahmo, alienhahmo2, alienhahmo3]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)


main()