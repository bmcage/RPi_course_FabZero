from tkgpio import TkCircuit

# initialize the circuit inside the 

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 17},
        {"x": 100, "y": 40, "name": "LED 2", "pin": 22}
    ],
    "buttons": [
        {"x": 50, "y": 130, "name": "Press to toggle LED 2", "pin": 11},
    ]
}

circuit = TkCircuit(configuration)

import gpiozero_Tk_example01_realcode
@circuit.run
def main ():
    # now execute the code you would use on a real Raspberry Pi
    gpiozero_Tk_example01_realcode.RPi_code()
    
