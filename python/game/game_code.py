import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이듵
pygame.display.set_caption("game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 설정(불러오기)
background = pygame.image.load("경로")

# 캐릭터(스프라이트) 설정(불러오기)
character = pygame.image.load("경로")
character_size = character.get_rect().size # 이미지 크기 불러오기
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height # 화면 세로 크기  가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표 설정
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임 진행상황
while running:
    frame = clock.tick(30) # 초당 프레임 수 설정
    
    #print(("fps : ") + str(clock.get_fps())) # 프레임 수 확인
    
    for event in pygame.event.get(): # 이벤트가 생기는 것을 반복 감지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 하였을 때
            running = False
            
        if event.type == pygame.KEYDOWN: # 키가 눌러지고 있는 이벤트가 발생 하였을 때
            if event.key == pygame.K_LEFT: # 왼쪽 화살표 키가 눌러졌을 때
                to_x -= 5
            
            elif event.key == pygame.K_RIGHT: # 오른쪽 화살표 키가 눌러졌을 때
                to_x += 5
            
            elif event.key == pygame.K_UP: # 위쪽 화살표 키가 눌러졌을 때
                to_y -+ 5
            
            elif event.key == pygame.K_DOWN: # 아래쪽 화살표 키가 눌러졌을 때
                to_y += 5
                
        if event.type == pygame.KEYUP: # 키가 눌러지고 있는 상태가 아닐 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    character_x_pos += to_x * frame
    character_y_pos += to_y * frame

    # 가로 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
            
    # 세로 경계
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        
        
    # 배경 적용 (왼쪽 위 부터 좌표)
    screen.blit(background, (0, 0))
    # 색으로만 설정하여 배경 사용
    # screen.fill((0, 0, 0)) (rgb값)
    
    # 캐릭터 적용
    screen.blit(character,(character_x_pos, character_y_pos))
    
    # 매 프레임마다 화면 적용
    pygame.display.update() # 화면을 다시 적용(업데이트, 불러오기)
        
# 게임 종료
pygame.quit()