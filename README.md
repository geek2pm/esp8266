# esp8266

install
```
sudo pip3 install esptool
sudo pip3 install adafruit-ampy
```

flash
```
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20191220-v1.12.bin
```

## blynk-library-python

linux & raspberry pi
```
pip3 install blynk-library-python
```

esp8266
```
sudo ampy -p /dev/ttyUSB0 mkdir /lib
sudo ampy -p /dev/ttyUSB0 put BlynkLib.py /lib/BlynkLib.py
```


> BlynkLib.py download from https://raw.githubusercontent.com/vshymanskyy/blynk-library-python/master/BlynkLib.py

## blynk-server (raspberry pi)

```
sudo apt install openjdk-8-jdk openjdk-8-jre
```
```
wget "https://github.com/blynkkk/blynk-server/releases/download/v0.41.12/server-0.41.12-java8.jar"
java -jar server-0.41.12-java8.jar -dataFolder /home/pi/Blynk
```

```
crontab -e
```

add

```
@reboot java -jar /home/pi/server-0.41.12-java8.jar -dataFolder /home/pi/Blynk &
```
