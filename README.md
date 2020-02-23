# esp8266

install
```
sudo pip3 install esptool
sudo pip3 install adafruit-ampy
```

flash
```
sudo esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash
sudo esptool.py --chip esp8266 --port /dev/ttyUSB0 write_flash -z 0x1000 esp8266-20191220-v1.12.bin
```
