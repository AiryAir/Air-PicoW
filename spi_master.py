import machine
import utime

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)  # SPI0
cs = machine.Pin(5, machine.Pin.OUT)  # chip select

def send_data(data):
    cs.value(0)  # SS
    spi.write(data)
    cs.value(1)  # slave deselect

while True:
    send_data(b'Hello from Raspberry Pi Pico!')
    utime.sleep(1)
