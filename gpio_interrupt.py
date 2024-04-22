from machine import Pin
import utime

counter = 0
pin = Pin(5, Pin.IN, Pin.PULL_UP)

def debounce(pin):
    debounce_time = 50
    current_value = pin.value()
    utime.sleep_ms(debounce_time)
    if pin.value() == current_value:
        return True
    return False

while True:
    if debounce(pin) == False:
        continue
    if pin.value() == 0:
        print("Button Pressed")
        counter += 1
        print("Count = {}".format(counter))
