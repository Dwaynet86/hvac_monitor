#! /usr/bin/env python3

import paho.mqtt.client as mqtt
#from read_sensors import * 
from mqtt_pub_sub import *
from time import sleep


supply_temperature = 10
supply_humidity = 10
supply_pressure = 10
return_temperature = 5
return_humidity = 5
return_pressure = 5
delta_temperature = 1
static_pressure = 0.41
cfm = 500

def get_sensor_data():
  print("reading sensor data...")
  supply_temperature, supply_humidity, supply_pressure = (70, 54, 20.8)
  return_temperature, return_humidity, return_pressure = (20, 40, 15.4)
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
  get_sensor_data()
  #client.publish("hassio/hvac_monitor/status/","supply:70",2)
  publish_data = "supply temperature: " + supply_temperature + ", supply humidity: " + supply_humidity + ", supply pressure: " + supply_pressure
  
  client.publish("hassio/hvac_monitor/status/",publish_data,2)
  print (supply_temperature, supply_humidity, supply_pressure)
  print (return_temperature, return_humidity, return_pressure)
  

