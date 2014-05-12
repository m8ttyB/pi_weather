#!/usr/bin/env python

from flask import jsonify, Flask, render_template
import sensors

app = Flask(__name__)

@app.route('/')
def home():
   templateData = {
      'title': 'Temperature :: 34 Orchard Lane',
      'time': sensors.get_time(),
      'kelvin': sensors.get_kelvin(),
      'celsius': sensors.get_celsius(),
      'fahrenheit': sensors.get_fahrenheit()
      }
   return render_template('main.html', **templateData)

weather_data = [
    {
        'id': 'weather_data',
        'time_stamp': sensors.get_time(),
        'kelvin': sensors.get_kelvin(),
        'celsius': sensors.get_celsius(),
        'fahrenheit': sensors.get_fahrenheit()
    }
]

@app.route('/weather/api/v1.0/temperature', methods = ['GET'])
def get_temp():
   return jsonify( { 'weather_data': weather_data } )

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4444, debug=True)
