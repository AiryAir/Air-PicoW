// Include the Servo library 
#include <Servo.h> 
// Declare the Servo pin 
int servoPin = 3; 

// Create a servo object 
Servo Servo1; 
void setup() { 
   // We need to attach the servo to the used pin number 
   Servo1.attach(servoPin); 
}
void loop(){ 
   // Make servo go to 0 degrees 

      Servo1.write(180);
     delay(100);


}
