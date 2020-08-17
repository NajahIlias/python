import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Ensimmäinen peli")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

main()