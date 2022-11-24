import pygame

x = 1000
y = 1000

screen = pygame.display.set_mode((x, y))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 255, 255), [mouse_pos[0] - 50, mouse_pos[1] - 50, 100, 100])
            pygame.draw.circle(screen, (0, 255, 0), (mouse_pos[0], mouse_pos[1]), 50)

    pygame.display.update()

pygame.quit()