#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
