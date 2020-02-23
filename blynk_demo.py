import BlynkLib
import network
import machine

WIFI_SSID = 'YourWiFiNetwork'
WIFI_PASS = 'YourWiFiPassword'

BLYNK_AUTH = 'YourAuthToken'

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

def runLoop():
    while True:
        blynk.run()
        machine.idle()

# Run blynk in the main thread:
runLoop()
