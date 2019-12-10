MQTT_SERVER = "10.0.0.20"
MQTT_PORT = 1883
MQTT_PATH = "hassio/hvac_monitor/#"
MQTT_USER = "DEVMQTT"
MQTT_PASS = "DEVMQTT"
MQTT_CLIENT = "HVAC-MONITOR"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("#")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
  
  print(msg.topic + msg.payload)

    
def on_publish(client, userdata, flags):
  print("published!")

  
  
def on_subscribe(client, userdata, flags):
  print("subscribed")  

def on_set(client, userdata, msg):
    # This callback will only be called for messages with topics that match
    # hvac_monitor/set/#
    
    print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_disconnect(client, userdata, msg):
  if msg.payload.decode() == "Disconnect":
    
    client.loop_stop()
    print("Loop Stopped..")
    client.disconnect()
    print("Disconnected...")
    os._exit(1)
