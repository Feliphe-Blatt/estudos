#include <WiFi.h>
#include <WebServer.h>
#include "A1.h"   // Arquivo HTML-CSS-JS

// Caso queira utilizar somente a rede interna do ESP-32 comente o 'define' abaixo:
#define USE_INTRANET

// Rede interna ESP-32
#define AP_SSID "Esp-32"
#define AP_PASS "doumaooito"

// Rede local pro ESP-32 se conectar
#define LOCAL_SSID "SucoDeFruta"
#define LOCAL_PASS "qcisqcaq"

// Built-in LED
#define PIN_LED 2

bool LED = false;

int RED = 0;
int GREEN = 0;
int BLUE = 0;

char XML[2048];
char buf[32];

IPAddress Actual_IP;
// Definições da página html no ESP32
IPAddress PageIP(192, 168, 1, 171);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress ip;

WebServer server(80);
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  

  LED = false;
  REDvalue = 0;
  GREENvalue = 0;
  BLUEvalue = 0;
  
  digitalWrite(PIN_LED, LED);
  analogWrite(RED, REDvalue);
  analogWrite(GREEN, GREENvalue);
  analogWrite(BLUE, BLUEvalue);
  
  disableCore0WDT();

  Serial.println("starting server");

#ifdef USE_INTRANET
  WiFi.begin(LOCAL_SSID, LOCAL_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
    Serial.print(".");
  }
  Serial.print("IP address: "); Serial.println(WiFi.localIP());
  Actual_IP = WiFi.localIP();
#endif
#ifndef USE_INTRANET
  WiFi.softAP(AP_SSID, AP_PASS);
  delay(100);
  WiFi.softAPConfig(PageIP, gateway, subnet);
  delay(100);
  Actual_IP = WiFi.softAPIP();
  Serial.print("IP address: "); Serial.println(Actual_IP);
#endif

  printWifiStatus();

  server.on("/", EnviarSite);
  server.on("/xml", EnviarXML);
  server.on("/LED", ControleLed);
  server.on("/RGB", ControleRGB);
  server.begin();
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  server.handleClient();
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ControleLed() {
  LED = !LED;
  digitalWrite(PIN_LED, LED);
  Serial.print("Led: "); Serial.println(LED);
  
  if(LED) {
    server.send(200, "text/plain", "1"); // Resposta do estado do LED pra página Html
  }else {
    server.send(200, "text/plain", "0");
  }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ControleRGB(){
  
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Enviar para o servidor o 'MAIN' (Site em html + css + js) que se encontra definido em 'A1.h'
void EnviarSite() {
  Serial.println("Enviando PáginaWeb");
  server.send(200, "text/html", MAIN);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// code to send the main web page
// I avoid string data types at all cost hence all the char mainipulation code
void EnviarXML() {
  strcpy(XML, "<?xml version = '1.0'?>\n<Data>\n");

  // show LED status
  if (LED) {
    strcat(XML, "<LED>1</LED>\n");
  }
  else {
    strcat(XML, "<LED>0</LED>\n");
  }

  //SHOW RGB STATUS
  const char REDstatus = "<RED>";
  strcat(REDstatus, REDvalue);
  strcat(REDstatus, "</RED>");
  
  const char GREENstatus = "<GREEN>";
  strcat(GREENstatus, GREENvalue);
  strcat(GREENstatus, "</GREEN>");
  
  const char BLUEstatus = "<BLUE>";
  strcat(BLUEstatus, BLUEvalue);
  strcat(BLUEstatus, "</BLUE>");
  

  strcat(XML, REDstatus);
  strcat(XML, GREENstatus);
  strcat(XML, BLUEstatus);
  
  Serial.println(XML);
  
  server.send(200, "text/xml", XML);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void printWifiStatus() {
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
  
  Serial.print("Open http://");
  Serial.println(ip);
}
