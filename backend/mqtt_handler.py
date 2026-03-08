import paho.mqtt.client as mqtt
import sqlite3

# Database setup
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       topic TEXT,
                       payload TEXT,
                       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                   )''')
conn.commit()

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f'Received message on topic {msg.topic}: {msg.payload.decode()}')
    # Store the received message in the database
    cursor.execute("INSERT INTO SensorData (topic, payload) VALUES (?, ?)", (msg.topic, msg.payload.decode()))
    conn.commit()

# MQTT setup
client = mqtt.Client()
client.on_message = on_message

client.connect('mqtt_broker_address', 1883, 60)

# Subscribe to the sensor topic
client.subscribe('sensor/topic')

# Start the loop
client.loop_forever()