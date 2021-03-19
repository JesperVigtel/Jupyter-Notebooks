import pygame
from pygame.locals import *
import random
from pylab import math
from pylab import loadtxt

#Starter programmer
pygame.init()

#Skjermen
bredde = 800
høyde = 600
vindu = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Space invaders")

#Spiller og fiende variabler

#Spiller
fart = 8
lasery_forandring = 20

leveler = 8
#Fiende
fiende_nummer = 6
fiende_fart = 1



#Farger
YELLOW = (255, 255,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Bakgrunn
bg = pygame.image.load("./assets/sort-bakgrunn.png")
bg = pygame.transform.scale(bg, (bredde, høyde))
start_bg = pygame.image.load("./assets/startbilde.png")
start_bg = pygame.transform.scale(start_bg, (bredde,høyde))



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


#Laseren   ready = du kan ikke se laseren,  fire = du kan se laseren
SPILLERLASER = pygame.image.load("./assets/gul-laser.png")
laserx = 0
lasery = 480
laserx_forandring = 0
lasertid = "ready"

#Fienden
fiendeImg = []
fiendex = []
fiendey = []
fiendex_forandring =[]
fiendey_forandring = []
ROMVESEN = pygame.transform.scale(ROMVESEN, (60,60))


for i in range(fiende_nummer):
    fiendeImg.append(ROMVESEN)
    fiendex.append(random.randint(0, bredde-40))
    fiendey.append(random.randint(50,150))
    fiendex_forandring.append(fiende_fart)
    fiendey_forandring.append(40)



 #Score og level
score_value = 0
level_nå = 0

high_score = str(int(loadtxt("./assets/poeng.txt")))






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
    


    
intro = True
kjører = False
    
while intro:
    vindu.blit(start_bg, (0,0))
    skriv("v2",50,600,200,YELLOW)
    skriv("Av Jesper Vigtel Hølland", 30,550,10,WHITE)
    skriv("High score: "+high_score, 50,10,10, WHITE)
    skriv("Obs: Du bruker piltaster til bevegelse og mellomromsttast til skyting", 30,10,570,YELLOW)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            kjører = True
            intro = False
            
    pygame.display.update()



#Spille loop


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
            level_nå = i
            
           
        
    
    #Poeng/score
    skriv("Level: "+ str(level_nå),40,650,10,WHITE)
    skriv("Poeng: " + str(score_value),40,10,10,WHITE)
    skriv("High score: "+ high_score, 30,300,10, WHITE)
    spiller(spillerx,spillery)   
    pygame.display.update()
    
