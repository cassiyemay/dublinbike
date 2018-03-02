from flask import Flask
from flask import render_template
from StationInfo import fetch_station_info
from StationInfo import StationInfo
import json
from flask import jsonify
import pandas as py


app = Flask(__name__)


@app.route('/')
def dublinbikes():

    # get station information
    StationInfo = fetch_station_info()

    return render_template("index.html", StationInfo = StationInfo)


if __name__ == '__main__':
    app.run()
