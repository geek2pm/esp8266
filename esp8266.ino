#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "YourAuthToken";
char ssid[] = "YourNetworkName";
char pass[] = "YourPassword";

void setup()
{
  Serial.begin(9600);
  Blynk.begin(auth, IPAddress(192,168,1,13), 8080);
}

void loop()
{
  Blynk.run();
}
