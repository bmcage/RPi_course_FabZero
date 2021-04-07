# code that should run on RPi
DEBUG = True

def RPi_code ():
    
    from gpiozero import LED, Button
    from time import sleep

    led = LED(17)

    def testpins():
        if DEBUG:
            print ('value LED', led.value)
        
    def button_pressed():
        print("button pressed!")
        led2.toggle()
    
    led2 = LED(22)
    button = Button(11)
    button.when_pressed = button_pressed
    
    while True:
        led.on()
        testpins()
        sleep(1)
        led.off()
        testpins()
        sleep(1)

if __name__ == "__main__":
    # code is being executed on real RPi
    RPi_code()
    
