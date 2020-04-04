from flask import Flask, request, jsonify
import json
import requests
import time
import csv

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
        json_data =[]
        csv_data = requests.get(API_URL)
        reader = csv.DictReader(csv_data)
        for row in reader:
            json_data.append(row)
        yield f"data:{json_data}\n\n"
        time.sleep(1)
    return Response(post_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
