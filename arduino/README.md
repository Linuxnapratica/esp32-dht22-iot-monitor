# Arduino IDE Setup for ESP32 DHT22 IoT Monitor

## 1. Install Arduino IDE
- Download the latest version of Arduino IDE from the [Arduino website](https://www.arduino.cc/en/software).
- Follow the installation instructions for your OS.

## 2. Setup ESP32 Board in Arduino IDE
- Open Arduino IDE.
- Go to **File** -> **Preferences**.
- In the **Additional Board Manager URLs** field, add the following URL:
  `https://dl.espressif.com/dl/package_esp32_index.json`
- Click **OK**.

## 3. Install ESP32 Board in Arduino IDE
- Go to **Tools** -> **Board** -> **Board Manager**.
- Type `esp32` in the search bar.
- Install the package by Espressif Systems.

## 4. Install Required Libraries
- Go to **Sketch** -> **Include Library** -> **Manage Libraries**.
- In the Library Manager, search for and install the following libraries:
  - **DHT sensor library** by Adafruit
  - **Adafruit Unified Sensor** library

## 5. Configure Your Sketch
- Connect your DHT22 sensor to the ESP32:
  - Connect the VCC pin to 3.3V.
  - Connect the GND pin to Ground.
  - Connect the Data pin to a digital pin (e.g., GPIO 4).

- Open the provided example sketch and modify it according to your configuration:
  - Set the correct pin number for the Data pin.
  - Adjust any other configuration settings as necessary.

## 6. Upload the Code
- Connect your ESP32 to your computer. 
- Select the appropriate board: **Tools** -> **Board** -> select **ESP32 Dev Module**.
- Select the appropriate port: **Tools** -> **Port** -> select your ESP32 port.
- Click on the upload button to upload your sketch.

## 7. Monitor the Output
- Open the Serial Monitor (Tools -> Serial Monitor) to view the output from the DHT22 sensor.