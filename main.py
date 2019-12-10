#!/usr/bin/python3

import paho.mqtt.client as mqtt
import mqtt_connect.py


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  print("Subscribing...")
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
  if msg.payload.decode() == "Disconnect":
    print("Disconnecting...")
    client.disconnect()

    
def on_publish(client, userdata, flags):
  print("published!")

  
  
def on_subscribe(client, userdata, flags):
  print("subscribed")  

def set_temperature(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
    print("set_temperature")
    print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
  
  
client = mqtt.Client(MQTT_CLIENT)
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect (MQTT_SERVER, port=MQTT_PORT)
client.message_callback_add("$SYS/broker/hvac_monitor/set/temperature/#", set_temperature)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.loop_forever()
