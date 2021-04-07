FAKE_RPI = True
DEBUG = True

if FAKE_RPI:
    from gpiozero.pins.mock import MockFactory
from gpiozero import Device, LED
from time import sleep

if FAKE_RPI:
    # set pins to implicitly use MockFactory instead of RPiGPIOPin
    Device.pin_factory = MockFactory()

led = LED(17)

def testpins():
    if DEBUG:
        print ('value LED', led.value)
    
while True:
    led.on()
    testpins()
    sleep(1)
    led.off()
    testpins()
    sleep(1)

