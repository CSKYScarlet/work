import pygame # pygame 불러오기
import numpy as np # 과학(공학)계산식 불러오기
from math import * # (부가적인)수학계산식 불러오기

# 색을 지정할 변수 선언
WHITE = (255, 255, 255) # 배경 설정
RED = (255, 0, 0) # 도트 설정
BLUE = (0, 0, 255)
BLACK = (0, 0, 0,) # 라인 설정

WIDTH, HEIGHT = 800, 600 # 창 크기 설정
pygame.display.set_caption("3D projection in pygame ! ") #  창 이름 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # 창 기준 0, 0 좌표를 설정

scale = 100 # 도트의 크기 설정

circle_pos = [WIDTH / 2, HEIGHT / 2] # x, y (도트의 위치 설정)

angle = 0 # 각도를 저장할 변수 선언

points = [] # 리스트를 저장할 변수 선언

# 정팔포체 꼭짓점 설정
# 도트들의 상대위치 설정
# http://matrixmultiplication.xyz/
# all the cube vertices
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


# 3차원 구조 설정
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]

projected_points2 = [
    [n, n] for n in range(len(points))
]

# 도트와 도트를 잇는 선을 그리는 함수를 선언
def connect_potints(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
    
def connect_potints2(i, j, points1, points2):
    pygame.draw.line(screen, BLACK, (points1[i][0], points1[i][1]), (points2[j - 1][0], points2[j - 1][1]))

clock = pygame.time.Clock() # 프레임 변수 설정
while True: # 이벤트 반복문 설정
    
    clock.tick(60) #프레임 수 설정
    
    for event in pygame.event.get(): # 이벤트 받기
        if event.type == pygame.QUIT: # 창 X버튼 누를 시 프로그램 종료
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: # ESC버튼 누를 시 프로그램 종료
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
    # 공학적 계산
    # wikipedia / Basic rotations
    # update stuff
    
    # 지정된 좌표(방향으로) n만큼 움직임을 설정
    # z 방향 움직임 설정
    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])
    
    # y 방향 움직임 설정
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])
    
    # x 방향 움직임 설정
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])
    
    angle += 0.01 # 움직임의 속도 설정
    
    # 화면 배경을 출력
    screen.fill(WHITE) # 지정한 색깔로 채우기
    
    # drawining stuff
    # 변수들을 불러와서 실제로 화면 상에 그려서 출력
    i = 0 # 리스트를 요약하여 저장 할 허수 변수 선언
    i2 = 0
    
    # 도트의 수 만큼 반복
    for point in points: # out cubic
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        
        projected2d = np.dot(projection_matrix, rotated2d)
        
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        
        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1 # 매 주기마다 그릴 도트의 상대위치 증가
        
    for point in points: # in cubic
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        
        projected2d = np.dot(projection_matrix, rotated2d)
        
        x = int(projected2d[0][0] * (scale / 2)) + circle_pos[0]
        y = int(projected2d[1][0] * (scale / 2)) + circle_pos[1]
        
        projected_points2[i2] = [x, y]
        pygame.draw.circle(screen, BLUE, (x, y), 5)
        i2 += 1
    
    # connect_potints(0, 1, projected_points)
    # connect_potints(1, 2, projected_points)
    # connect_potints(2, 3, projected_points)
    # connect_potints(3, 0, projected_points)
    
    # connect_potints(4, 5, projected_points)
    # connect_potints(5, 6, projected_points)
    # connect_potints(6, 7, projected_points)
    # connect_potints(7, 4, projected_points)
    
    # connect_potints(0, 4, projected_points)
    # connect_potints(1, 5, projected_points)
    # connect_potints(2, 6, projected_points)
    # connect_potints(3, 7, projected_points)
    
    # 도트와 도트들을 잇는 선을 그리기
    for p in range(4): # 위의 명령문을 요약, 반복
        # out cubic
        connect_potints(p, (p + 1) % 4, projected_points)
        connect_potints(p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_potints(p, p + 4, projected_points)

        # in cubic
        connect_potints(p, (p + 1) % 4, projected_points2)
        connect_potints(p + 4, ((p + 1) % 4) + 4, projected_points2)
        connect_potints(p, p + 4, projected_points2)
        
        # connect out-in cubic
        connect_potints2(p, (p + 1), projected_points, projected_points2)
        connect_potints2(p + 4, ((p + 1)) + 4, projected_points, projected_points2)
    
    
    # 주기적으로 화면 갱신(업데이트)
    pygame.display.update()