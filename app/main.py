from flask import Flask
from flask import request
from flask_cors import CORS
from numpy import array
import pickle

app = Flask(__name__)

# enable cors
CORS(app)


# load the models from disk
irrigation_model_filename = './ml_models/irrigation_model.sav'
radiation_model_filename = './ml_models/radiation_model.sav'
test_model_filename = './ml_models/test_model.sav'

# load models using pickle
loaded_model_irrigation = pickle.load(open(irrigation_model_filename, 'rb'))
loaded_model_radiation = pickle.load(open(radiation_model_filename, 'rb'))
loaded_model_test - pickle.load(open(test_model_filename, 'rb'))


@app.route("/")
def home_view():
    return {
        "api_status": "Up and running"
    }


def irrigate_or_not_irrigate(soil_moisture):
    if (loaded_model_irrigation.predict([[soil_moisture]])) == 0:
        return 'Irrigate'
    else:
        return 'Not irrigate'


# Irrigation model api endpoint http://127.0.0.1:8000/api/model/irrigation
@app.post('/api/model/irrigation')
def irrigation():
    predictions = ''
    soil_moisture = request.form.get('soil_moisture')

    if (loaded_model_irrigation.predict([[soil_moisture]])) == 0:
        predictions = 'Irrigate'
    else:
        predictions = 'Not irrigate'

    # response
    return {
        "predictions": predictions
    }


# Radiation model api endpoint http://127.0.0.1:8000/api/model/radiation
@app.post('/api/model/radiation')
def radiation():
    first_interval = request.form.get('first_interval')
    second_interval = request.form.get('sec_interval')
    third_interval = request.form.get('third_interval')

    actual_solar_radiation = array(
        [float(first_interval), float(second_interval), float(third_interval)])
    actual_solar_radiation = actual_solar_radiation.reshape((1, 3, 1))
    predictions = loaded_model_radiation.predict(actual_solar_radiation)

    # response
    return {
        "predictions": predictions.tolist()
    }

    # Radiation model api endpoint http://127.0.0.1:8000/api/model/radiation
@app.post('/api/model/test')
def radiation():
    first_interval = request.form.get('first_interval')
    second_interval = request.form.get('sec_interval')
    third_interval = request.form.get('third_interval')

    actual_solar_radiation = array(
        [float(first_interval), float(second_interval), float(third_interval)])
    actual_solar_radiation = actual_solar_radiation.reshape((1, 3, 1))
    predictions = loaded_model_radiation.predict(actual_solar_radiation)

    # response
    return {
        "predictions": predictions.tolist()
    }
