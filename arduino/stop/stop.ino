#include <Servo.h>

Servo myservo;
int sensor = 12;

int pos = 0;

int value = 0;
int flag = LOW;

void setup()
{
  myservo.attach(9);

  pinMode(sensor, INPUT);
  Serial.begin(9600);

}


void loop()
{
  value = digitalRead(sensor);
  if (value == HIGH) {
    
    flag = HIGH;

  } else {
    
    flag = LOW;
    value = LOW;

  }

  if (flag == HIGH) {
    for (pos = 0; pos < 180; pos += 1)
    {
      myservo.write(pos);
      delay(10);
    }
  } else {
    for (pos = 180; pos >  0; pos -= 1)
    {
      myservo.write(pos);
      delay(10);
    }
  }

  delay(5000);

}
