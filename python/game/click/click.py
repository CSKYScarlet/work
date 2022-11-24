from doctest import COMPARISON_FLAGS
import pygame

pygame.init()

screenX = 1080
screenY = 720
screen  = pygame.display.set_mode((screenX, screenY))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#------------------------------------------------------------------------------

# Order Of Magnitude(round 2)
def OOM(num_args):
    K = 10 ** 3 # thousand
    M = 10 ** 6 # million
    B = 10 ** 9 # billion
    T = 10 ** 12 # trillion
    QUARD = 10 ** 15 # quadrillion
    QUINT = 10 ** 18 # quintillion
    SEX = 10 ** 21 # sextillion
    SEP = 10 ** 24 # septillion
    if num_args >= K:
        RE_num = str(round(num_args / K, 2)) + "K"
        if num_args >= M:
            RE_num = str(round(num_args / M, 2)) + "M"
            if num_args >= B:
                RE_num = str(round(num_args / B, 2)) + "B"
                if num_args >= T:
                    RE_num = str(round(num_args / T, 2)) + "T"
                    if num_args >= QUARD:
                        RE_num = str(round(num_args / QUARD, 2)) + "QUARD"
                        if num_args >= QUINT:
                            RE_num = str(round(num_args / QUINT, 2)) + "QUINT"
                            if num_args >= SEX:
                                RE_num = str(round(num_args / SEX, 2)) + "SEX"
                                if num_args >= SEP:
                                    RE_num = str(round(num_args / SEP, 2)) + "SEP"
    else:
        RE_num = str(round(num_args, 2))
        
    return RE_num
    
# float point numbers
def float_point(FPnum):
    Enum = 0
    while FPnum >= 10:
        FPnum = FPnum / 10
        Enum += 1
        
    return str(round(FPnum, 2)) + "e" + str(Enum)

def num_methods(num_values):
    if num_values < 10 ** 25:
        return OOM(num_values)
    elif num_values >= 1.00e24:
        return float_point(num_values)
    
main_img      = pygame.image.load("./main.png")
main_img      = pygame.transform.scale(main_img, (300, 300))
main_object   = main_img.get_rect()
main_object.x = (screenX / 2 - main_object.width  / 2)
main_object.y = (screenY / 2 - main_object.height / 2)

NPC_img = pygame.image.load("./NPC_up.png")
NPC_img = pygame.transform.scale(NPC_img, (100, 100))
NPC_object = NPC_img.get_rect()
NPC_object.x = main_object.x
NPC_object.y = screenY - NPC_object.height - 75

CPT_img = pygame.image.load("./CPT_up.png")
CPT_img = pygame.transform.scale(CPT_img, (100, 100))
CPT_object = CPT_img.get_rect()
CPT_object.x = main_object.x + main_object.width - CPT_object.width
CPT_object.y = screenY - CPT_object.height - 75

POP_list = []

#------------------------------------------------------------------------------

score_num  = 1.e9
NPC        = 1 # number per click
NPCup_need = 10
CPT        = 0 # click per tick
CPTup_need = 1000

POP_rate   = 0
fps        = pygame.time.Clock()
run        = True

while run:
    fps.tick(30)
    
    # text settings
    POP_font   = pygame.font.SysFont("arial", 20, False, True)
    POP_text   = POP_font.render(("+" + num_methods(NPC)), True, BLACK)
    POP_object = POP_text.get_rect()
    
    score_font     = pygame.font.SysFont("arial", 48, True, False)
    score_text     = score_font.render(num_methods(score_num), True, BLACK)
    score_object   = score_text.get_rect()
    score_object.x = (screenX / 2) - (score_object.width / 2)
    score_object.y = 100
    
    # upgrade text
    NPCup_font     = pygame.font.SysFont("arial", 20, True, False)
    NPCup_text     = NPCup_font.render("NPC.UP", True, BLACK)
    NPCup_object   = NPCup_text.get_rect()
    NPCup_object.x = (NPC_object.x + (NPC_object.width / 2)) - (NPCup_object.width / 2)
    NPCup_object.y = screenY - 160
    
    NPCneed_font     = pygame.font.SysFont("arial", 20, False, False)
    NPCneed_text     = NPCneed_font.render("need/" + num_methods(NPCup_need), True, BLACK)
    NPCneed_object   = NPCneed_text.get_rect()
    NPCneed_object.x = (NPC_object.x + (NPC_object.width / 2)) - (NPCneed_object.width / 2)
    NPCneed_object.y = screenY - 120
    
    CPTup_font     = pygame.font.SysFont("arial", 20, True, False)
    CPTup_text     = CPTup_font.render("CPT.UP", True, BLACK)
    CPTup_object   = CPTup_text.get_rect()
    CPTup_object.x = (CPT_object.x + (CPT_object.width / 2)) - (CPTup_object.width / 2)
    CPTup_object.y = screenY - 160
    
    CPTneed_font     = pygame.font.SysFont("arial", 20, False, False)
    CPTneed_text     = CPTneed_font.render("need/" + num_methods(CPTup_need), True, BLACK)
    CPTneed_object   = CPTneed_text.get_rect()
    CPTneed_object.x = (CPT_object.x + (CPT_object.width / 2)) - (CPTneed_object.width / 2)
    CPTneed_object.y = screenY - 120
    
    # info text
    NPC_T_font     = pygame.font.SysFont("arial", 20, True, True)
    NPC_T_text     = NPC_T_font.render("Numper Per Click " + num_methods(NPC), True, BLACK)
    NPC_T_object   = NPC_T_text.get_rect()
    NPC_T_object.x = screenX - 200 - (NPC_T_object.width / 2)
    NPC_T_object.y = 200
    
    CPT_T_font     = pygame.font.SysFont("arial", 20, True, True)
    CPT_T_text     = CPT_T_font.render("Click Per tick " + num_methods(CPT), True, BLACK)
    CPT_T_object   = CPT_T_text.get_rect()
    CPT_T_object.x = screenX - 200 - (CPT_T_object.width / 2)
    CPT_T_object.y = NPC_T_object.y + CPT_T_object.height + 5
    
    # blit & draw
    pygame.draw.rect(screen, WHITE, (50, 50, screenX - 100, screenY - 100))
    screen.blit(main_img, main_object)
    screen.blit(NPC_img, NPC_object)
    screen.blit(CPT_img, CPT_object)
    for blit in POP_list:
        screen.blit(blit[0], blit[1])
    screen.blit(score_text, score_object)
    screen.blit(NPCup_text, NPCup_object)
    screen.blit(NPCneed_text, NPCneed_object)
    screen.blit(CPTup_text, CPTup_object)
    screen.blit(CPTneed_text, CPTneed_object)
    screen.blit(NPC_T_text, NPC_T_object)
    screen.blit(CPT_T_text, CPT_T_object)
    
    # events
    for event in pygame.event.get(): # quit event
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN: # keyboard events
            if event.key == pygame.K_ESCAPE: # quit
                run = False

        elif event.type == pygame.MOUSEBUTTONDOWN: # mousebutton events
            if main_object.collidepoint(event.pos): # when collide point
                POP_object.x , POP_object.y = event.pos
                POP_object.x = POP_object.x - (POP_object.width / 2)
                POP_object.y = POP_object.y - (POP_object.height / 2)
                POP_list.append([POP_text, POP_object])
                
                score_num += NPC
                
            elif NPC_object.collidepoint(event.pos): # when collide point
                if score_num >= NPCup_need:
                    score_num -= NPCup_need
                    NPC *= 1.3
                    NPCup_need *= 1.4
                    
            elif CPT_object.collidepoint(event.pos): # when collide point
                if CPT == 0:
                    score_num -= CPTup_need
                    CPT += 1
                    CPTup_need *= 1.4
                elif score_num >= CPTup_need:
                    score_num -= CPTup_need
                    CPT *= 1.4
                    CPTup_need *= 1.5
                    
    score_num += CPT
                
    # del text
    if len(POP_list) > 0:
        POP_rate += 1
        if POP_rate == 5:
            del POP_list[0]
            POP_rate = 0

    print(fps.get_fps())
    # display update
    pygame.display.update()

# gamequit
pygame.display.quit()