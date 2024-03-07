import pygame
import os
pygame.init()

WIN = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Tiger Chasing Deer!")
td_img= pygame.image.load(os.path.join('Assets', 'tiger_deer.gif'))
td = pygame.transform.scale(td_img, (400,200))

def input_t():
    t = ''
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
                    if t!= '':
                        return t
                    else:
                        pass
                if tb3.collidepoint(events.pos):
                    if t!= '':
                        return (float(t)*60*60)
                    else:
                        pass
            if events.type == pygame.KEYDOWN:
                if active:
                    if events.key == pygame.K_BACKSPACE:
                        t = t[:-1]
                    elif events.key == pygame.K_RETURN:
                        if t == "":
                            pass
                        else:
                            return t
                    else:
                        temp = events.unicode
                        if (temp >= "0" and temp<="9" or temp == "."):
                            t += events.unicode
                        else:
                            pass
                    
            
        WIN.fill('white')
        if active:
            color = pygame.Color('black')
        else:
            color = pygame.Color((100,100,100))
        WIN.blit(td, (190,30))
        pygame.draw.rect(WIN,color, tb1,4)

        pygame.draw.rect(WIN,color2, tb2,4)
        pygame.draw.rect(WIN,color2, tb3,4)
        m_s = font3.render("second",True,'black')
        kmh = font3.render("hour",True,'black')
        tb2.w = max(100, m_s.get_width()+10)
        WIN.blit(m_s, (tb2.x+8,tb2.y+10))
        tb3.w = max(100, kmh.get_width()+10)
        WIN.blit(kmh, (tb3.x+22,tb3.y+10))


        surf = font2.render(t,True,'black')
        vd_title = font1.render("Enter time of chase (t):",True,"black")
        WIN.blit(vd_title, (tb1.x-70, tb1.y -35))
        WIN.blit(surf, (tb1.x+5, tb1.y+5))
        tb1.w = max(100, surf.get_width()+10)
        pygame.display.update()
        clock.tick(50)
