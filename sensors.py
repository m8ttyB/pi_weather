#!/usr/bin/env python
import datetime
from ds18b20 import DS18B20

sensor = DS18B20()

def get_time():
   now = datetime.datetime.now()
   return now.strftime("%Y-%m-%d %H:%M")

def get_kelvin():
    return sensor.get_temperatures([DS18B20.KELVIN])

def get_celsius():
    return sensor.get_temperatures([DS18B20.DEGREES_C])

def get_fahrenheit():
    return sensor.get_temperatures([DS18B20.DEGREES_F])
