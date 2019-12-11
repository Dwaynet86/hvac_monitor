#! /usr/bin/env python3

import paho.mqtt.client as mqtt
from mqtt_pub_sub import *
from time import sleep

def read_sensors()
  print("reading sensor data...")
  supply_temperature = read_adc(1)
  return_temperature = read_adc(2)
  
  supply_humidity = read_adc(3)
  return_humidity = read_adc(4)
  
  supply_pressure = read_adc(5)
  return_pressure = read_adc(6)
  
  return


#setup  
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

#Main loop
while True:
  sleep(10)
  client.publish("hassio/hvac_monitor/status/","supply:70",2)
  

