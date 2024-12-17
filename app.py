from flask import Flask, render_template, request, jsonify
from weather import get_weather_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weatherdata/<string:city>')
def getweatherdata(city):
    temp_data = {"temperature": get_weather_data(city)[0],
                 "windspeed": get_weather_data(city)[2],
                 "winddirection": get_weather_data(city)[3],
                 "elevation": get_weather_data(city)[4]}
    return jsonify(temp_data)
    #return str(get_weather_data(city)[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)