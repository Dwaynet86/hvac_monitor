#! /usr/bin/env python3

import paho.mqtt.client as mqtt
from mqtt_connect import *
from time import sleep
import os

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
  
client = mqtt.Client(MQTT_CLIENT)
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect (MQTT_SERVER, port=MQTT_PORT)
client.message_callback_add("hvac_monitor/set/#", on_set)
client.message_callback_add("hvac_monitor/disconnect", on_disconnect)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.loop_start()
while True:
  sleep(10)
  client.publish("hassio/hvac_monitor/status/","supply:70",2)
  

