import pygame
import os
pygame.init()

WIN = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Tiger Chasing Deer!")
tiger_img= pygame.image.load(os.path.join('Assets', 'tg2.png'))
tiger = pygame.transform.scale(tiger_img, (300,300))

def input_a():
    a = ''
    font1 = pygame.font.SysFont('aerial',35)
    font2 = pygame.font.SysFont('aerial',50)
    tb1 = pygame.Rect(330,250,50,40)
    active = False
    color = pygame.Color((100,100,100))
    clock = pygame.time.Clock()

    font3 = pygame.font.SysFont('aerial',35)
    tb2 = pygame.Rect(330,300,50,40)
    tb3 = pygame.Rect(330,350,50,40)
    color2 = pygame.Color('black')

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
                    if a!= '':
                        return a
                    else:
                        pass
                if tb3.collidepoint(events.pos):
                    if a!= '':
                        return (float(a)*0.00007716)
                    else:
                        pass
            if events.type == pygame.KEYDOWN:
                if active:
                    if events.key == pygame.K_BACKSPACE:
                        a = a[:-1]
                    elif events.key == pygame.K_RETURN:
                        if a == "":
                            pass
                        else:
                            return a
                    else:
                        temp = events.unicode
                        if (temp >= "0" and temp<="9" or temp == "."):
                            a += events.unicode
                        else:
                            pass
                    
            
        WIN.fill('white')
        if active:
            color = pygame.Color('black')
        else:
            color = pygame.Color((100,100,100))
        WIN.blit(tiger, (200,-40))
        pygame.draw.rect(WIN,color, tb1,4)

        pygame.draw.rect(WIN,color2, tb2,4)
        pygame.draw.rect(WIN,color2, tb3,4)
        m_s = font3.render("m/s^2",True,'black')
        kmh = font3.render("km/h^2",True,'black')
        tb2.w = max(100, m_s.get_width()+10)
        WIN.blit(m_s, (tb2.x+15,tb2.y+10))
        tb3.w = max(100, kmh.get_width()+10)
        WIN.blit(kmh, (tb3.x+8,tb3.y+10))


        surf = font2.render(a,True,'black')
        vd_title = font1.render("Enter acceleration of Tiger (a):",True,'black')
        WIN.blit(vd_title, (tb1.x-120, tb1.y -35))
        WIN.blit(surf, (tb1.x+5, tb1.y+5))
        tb1.w = max(100, surf.get_width()+10)
        pygame.display.update()
        clock.tick(50)
