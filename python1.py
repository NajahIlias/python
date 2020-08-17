#import random
#import string

#print ("Silmäluku:", random.randint(1, 6))


#a = random.randint(1,2)
#if a > 1:
  #  print("Tulos: kruuna")
#else:
    #print("Tulos: klaava")


#def random_char(y):
 #      return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
#print ("Salasana:", random_char(8))

#luvut = [1, 2, 3, 4, 5, 6, 7, 8]

#def sekoitaLista():
#    random.shuffle(luvut)

#def tulostaLista():
#    print(luvut)

#sekoitaLista()
#tulostaLista()


#list = []
#def EnemyList():
 #   for x in range(0,1000):
  #      y = str(random.randint(1, 101))
   #     y += "," 
    #    y += str(random.randint(1,101))
     #   list.append(y)
#EnemyList()
#print(list)

#lista = [1, 3, 5, 4]
#lista.sort()
#print(lista)

def Pistelista():
  player = ""
  highest = 0
  while True:
    print("Enter your name")
    x = input()
    if x == "lopeta":
       print(player,",", highest)
       break
    print("Enter your score")
    y = input()
    if int(y) > highest:
      highest = int(y)
      player = x

#Pistelista()


