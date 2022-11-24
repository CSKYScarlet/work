#include <Servo.h> // 서보 패키지 불러오기

Servo myservo; // 서보 함수 지정

long ping = 0; // 초음파 송수신 변수
long sonic = 0; // 서보 제어용


void setup() // 하드세팅
{
  myservo.attach(9);

  Serial.begin(9600); // 통신(모니터링) 설정

  pinMode(5, OUTPUT);
  pinMode(6, INPUT);

}

// 전체 루틴
void loop()
{
  // 초음파 조작
  digitalWrite(5, LOW);
  delayMicroseconds(2);
  digitalWrite(5, HIGH); // 초음파 송신
  delayMicroseconds(10);
  digitalWrite(5, LOW);
  ping = pulseIn(6, HIGH); // 수신(시간)

  sonic = ping * 17 / 1000; // 초음파 cm 계산식

//-----------------------------------------
// 모니터링 시 필요
  Serial.println(ping);
  Serial.print("\nDIstance : ");
  Serial.print(sonic);
  Serial.println(" Cm");
//-----------------------------------------

  // 모터 조작
  if (sonic <= 85) {
    myservo.write(0); // 앞면
    delay(4000); // 딜레이 4초
    myservo.write(180); // 뒷면
    delay(4000); // 딜레이 4초
  }

  delay(300); // 0.3초 루틴

}
