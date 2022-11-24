import pygame

# 체스
# 8 * 8 = 64 칸 격자
# https://en.wikipedia.org/wiki/Chess

# reset
pygame.init()

# color
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
LIGHTGRAY = (211, 211, 211)
LIGHTBROWN = (196, 164, 132)
PALEGREEN = (152, 251, 152)

# screen setting
# 100 * 8 = 400
screenX = 800
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

# rect
rect_width = 100
rect_height = 100

# tiles
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
AN = [A, B, C, D, E, F, G, H] # Algebraic notation
for lists in AN:
    for tilenum in range(8):
        lists.append(8 - tilenum)
        
# position & rotation notation
for height in range(8):
        for width in range(8):
            AN[height].append([height * 100, width * 100])

select_pos = []

# pieces
# black
rock_img = pygame.image.load("black/BRock.png")
rock_object = rock_img.get_rect()

knight_img = pygame.image.load("black/BKnight.png")
knight_object = knight_img.get_rect()

bishop_img = pygame.image.load("black/BBishop.png")
bishop_object = bishop_img.get_rect()

queen_img = pygame.image.load("black/BQueen.png")
queen_object = queen_img.get_rect()

king_img = pygame.image.load("black/BKing.png")
king_object = king_img.get_rect()

pawn_img = pygame.image.load("black/BPawn.png")
pawn_object = pawn_img.get_rect()

team_black = [
    rock_object,
    knight_object,
    bishop_object,
    queen_object,
    king_object,
    pawn_object
]


run = True
fps = pygame.time.Clock()
while run:
    fps.tick(30)
    
    screen.fill(LIGHTBROWN)
    for height in range(8):
        for width in range(8):
            if (height % 2 == 0 and width % 2 == 0) or (height % 2 == 1 and width % 2 == 1):
                pygame.draw.rect(screen, LIGHTGRAY, (height * 100, width * 100 , rect_width, rect_height))
    for blit in range(len(select_pos)):
        pygame.draw.rect(screen, PALEGREEN, (select_pos[blit][0], select_pos[blit][1], rect_width, rect_height))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                select_pos = []
                posX = (event.pos[0] // 100) * 100
                posY = (event.pos[1] // 100) * 100
                select_pos.append([posX, posY])
                
            elif event.button == 3:
                select_pos.clear()
                
    
    
    pygame.display.update()
pygame.quit()