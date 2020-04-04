from flask import Flask, request, jsonify
import json
import requests
import time
import csv
import codecs
from contextlib import closing

#CONSTANTS
API_URL = 'https://taist-2020-heroku.herokuapp.com/api/sensor_data'

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event')
def event_data():
    def post_data():
        json_dict =[]
        csv_data = requests.get(API_URL)
        fieldnames = ("device_id","roll","pitch","yaw","acc_x","acc_y","acc_z","label","type","timestamp")
        with closing(requests.get(API_URL, stream=True)) as r:
            reader = csv.DictReader(codecs.iterdecode(r.iter_lines(), 'utf-8'), fieldnames)
            for row in reader:
                json_dict.append(row)
        json_data = json.dumps(json_dict)
        yield f"data:{json_data}\n\n"
        time.sleep(1)
    return Response(post_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
