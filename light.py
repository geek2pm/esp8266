import BlynkLib
import network
import machine
from machine import Pin



light = Pin(2,Pin.OUT)

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
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

@blynk.on("V1")
def v1_write_handler(value):
    light.value(int(value[0]))

while True:
    blynk.run()
    machine.idle()
