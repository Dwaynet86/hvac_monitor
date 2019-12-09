import paho.mqtt.client as mqtt

MQTT_SERVER = "10.0.0.20"
MQTT_PORT = 1883
MQTT_PATH = "hvac_monitor"
MQTT_USER = "DEVMQTT"
MQTT_PASS = "DEVMQTT"
MQTT_CLIENT = "HVAC-MONITOR"

client = mqtt.Client(MQTT_CLIENT)
client.connect (MQTT_SERVER, port=MQTT_PORT)
client.close()

