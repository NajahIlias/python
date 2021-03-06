import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma):
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo = hahmot[0]
            if päähahmo[1] >= 540:
                print("cant go further")
            else:
             päähahmo[1] += 10


def main():
    kissahahmo = ["cat.png", 100, 100, False]
    alienhahmo = ["alien.png", 200, 200, False]

    hahmot = [kissahahmo, alienhahmo]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma)
        piirtaminen(naytto, hahmot)


main()