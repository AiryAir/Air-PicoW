# vcc - pin 36
# gnd - pin 38
# in - pin 34 (gp28)

import machine
import utime

pico_led = machine.Pin("LED", machine.Pin.OUT)
pico_led.on()

analog_value = machine.ADC(28)
 
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.2)