from os import name
import os
from flask import Flask, render_template, request,jsonify
from requests.models import Response
from werkzeug.wrappers import response
from flight_data import getFlightData 
import json

app = Flask(__name__)







@app.route('/', methods=['GET'])
def index():
    fileData = 0;
    with open('airports.json', 'r') as f:
      fileData = json.load(f)
      f.close()
    return render_template('web_design.html', fileData = fileData)


@app.route('/', methods=['POST'])
def formSubmit():
    response = getFlightData(request.form)
    print(response)
    return render_template('search_result.html', result_data = response)
    # return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)