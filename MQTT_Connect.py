import paho.mqtt.client as mqtt

MQTT_SERVER = "10.0.0.20"
MQTT_PORT = 1883
MQTT_PATH = "hvac_monitor"
MQTT_USER = "DEVMQTT"
MQTT_PASS = "DEVMQTT"
MQTT_CLIENT = "HVAC-MONITOR"


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()

    
client = mqtt.Client(MQTT_CLIENT)
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect (MQTT_SERVER, port=MQTT_PORT)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

#client.disconnect()


