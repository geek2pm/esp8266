import BlynkLib
import network
import machine
from machine import Pin
from machine import PWM
from time import sleep

class LED_rgb:
    def __init__(self):
        self.led_r = PWM(Pin(4), freq=500)
        self.led_g = PWM(Pin(0), freq=500)
        self.led_b = PWM(Pin(2), freq=500)
        self.r=256
        self.g=256
        self.b=256

    def set_r(self,num):
        self.r=int(num)

    def set_g(self,num):
        self.g=int(num)

    def set_b(self,num):
        self.b=int(num)

    def run(self):
        self.led_r.duty(self.r)
        self.led_g.duty(self.g)
        self.led_b.duty(self.b)

led = LED_rgb()

WIFI_SSID = ''
WIFI_PASS = ''

BLYNK_AUTH = ''

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH,server="192.168.1.7",port=8080)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

@blynk.on("V1")
def v1_write_handler(value):
    led.set_r(value[0])

@blynk.on("V2")
def v2_write_handler(value):
    led.set_g(value[0])

@blynk.on("V3")
def v3_write_handler(value):
    led.set_b(value[0])

while True:
    blynk.run()
    led.run()
    machine.idle()
