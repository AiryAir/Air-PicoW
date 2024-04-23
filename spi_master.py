import machine
import utime

pico_led = machine.Pin("LED", machine.Pin.OUT)

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)  # SPI0
cs = machine.Pin(7, machine.Pin.OUT)

def send_data(data):
    cs.value(0)
    spi.write(data)
    cs.value(1)

while True:
    send_data(b'Hello from Raspberry Pi Pico!')
    print('data sent')
    pico_led.off()
    utime.sleep(1)
    pico_led.on()

