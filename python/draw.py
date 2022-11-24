# 터틀 가져오기
from turtle import *

# 터틀의 유형(형체) 설정
shape("turtle") # 거북이형태
# 속도 설정
speed(0) # 속도
width(0) # 굵기

# 이동
for main in range(51): # 원형 반복
    for value in range(5):# 곡선
        left(10)
        forward(30)
        
    # 약간 어긋나게 반대방향으로
    right(168)
    
    for value in range(5):# 곡선
        right(10)
        forward(30)
    
    # 원형각 반대로 돌리기
    right(185)# 각도조절

done()
