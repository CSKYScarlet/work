import pygame

pygame.init()

screenX = 1000
screenY = 1000
screen = pygame.display.set_mode((screenX, screenY))

PINK = (255, 192, 203)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ground = 50
HARF = 25
Xpos = 0
Xmove = 0
Ypos = screenY - (ground + HARF)
Ymove = 0
jump_tick = 0

fps = pygame.time.Clock()
run = True
while run:
    fps.tick(30)
    
    CirPos = Xpos + HARF, Ypos
    
    pygame.draw.rect(screen, WHITE, (0, 0, screen.get_width(), screen.get_height()))
    pygame.draw.rect(screen, BLACK, (0, screenY - ground, screen.get_width(), screen.get_height() - (screenY - ground)))
    pygame.draw.circle(screen, PINK, CirPos, HARF)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                
            if event.key == pygame.K_RIGHT:
                Xmove += 10
                
            if event.key == pygame.K_LEFT:
                Xmove -= 10
                
            if event.key == pygame.K_SPACE and Ypos == screenY - (ground + HARF):
                Ymove += 40
                jump_tick += 1
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                Xmove = 0
                
    
    Xpos += Xmove
    Ypos -= Ymove
    if jump_tick > 0:
        jump_tick += 1
        if jump_tick > 3:
            jump_tick = 0
            Ymove = -15
        
    if Ypos > screenY - (ground + HARF):
        Ypos = screenY - (ground + HARF)
    
    if Xpos < 0:
        Xpos = 0
        
    elif Xpos > screenX - (HARF * 2):
        Xpos = screenX - (HARF * 2)
    
    pygame.display.update()