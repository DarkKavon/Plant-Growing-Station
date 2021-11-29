import RPi.GPIO as GPIO
from time import sleep

class LM393:
    def __init__(self,pin):
        self.pin=pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.IN)

    def enoughLight(self):
        return not GPIO.input(self.pin)


if __name__ == "__main__":
    s = LM393(4)
    print(s.enoughLight())
