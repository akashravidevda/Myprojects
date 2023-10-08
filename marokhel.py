import pygame, sys
from pygame.locals import *
import random
import math 
  
pygame.init()  
#l = pygame.image.load("back.png")
DISPLAYSURF = pygame.display.set_mode((600,800))  
exx = -0.3
pygame.display.set_caption('Hello World')
#DISPLAYSURF.fill((0,0,0))
pygame.display.update()
#a = DISPLAYSURF.image.load("c.png")
a = pygame.image.load("b.png") 
b = pygame.image.load("ben.png")
varr = pygame.image.load("fire.png")
x = 250
y = 500 
xt = 0
yt = 0
enx = 0
eny = 40
eyy = 0
atx = x + 16
aty = y - 35
score = 0 
fire = False
#def collider(atx,aty,enx,eny):
def collider(atx,aty,enx,eny):
   distance = math.sqrt((math.pow(enx-atx,2))+((math.pow(eny-aty,2))))
   #distance1 = math.sqrt(15 +(math.pow(enx-atx,2))+(39+(math.pow(eny-aty,2))))
   #distance3 = math.sqrt(30+(math.pow(enx-atx,2))+(39+(math.pow(eny-aty,2))))
#    pic1 = varr.get_rect()
#    pic2 = b.get_rect()
#    k =  pic1.collidepoint(pic2.x,pic2.y)
   #if distance < 35 or distance1 < 35 or distance3 < 35:
   if distance < 45: 
         return True
#    return k



def pando(i):
     if i == "w":
        y -= 10
        tyle(x,y)
        return x,y
     elif i == "a":    
       x -= 10
       tyle(x,y)
       return x,y
     elif i == "s":
       x -= 10
       tyle(x,y)
       return x,y
     elif i == "d" : 
       x += 10
       tyle(x,y)
       return x,y
#enx = random.randint(0,470)
#eny = random.randint(0,600)
def tyle(x,y) :
   DISPLAYSURF.blit(a,(x,y))
def enemy(x,y) :
   DISPLAYSURF.blit(b,(x,y))
#DISPLAYSURF.fill((10,10,10))
def attack(x,y,m = False):
   if m:
       DISPLAYSURF.blit(varr,(x,y)) 
   else : 
      return 0   
#def collider(atx,aty,enx,eny):
#      distance = math.sqrt((math.pow(atx- enx,2))+(math.pow(aty-eny,2))
#          #return True
           
# screen size :x = 500 ,y = 850 
print(a.get_size())
while True: 
    #DISPLAYSURF.blit(l,(0,0))
    m = ""
    k  =   ""
    DISPLAYSURF.fill((225,210,230))
    pygame.draw.rect(DISPLAYSURF,(0,200,255),(0,0,580,490)) 
    pygame.draw.rect(DISPLAYSURF,(0,200,255),(0,500,580,490)) 
    pygame.draw.rect(DISPLAYSURF,(210,100,0),(0,0,15,990))
    pygame.draw.rect(DISPLAYSURF,(210,100,0),(527,0,15,990))
    pygame.draw.rect(DISPLAYSURF,(115,10,120),(12,490,515,5))  
    #x,y = pygame.mouse.get_pos()
    for i in pygame.event.get():
        #enx = random.randint(0,470)
        #eny = random.randint(0,250)
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        if i.type == KEYDOWN : 
            if i.key == pygame.K_a: 
                xt = -7 
            elif i.key == pygame.K_d:
                xt = 7
            elif i.key == pygame.K_w:   
                yt = -7  
            elif i.key == pygame.K_s:
                yt = 7
            elif i.key == pygame.K_o :
                attack(atx,aty,fire)
            elif i.key == pygame.K_SPACE:
                    fire = True 
                    atx = x + 16
                    #aty = y - 10
            elif i.key == pygame.K_p:
                aty = 450
                fire = False 
                
        if i.type == KEYUP :
                xt = 0
                yt = 0
        #x += 1
    
    x += xt
    y += yt
    if x > 500 :
       x = 500
    elif x<0:
       x = 0
    if y > 800: 
       y = 800
    elif  y<0:
       y = 0
    enx += exx
    if enx <= 0 : 
       # this is for adding bg img
       # exx = 10
       exx = 0.9
       eny += 40
    if enx >= 480:
         # this is for bg img
         # exx = 10i
         exx = -0.9
         eny += 40
#       if  enx >= 450 :      
#           eny += 40 
#    elif enx >= 450:
#         enx -= 0.9
#         if enx <= 0:
#            eny += 40
            
            
#    elif x<=450:
#       enx -= 0.9
#       if x <= 0:
#          eny += 40
#    if y >= 800:
#       eny = 800
#    elif  y <= 0:
#       eny = 0
    tyle(x,y) 
    if aty <= 0 :
        fire = False
        aty = 450
        
    if fire == True:
       aty -= 1.9
       
#    if aty <= 0 : 
#        aty = 450
#        fire = False    
#    elif aty >1 :
#       aty -= 0.9
    enemy(enx,eny)      
    attack(atx,aty,fire)
#    if collider(varr,b):
#    pic1 = varr.get_rect()
#    pic2 = b.get_rect()
#    
#    k = pic1.colliderect(pic2)
#    if k :
#       print(pic1,pic2)
#       print("halo")
#    else : 
#       print("dam",end =" ")
    if collider(atx,aty,enx,eny):
        fire = False
        score += 1
        print(score)
        aty = 450
        enx = random.randint(0,490)
        eny = random.randint(0,250)
    pygame.display.update()
             

      #for event in pygame.event.get():

#pygame.display.fill((225,0,0))

#while True: # main game loop

#  for event in pygame.event.get():

#    if event.type == QUIT:

#       pygame.quit()

#       sys.exit()

#      pygame.display.update()