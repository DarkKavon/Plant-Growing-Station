import RPi.GPIO as GPIO
from time import sleep

class WH080:
    def __init__(self,pin):
        self.pin=pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.IN)

    def enoughWater(self):
        return not GPIO.input(self.pin)


if __name__ == "__main__":
    s = WH080(4)
    print(s.enoughWater())
