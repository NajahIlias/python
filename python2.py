#import pygame

#naytto = pygame.display.set_mode((640, 400))
#pygame.display.set_caption("Ensimmäinen peli")

#def main():
    #while True:
   #     tapahtuma = pygame.event.poll()
  #      if tapahtuma.type == pygame.QUIT:
 #           break
#
#main()




#import pygame

#naytto = pygame.display.set_mode((640, 400))
#pygame.display.set_caption("Piirtäminen")

#def main():
 #   while True:
  #      tapahtuma = pygame.event.poll()
   #     if tapahtuma.type == pygame.QUIT:
    #        break

     #   naytto.fill((0, 0, 0))
      #  pygame.draw.line(naytto, (0, 0, 255), (0,0), (640, 400))
       # pygame.draw.line(naytto, (0, 255, 0), (0, 400), (640, 0))   
        #pygame.display.flip()

#main()




#import pygame

#naytto = pygame.display.set_mode((640, 400))
#pygame.display.set_caption("Piirtäminen")

#def main():
 #   while True:
  #      tapahtuma = pygame.event.poll()
   #     if tapahtuma.type == pygame.QUIT:
    #        break

     #   naytto.fill((0, 0, 0))
      #  pygame.draw.rect(naytto, (255, 0, 0), (100, 50, 150, 200))
       # pygame.display.flip()

#main()




#import pygame

#naytto = pygame.display.set_mode((640, 400))
#pygame.display.set_caption("Piirtäminen")

#def main():
 #   while True:
  #      tapahtuma = pygame.event.poll()
   #     if tapahtuma.type == pygame.QUIT:
    #        break

     #   naytto.fill((0, 0, 0))
      #  pygame.draw.circle(naytto, (255, 255, 0), (350, 150), 40)
       # pygame.display.flip()

#main()







import pygame
import random

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")
kuva = pygame.image.load("cat.png").convert()

def main():

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        naytto.blit(kuva, (400, 400))
        pygame.display.flip()
        x = random.randint(1, 640)
        y = random.randint(1, 400)
        piirraKuva(kuva, x, y)
def piirraKuva(kuva, x, y):
    naytto.blit(kuva, (x, y))
    pygame.display.flip()
main()
