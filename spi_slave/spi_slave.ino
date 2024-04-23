#include <SPI.h>

#define SS_PIN 10  // Slave select pin

void setup() {
  // Initialize SPI as Slave
  SPI.begin();
  // Set SS pin as an input pin with pull-up resistor enabled
  pinMode(SS_PIN, INPUT_PULLUP);
  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if the master is selecting this slave
  if (digitalRead(SS_PIN) == LOW) {
    // Debug statement
    Serial.println("Slave selected");
    // Read data from master
    char receivedData = SPI.transfer(0);
    // Print received data
    Serial.println(receivedData);
  }
}
