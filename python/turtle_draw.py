import turtle

# 터틀 적용
t = turtle.Turtle()
# 터틀의 속도 조정
t.speed(1)
#반복해서 그리기
for value in range(5):
    t.left(-144)# 각도조절
    t.forward(100)# 전진