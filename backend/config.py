class Config:
    # Flask app configuration
    FLASK_ENV = 'development'
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True

    # MQTT broker configuration
    MQTT_BROKER_URL = 'mqtt.example.com'
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = 'your_mqtt_username_here'
    MQTT_PASSWORD = 'your_mqtt_password_here'
    MQTT_KEEPALIVE = 60

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
