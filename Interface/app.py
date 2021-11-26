import folium
import pandas as pd
from folium.plugins import HeatMap
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
        return render_template('index.html')


@app.route('/map')
def map():
    return render_template('map_all_locations.html')

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap_all_locations.html')


if __name__ == "__main__":
    app.run(debug=True)