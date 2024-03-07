import pygame
import os
pygame.init()


WIN = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Tiger Chasing Deer!")
tiger_deer_img = pygame.image.load(os.path.join('Assets', 'tiger_deer.gif'))
tiger_deer = pygame.transform.scale(tiger_deer_img, (400,200))
grass_img = pygame.image.load(os.path.join('Assets', 'grassline.png'))
grass = pygame.transform.scale(grass_img, (1000,100))

def home_pg():
    vd = ''
    font1 = pygame.font.SysFont('aerial',55)
    font2 = pygame.font.SysFont('aerial',35)
    tb1 = pygame.Rect(330,300,50,40)
    tb2 = pygame.Rect(330,350,50,40)
    color = pygame.Color('black')
    clock = pygame.time.Clock()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if tb1.collidepoint(events.pos):
                    #print("Check!")
                    return True
                if tb2.collidepoint(events.pos):
                    #print("Exit!")
                    return False
                    
            
        WIN.fill('white')
        pygame.draw.rect(WIN, color, tb1, 4)
        pygame.draw.rect(WIN, color, tb2, 4)
        WIN.blit(tiger_deer, (150, 100))
        WIN.blit(grass, (-40, 190))
        surf = font2.render(vd,True,'black')
        vd_title = font1.render("Can the Tiger catch the Deer?",True,'black')
        WIN.blit(vd_title, (95,40))
        WIN.blit(surf, (tb1.x+5, tb1.y+5))
        check = font2.render("Check!",True,'black')
        exit = font2.render("Exit!",True,'black')
        tb1.w = max(100, surf.get_width()+10)
        WIN.blit(check, (tb1.x+10,tb1.y+10))
        tb2.w = max(100, surf.get_width()+10)
        WIN.blit(exit, (tb2.x+20,tb2.y+10))
        pygame.display.update()
        clock.tick(50)

