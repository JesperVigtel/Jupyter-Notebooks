import pygame
from pygame.locals import *
import random
import math

#Starter programmer
pygame.init()

#Skjermen
bredde = 800
høyde = 600
vindu = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Space invaders")

#Sette FPS
FPS = 60
FramePerSec = pygame.time.Clock()


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
pygame.display.update()

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
pygame.display.update()
hastighet = 10

#Laseren
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
ROMVESEN = pygame.transform.scale(ROMVESEN, (20,20))
fiende_nummer = 6

for i in range(fiende_nummer):
    fiendeImg.append(ROMVESEN)
    fiendex.append(random.randint(0, 736))
    fiendey.append(random.randint(50,150))
    fiendex_forandring.append(4)
    fiendey_forandring.append(40)

"""

 #Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

tekstx = 10
teksty = 10
"""


def fiende(x,y,i):
    vindu.blit(fiendeImg[i], (x,y))
    
    
def skyt_laser(x,y):
    global lasertid
    lasertid = "skyt"
    vindu.blit(SPILLERLASER, (x+16,y+10))
    
def hviskollisjon(fiendex,fiendey,laserx,lasery):
    avstand = math.sqrt(math.pow(fiendex-laserx, 2) + (math.pow(fiendey-lasery,2)))
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



#Spille loop

kjører = True
while kjører:
    
#Knapper som trykkes
    for e in pygame.event.get():
        #For å avslutte 
        if e.type == pygame.QUIT:
            pygame.quit()
        #Sjekker om hvis en tast trykkes, høyre eller venstre
        if e.type == pygame.KEYDOWN:
            vindu.blit(SPILLER, (spillerx,spillery))
            pygame.display.update()
#Bevegelser for spiller
            if e.key == pygame.K_LEFT:
                vindu.blit(bg, (0,0))
                spillerx -= hastighet
                if spillerx < 0:
                    spillerx = -10
                    
            if e.key == pygame.K_RIGHT:
                vindu.blit(bg, (0,0))
                spillerx += hastighet
                if spillerx > bredde-90:
                    spillerx = bredde-90
            if e.key == pygame.K_SPACE:
                if lasertid == "ready":
                    laserx = spillerx  #finner posisjonen til romskipet
                    skyt_laser(laserx, lasery)
                
            vindu.blit(SPILLER,(spillerx,spillery))
          
        pygame.display.update()
           
#Laser bevegelse
    if lasery <= 0:
        lasery = 480
        lasertid = "ready"
        
    if lasertid == "fire":
        skyt_laser(laserx,lasery)
        lasery -= lasery_forandring
        
             
            
    pygame.display.update()
    FramePerSec.tick(FPS)
