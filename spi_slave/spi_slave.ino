#include <SPI.h>

#define SS_PIN 10  // Slave select pin

void setup() {
  // Set SS pin as an input pin
  pinMode(SS_PIN, INPUT);
  // Initialize SPI as Slave
  SPI.begin();
  // Attach a function to trigger when a message is received
  SPI.attachInterrupt();
  // Start serial communication
  Serial.begin(9600);
}

// SPI interrupt service routine
ISR(SPI_STC_vect) {
  // Read received data
  char receivedData = SPI.transfer(0);
  // Print received data
  Serial.println(receivedData);
}

void loop() {
  // Do nothing, wait for SPI interrupt
}
