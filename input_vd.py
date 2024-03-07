import pygame
import os
pygame.init()

WIN = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Tiger Chasing Deer!")
deer_img= pygame.image.load(os.path.join('Assets', 'dr2.png'))
deer = pygame.transform.scale(deer_img, (300,300))

def input_vd():
    vd = ''
    font1 = pygame.font.SysFont('aerial',35)
    font2 = pygame.font.SysFont('aerial',50)
    
    tb1 = pygame.Rect(330,250,50,40)
    font3 = pygame.font.SysFont('aerial',35)
    tb2 = pygame.Rect(330,300,50,40)
    tb3 = pygame.Rect(330,350,50,40)
    active = False
    color = pygame.Color((100,100,100))
    color2 = pygame.Color('black')
    clock = pygame.time.Clock()


    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if tb1.collidepoint(events.pos):
                    active = True
                else:
                    active = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                if tb2.collidepoint(events.pos):
                    if vd!= '':
                        return vd
                    else:
                        pass
                if tb3.collidepoint(events.pos):
                    if vd!= '':
                        return (float(vd)*0.277777778)
                    else:
                        pass
            if events.type == pygame.KEYDOWN:
                if active:
                    if events.key == pygame.K_BACKSPACE:
                        vd = vd[:-1]
                    elif events.key == pygame.K_RETURN:
                        if vd == "":
                            pass
                        else:
                            return vd
                    else:
                        temp = events.unicode
                        if (temp >= "0" and temp<="9" or temp == "."):
                            vd += events.unicode
                        else:
                            pass
     
        WIN.fill('white')
        if active:
            color = pygame.Color('black')
        else:
            color = pygame.Color((100,100,100))
        pygame.draw.rect(WIN,color, tb1,4)

        pygame.draw.rect(WIN,color2, tb2,4)
        pygame.draw.rect(WIN,color2, tb3,4)
        m_s = font3.render("m/s",True,'black')
        kmh = font3.render("km/h",True,'black')
        tb2.w = max(100, m_s.get_width()+10)
        WIN.blit(m_s, (tb2.x+27,tb2.y+10))
        tb3.w = max(100, kmh.get_width()+10)
        WIN.blit(kmh, (tb3.x+21,tb3.y+10))

        WIN.blit(deer, (200,-40))
        surf = font2.render(vd,True,'black')
        vd_title = font1.render("Enter velocity of Deer (v):",True,'black')
        WIN.blit(vd_title, (tb1.x-110, tb1.y -35))
        WIN.blit(surf, (tb1.x+5, tb1.y+5))
        tb1.w = max(100, surf.get_width()+10)
        pygame.display.update()
        clock.tick(50)
