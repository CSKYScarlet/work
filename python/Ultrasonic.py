import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG_PIN = 13 # Emitter Pin
ECHO_PIN = 19 # Detector Pin

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

RED = 8 # 첫번째 신호등
YELLOW = 10 # 두번재 신호등
GREEN = 12 # 세번째 신호등
GREEN2 = 18 # 세번재 시호등(보행자)

GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN2, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(RED, GPIO.HIGH) # 첫번째 신호등 지속
        
        GPIO.output(TRIG_PIN, False)
        time.sleep(0.5) # Emitter 초기화
        
        GPIO.output(TRIG_PIN, True) # Emitter 초음파 발송 시작 - 40Khz
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False) # Emitter 초음파 발송 종료
        
        # 반송파가 도착하기 전까지 대기
        while GPIO.input(ECHO_PIN) == 0:
            start = time.time() # 반송파 수신 시작 시 현재 시간 저장 후 루프 탈출
            
        # 반송파 도착이 끝날 때가지 대기
        while GPIO.input(ECHO_PIN) == 1:
            stop = time.time()
            
        # 초음파가 되돌아오는 시간차로 거리를 계산
        time_interval = stop - start
        distance = time_interval * 17165 # 17,165 음속/2
        distance = round(distance, 2) # 소수점 3째자리 반올림.
        
        print("Distance => ", distance, "cm")
        
        # 신호등
        if distance <= 10: # 10cm 이내 감지 시
            GPIO.output(RED, GPIO.LOW) # 첫번재 꺼짐
            
            GPIO.output(YELLOW, GPIO.HIGH) # 두번째 점등
            time.sleep(3)
            GPIO.output(YELLOW, GPIO.LOW)
            
            GPIO.output(GREEN, GPIO.HIGH) # 세번째 지속
            GPIO.output(GREEN2, GPIO.HIGH) # 세번째(보행자)10초간 지속
            time.sleep(10)
            for value in range(3): # 세번째(보행자) 3초간 0.5초씩 점멸
                GPIO.output(GREEN2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(GREEN2, GPIO.HIGH)
                time.sleep(0.5)
            GPIO.output(GREEN2, GPIO.LOW)
            GPIO.output(GREEN, GPIO.LOW) # 세번째 종료
        
except KeyboardInterrupt:
    GPIO.cleanup()