from flask import Flask
from flask import request
# Pickle package
import pickle
# from ML.test_model import irrigate_or_not_irrigate
app = Flask(__name__)



# load the model from disk
irrigation_model = './ml_models/irrigation_model.sav'
loaded_model = pickle.load(open(irrigation_model, 'rb'))

def irrigate_or_not_irrigate(soil_moisture):
    if(loaded_model.predict([[soil_moisture]]))==0:
        return 'Irrigate'
    else:
        return 'Not irrigate'


@app.route("/")
def home_view():
        return {
            "api_status": "Up and running"
        }


# Irrigation model api endpoint http://127.0.0.1:8000/api/model/irrigation
@app.post('/api/model/irrigation')
def predict():
        soil_moisture = request.form.get('soil_moisture')
        predictions = irrigate_or_not_irrigate(int(soil_moisture))
        return {
            "predictions": predictions
        }