from flask import Flask, jsonify, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Settings
MQTT_BROKER = 'mqtt.example.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'sensor/data'

# MQTT Client
mqtt_client = mqtt.Client()

# Dashboard route
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API endpoint to fetch sensor data
@app.route('/api/sensor_data')
def get_sensor_data():
    # Simulate fetching data from the MQTT broker
    sensor_data = {'temperature': 22.5, 'humidity': 60}
    return jsonify(sensor_data)

# Function to handle incoming MQTT messages
def on_message(client, userdata, message):
    # Handle incoming messages here
    print(f'Received message: {message.payload.decode()}')

# Set up MQTT client and connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.loop_start()  # Start the MQTT loop in a background thread

if __name__ == '__main__':
    app.run(debug=True)
