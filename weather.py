#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import jsonify, Flask, render_template
import sensors


app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    templateData = {
        'title': 'Temperature :: Home',
        'time': sensors.get_time(),
        'kelvin': sensors.get_kelvin(),
        'celsius': sensors.get_celsius(),
        'fahrenheit': sensors.get_fahrenheit()
    }
    return render_template('main.html', **templateData)

@app.route('/weather/')
def current_weather():
    templateData = {
        'title': 'Temperature :: Home',
        'time': sensors.get_time()
        }
    return render_template('current_weather.html', **templateData)


@app.route('/weather/api/v1.0/temperature', methods=['GET'])
def get_temp():
    weather_data = [
        {
            'id': 'temperature',
            'time_stamp': sensors.get_time(),
            'kelvin': sensors.get_kelvin(),
            'celsius': sensors.get_celsius(),
            'fahrenheit': sensors.get_fahrenheit()
        }
    ]
    return jsonify({'weather_data': weather_data})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444, debug=True)
