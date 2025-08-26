#include <Wire.h>
#include <MCP342x.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define ADC_ADDRESS 0x68
#define WIFI_SSID "EnergyMonitorAP"
#define WIFI_PASS "12345678"

MCP342x adc(ADC_ADDRESS);
ESP8266WebServer server(80);

// Calibration and measurement values of records
long offset = 523;
long divider = 3805;
long voltage = 230;
long lastAdc = 0;

// Function to read ADC value to evaluate 
long getAdc() {
  long value = 0;
  MCP342x::Config status;
  uint8_t err = adc.convertAndRead(MCP342x::channel1, MCP342x::continous, MCP342x::resolution18, MCP342x::gain2, 2000, value, status);
  if (err) return -1;
  return value;
}

// simple Web page to get and view records
void handleRoot() {
  lastAdc = getAdc();
  float current = (float)(lastAdc - offset) / divider;
  if (current < 0) current = 0;
  float power = voltage * current;

  String html = "<html><body>";
  html += "<h1>Energy Monitor</h1>";
  html += "ADC Value: " + String(lastAdc) + "<br>";
  html += "Current: " + String(current, 3) + " A<br>";
  html += "Power: " + String(power, 2) + " W<br>";
  html += "</body></html>";

  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  // Initialize MCP3421
  Wire.requestFrom(ADC_ADDRESS, (uint8_t)1);
  if (!Wire.available()) Serial.println("MCP3421 not found!");

  // Start WiFi
  WiFi.softAP(WIFI_SSID, WIFI_PASS);
  Serial.println("Access Point started: " + String(WIFI_SSID));

  // Start web server
  server.on("/", handleRoot);
  server.begin();
}

void loop() {
  server.handleClient();
}
