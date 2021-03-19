import pygame
from pygame.locals import *
import random
from pylab import math
import time

#Starter programmer
pygame.init()

#Skjermen
bredde = 800
høyde = 600
vindu = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Space invaders")



#Farger
YELLOW = (255, 255,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Bakgrunn
bg = pygame.image.load("./assets/sort-bakgrunn.png")
bg = pygame.transform.scale(bg, (bredde, høyde))
vindu.blit(bg, (0,0))
start_bg = pygame.image.load("./assets/startbilde.png")


#Figurer
RØDSKIP = pygame.image.load("./assets/rød-skip.png")
BLÅSKIP = pygame.image.load("./assets/blå-skip.png")
GRØNNSKIP = pygame.image.load("./assets/grønn-skip.png")
ROMVESEN = pygame.image.load("./assets/slemming.png")

RØDLASER = pygame.image.load("./assets/rød-laser.png")
BLÅLASER = pygame.image.load("./assets/blå-laser.png")
GRØNLASER = pygame.image.load("./assets/grønn-laser.png")


#Lager spiller
SPILLER = pygame.image.load("./assets/gul-skip.png")
spillerx = 370
spillery = 470
vindu.blit(SPILLER, (spillerx, spillery))
spillerx_forandring = 0
fart = 4

#Laseren   ready = du kan ikke se laseren,  fire = du kan se laseren
SPILLERLASER = pygame.image.load("./assets/gul-laser.png")
laserx = 0
lasery = 480
laserx_forandring = 0
lasery_forandring = 10
lasertid = "ready"

#Fienden
fiendeImg = []
fiendex = []
fiendey = []
fiendex_forandring =[]
fiendey_forandring = []
ROMVESEN = pygame.transform.scale(ROMVESEN, (60,60))
fiende_nummer = 6
fiende_fart = 1

for i in range(fiende_nummer):
    fiendeImg.append(ROMVESEN)
    fiendex.append(random.randint(0, bredde-40))
    fiendey.append(random.randint(50,150))
    fiendex_forandring.append(fiende_fart)
    fiendey_forandring.append(40)



 #Score og level
score_value = 0


tekstx = 10
teksty = 10
leveler = 6



def fiende(x,y,i):
    vindu.blit(fiendeImg[i], (x,y))

def spiller(x,y):
    vindu.blit(SPILLER, (x,y))


    
    
    
    
def skyt_laser(x,y):
    global lasertid
    lasertid = "fire"
    vindu.blit(SPILLERLASER, (x,y+10))
    
def hviskollisjon(fiendex,fiendey,laserx,lasery):
    avstand = math.sqrt(math.pow(fiendex-(laserx+30), 2) + (math.pow(fiendey-(lasery+40),2)))
    if avstand < 27:
        return True
    else:
        return False

#Game over
def skriv(t,størrelse,x,y,farge):   #Definerer funksjon
    fontObj = pygame.font.Font(None, størrelse)  #Lager et fontobjekt
    tekstFlateObj = fontObj.render(t, True, farge)  
    tekstRectObj = tekstFlateObj.get_rect()
    tekstRectObj.left = x
    tekstRectObj.top = y
    vindu.blit(tekstFlateObj, tekstRectObj)

def startskjerm():
    intro = True
    
    while intro:
        for e in pygame.event.get():
            print(e)
            if e.type == pygame.QUIT:
                pygame.quit()
            
        vindu.blit(start_bg, (0,0))
        pygame.display.update()

#Spille loop

kjører = True
while kjører:
    
    
    #Settter bakgrunnbilde
    vindu.blit(bg, (0,0))
    #Knapper som trykkes
    for e in pygame.event.get():
        
        if e.type == pygame.QUIT:
            pygame.quit()
        
        if e.type == pygame.KEYDOWN:       
#Bevegelser for spiller, piltaster
            if e.key == pygame.K_LEFT:
                spillerx_forandring = -fart
            if e.key == pygame.K_RIGHT:   
               spillerx_forandring = fart
#Skyting          
            if e.key == pygame.K_SPACE:
                if lasertid == "ready":
                    laserx = spillerx   #finner posisjonen til romskipet
                    skyt_laser(laserx,lasery)
                    
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                spillerx_forandring = 0
        
#Spillerbevegelser etter piltast
    spillerx += spillerx_forandring
    if spillerx <= 0:
        spillerx = 0
    if spillerx >= bredde-100:
        spillerx = bredde-100
   
 
#Fiendebevegelse
    for i in range(fiende_nummer):
        
        if fiendey[i] > 440:   #spillet er over
            for j in range(fiende_nummer):
                fiendey[j] = 2000
                skriv("Game over",100, 200, høyde/2 , YELLOW)
                break
         
        fiendex[i] += fiendex_forandring[i]   
        if fiendex[i] <= 0:
            fiendex_forandring[i] = fiende_fart
            fiendey[i] += fiendey_forandring[i]    
        elif fiendex[i] >= bredde-60:
            fiendex_forandring[i] = -fiende_fart
            fiendey[i] += fiendey_forandring[i]
            
    #Kollisjon laser og fiende    
        if hviskollisjon(fiendex[i], fiendey[i], laserx, lasery):
            lasery = 480
            lasertid = "ready"
            score_value += 1
            fiendex[i] = random.randint(0, bredde-60)
            fiendey[i] = random.randint(50,150)
        
        fiende(fiendex[i], fiendey[i], i)
        
          
#Laser bevegelse
    if lasery <= 0:
        lasery = 480
        lasertid = "ready"
        
    if lasertid == "fire":
        skyt_laser(laserx,lasery)
        lasery -= lasery_forandring
    
    for i in range (1,leveler+1):
        if score_value == i*6:
            fiende_fart = i
            skriv("Level "+str(i)+" Farten øker!",30,10,40,WHITE)
    
    #Poeng/score
  
    skriv("Poeng: " + str(score_value),40,tekstx,teksty,WHITE)
    spiller(spillerx,spillery)   
    pygame.display.update()
    
