#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// DHT22 sensor settings
#define DHTPIN 4         // Pin where the DHT22 is connected
#define DHTTYPE DHT22    // DHT 22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

// WiFi settings
const char* ssid = "your_SSID";          // SSID of your WiFi
const char* password = "your_PASSWORD";  // Password of your WiFi

// MQTT settings
const char* mqtt_server = "broker.hivemq.com";
const char* mqtt_topic = "esp32/dht22";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Read temperature and humidity
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Publish the readings
  if (!isnan(h) && !isnan(t)) {
    String payload = "{";  
    payload += "\"temperature\":";  
    payload += t; 
    payload += ", \"humidity\":";  
    payload += h; 
    payload += "}";
    client.publish(mqtt_topic, (char*) payload.c_str());
    Serial.println(payload);
  } else {
    Serial.println("Failed to read from DHT sensor!");
  }

  delay(2000);  // Wait for 2 seconds before next reading
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}