# ESP32 DHT22 IoT Monitor

## Overview
This project utilizes the ESP32 microcontroller and the DHT22 temperature and humidity sensor to monitor environmental conditions. The data can be displayed on a web interface and is ideal for IoT applications.

## Features
- Real-time temperature and humidity monitoring
- Web-based user interface
- Support for multiple DHT22 sensors
- Mobile-friendly design

## Hardware Requirements
- ESP32 development board
- DHT22 temperature & humidity sensor
- Jumper wires
- Breadboard (optional)

## Installation
1. Clone the repository:  
   `git clone https://github.com/Linuxnapratica/esp32-dht22-iot-monitor.git`
2. Open the project in your IDE (e.g., Arduino IDE).
3. Install necessary libraries for DHT22 and ESP32.
4. Connect the ESP32 to your computer and upload the code.

## Wiring Diagram
- **ESP32 Pin 23** → **DHT22 Data Pin**  
- **ESP32 Pin 3.3V** → **DHT22 VCC Pin**  
- **ESP32 Ground** → **DHT22 GND Pin**  

![Wiring Diagram](https://example.com/wiring_diagram)

## Usage
1. Open the serial monitor in your IDE to view debug messages.
2. Connect to the ESP32 WiFi network using the credentials provided in the code.
3. Open a web browser and navigate to the ESP32's IP address to access the user interface.

## Troubleshooting
- **Problem**: DHT22 not responding.  
  **Solution**: Check the wiring and ensure the DHT22 is powered correctly.
- **Problem**: Code fails to upload.  
  **Solution**: Ensure you have the correct board and port selected in your IDE.

For additional support, open an issue in the GitHub repository.