import Adafruit_DHT

class DHT11:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11

    def retTempHum(self):
        hum, temp = Adafruit_DHT.read(self.sensor, self.pin)
        while hum is None and temp is None:
            hum, temp = Adafruit_DHT.read(self.sensor, self.pin)
        return temp, hum
        

if __name__ == '__main__':
    s = DHT11(4)
    t, h = s.retTempHum()
    print(t,h)