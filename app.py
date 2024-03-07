#______imports_______
import pygame
from pygame_functions import *
import os
from math_solv import m_solv
from home import home_pg

#________variables______
WIDTH = 800
HEIGHT = 450
COLOR = (255,255,255)
FPS = 30
tik_img = pygame.image.load(os.path.join('Assets', 'tick.jpg'))
tik = pygame.transform.scale(tik_img, (70,70))
cross_img = pygame.image.load(os.path.join('Assets', 'cross.jpg'))
cross = pygame.transform.scale(cross_img, (70,70))
grass_img = pygame.image.load(os.path.join('Assets', 'grassline.png'))
grass = pygame.transform.scale(grass_img, (1000,40))
tiger_deer_img = pygame.image.load(os.path.join('Assets', 'tiger_deer.gif'))
tg1_img = pygame.image.load(os.path.join('Assets', 'tg1.png'))
tg1 = pygame.transform.scale(tg1_img, (120,120))
tg2_img = pygame.image.load(os.path.join('Assets', 'tg2.png'))
tg2 = pygame.transform.scale(tg2_img, (120,120))
tg3_img = pygame.image.load(os.path.join('Assets', 'tg3.png'))
tg3 = pygame.transform.scale(tg3_img, (120,120))
dr1_img = pygame.image.load(os.path.join('Assets', 'dr1.png'))
dr1 = pygame.transform.scale(dr1_img, (120,120))
dr2_img = pygame.image.load(os.path.join('Assets', 'dr2.png'))
dr2 = pygame.transform.scale(dr2_img, (120,120))
dr3_img = pygame.image.load(os.path.join('Assets', 'dr3.png'))
dr3 = pygame.transform.scale(dr3_img, (120,120))
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
tb1 = pygame.Rect(330,260,50,40)
tb2 = pygame.Rect(330,320,50,40)

font1 = pygame.font.SysFont('aerial',25)
try_again = font1.render("Try Again!",True,'black')
exi_t = font1.render("Exit!",True,'black')
color = pygame.Color('black')
pygame.display.set_caption("Tiger chasing Deer!")

font1 = pygame.font.SysFont('aerial',25)




#_______methods________
def window1(tiger, deer):

    WIN.fill(COLOR)
    WIN.blit(tg1,(tiger.x,tiger.y))
    WIN.blit(dr1,(deer.x,deer.y))
    WIN.blit(grass,(-25,205))
    pygame.display.update()
    WIN.fill(COLOR)
    WIN.blit(tg2,(tiger.x,tiger.y))
    WIN.blit(dr2,(deer.x,deer.y))
    WIN.blit(grass,(-25,205))
    pygame.display.update()
    WIN.fill(COLOR)
    WIN.blit(tg3,(tiger.x,tiger.y))
    WIN.blit(dr3,(deer.x,deer.y))
    WIN.blit(grass,(-25,205))
    pygame.display.update()
    
def window2(tiger, deer):
    WIN.fill(COLOR)
    WIN.blit(tg1,(tiger.x,tiger.y))
    WIN.blit(dr1,(deer.x,deer.y))
    WIN.blit(grass,(-25,205))
    #pygame.display.update()


#________________Main___________________
def disp1():
    tiger = pygame.Rect(0, 150, 120, 120)
    deer = pygame.Rect(120, 150, 120, 120)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tb2.collidepoint(event.pos):
                    return False
                if tb1.collidepoint(event.pos):
                    return True
            
        if tiger.x >= deer.x-10:
            window2(tiger,deer)
            pygame.draw.rect(WIN,color, tb1,4)
            pygame.draw.rect(WIN,color, tb2,4)
            Final = font1.render("The Tiger caught the Deer :(",True,'black')
            WIN.blit(Final, (280, 80))
            WIN.blit(try_again, (340,270))
            WIN.blit(exi_t, (360,330))
            tb1.w = max(100, try_again.get_width()+10)
            tb2.w = max(100, exi_t.get_width()+10)
            pygame.display.update()
            WIN.blit(tik,(350,110))
            pygame.display.update()
            
        else:
            tiger.x += 3
            deer.x += 2
            window1(tiger, deer)
    
    pygame.quit()


def disp2():
    tiger = pygame.Rect(0, 150, 120, 120)
    deer = pygame.Rect(120, 150, 120, 120)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tb2.collidepoint(event.pos):
                    return False
                if tb1.collidepoint(event.pos):
                    return True
            
        if WIN.get_width() < deer.x+10:
            window2(tiger,deer)
            pygame.draw.rect(WIN,color, tb1,4)
            pygame.draw.rect(WIN,color, tb2,4)
            Final = font1.render("The Tiger couldn't catch the Deer :)",True,'black')
            WIN.blit(Final, (240, 80))
            WIN.blit(try_again, (340,270))
            WIN.blit(exi_t, (360,330))
            tb1.w = max(100, try_again.get_width()+10)
            tb2.w = max(100, exi_t.get_width()+10)
            pygame.display.update()
            WIN.blit(cross,(350,110))
            pygame.display.update()
        else:
            tiger.x += 3
            deer.x += 3
            window1(tiger, deer)
    
    pygame.quit()



def main():
    y = home_pg()
    while y:
        x = m_solv()
        if x:
          y = disp1()
          if y == True:
             pass
          else:
             return 0
        else:
           y = disp2()
           if y == True:
             pass
           else:
             return 0

if __name__ == "__main__":
    main()