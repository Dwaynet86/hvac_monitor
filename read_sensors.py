#! /usr/bin/env python3

import smbus2
import bme280

#setup
port = 1
supply_address = 0x76
return_address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, supply_address)
calibration_params = bme280.load_calibration_params(bus, return_address)
# the sample method will take a single reading and return a
# compensated_reading object


def read_adc(address):
  if 1:
    #Supply sensor
    supply_data = bme280.sample(bus, supply_address, calibration_params)
    
    print(supply_data)
    return (supply_data.temperature, supply_data.pressure, supply_data.humidity)
  
  elif 2:
    # Return Sensor
    return_data = bme280.sample(bus, return_address, calibration_params)
    
    print(return_data)
    return (return_data.temperature, return_data.pressure, return_data.humidity)
  
  else: 
    return (0, 0, 0)


