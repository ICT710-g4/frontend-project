from flask import Flask, request, jsonify, render_template, Response
import json
import requests
import time
import csv
import codecs
from contextlib import closing

#CONSTANTS
API_URL = 'http://taist-2020-heroku.herokuapp.com/api/sensor_data?device_id=1&limit=1&type=predicted'

app = Flask(__name__, template_folder = 'frontend_interface')
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event')
def event_data():
    def post_data():
        API_URL = 'http://taist-2020-heroku.herokuapp.com/api/sensor_data?device_id=1&limit=1&type=predicted'
        fieldnames = ["device_id","roll","pitch","yaw","acc_x","acc_y","acc_z","label","type","timestamp"]
        json_dict = list()
        for num in range(1,10):
            API_URL = f"http://taist-2020-heroku.herokuapp.com/api/sensor_data?device_id={num}&limit=1&type=predicted"
            with closing(requests.get(API_URL, stream=True)) as r:
                text = r.text[1:-4]
                if not text : continue
                text = text.split(',')
                json_temp = dict()
                i = 0
                for column in fieldnames:
                    json_temp[column] = text[i]
                    i+=1
                json_dict.append(json_temp)
        json_data = json.dumps(json_dict)
        yield f"data:{json_data}\n\n"
        time.sleep(1)
    return Response(post_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
