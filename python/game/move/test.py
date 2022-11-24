import pygame

# 창 크기
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
# 창 이름
pygame.display.set_caption("mygame")

# 네모
yellow = "yellow_rect.png"
blue = "blue_rect.png"

#------------------------------------------------------------------------------
def change():
    global box_img
    global rect_num
    
    if rect_num == 0:
        box_img = pygame.image.load(blue)
        rect_num = 1
        
    elif rect_num == 1:
        box_img = pygame.image.load(yellow)
        rect_num = 0

def setting():
    global box_img, rect_object, rects, rect_num, xpos, ypos
    
    box_img = pygame.image.load(yellow)
    rect_object = box_img.get_rect()
    rect_object.x = 225
    rect_object.y = 225

    rects = [[box_img, rect_object]]

    rect_num = 0

    xpos = 0
    ypos = 0
#------------------------------------------------------------------------------

box_img = pygame.image.load(yellow)
rect_object = box_img.get_rect()
rect_object.x = 225
rect_object.y = 225

rects = [[box_img, rect_object]]

rect_num = 0

xpos = 0
ypos = 0

reset_img = pygame.image.load("reset.png")
reset_object = reset_img.get_rect()

#------------------------------------------------------------------------------
fps = pygame.time.Clock()
run = True
while run:
    # fps 설정
    fps.tick(60)
    
    screen.fill((0, 0, 0))
    
    if len(rects) > 0:
        rects = [[box_img, rect_object]]
        for value in range(len(rects)):
            screen.blit(rects[value][0], rects[value][1])
    
    screen.blit(reset_img, reset_object)
    
    # 이벤트 관리
    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            
            if len(rects) > 0:
                if rect_object.collidepoint(event.pos):
                    print("true")
                    del rects[0]
            
            # 리셋
            if reset_object.collidepoint(event.pos):
                # box_img = pygame.image.load(yellow)
                # rect_object.x = 225
                # rect_object.y = 225
                # rects = [[box_img, rect_object]]
                # screen.fill((0, 0, 0))
                setting()
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ypos -= 5
                
            elif event.key == pygame.K_DOWN:
                ypos += 5
                
            elif event.key == pygame.K_LEFT:
                xpos -= 5
                
            elif event.key == pygame.K_RIGHT:
                xpos += 5
                
            if event.key == pygame.K_SPACE:
                change()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
                
    rect_object.x += xpos
    rect_object.y += ypos
    
    if rect_object.x < 0:
        rect_object.x = 0
    elif rect_object.x > screen_width - rect_object.width:
        rect_object.x = screen_width - rect_object.width
        
    if rect_object.y < 0:
        rect_object.y = 0
    elif rect_object.y > screen_height - rect_object.height:
        rect_object.y = screen_height - rect_object.height
        
    # 화면 갱신
    pygame.display.update()
#------------------------------------------------------------------------------