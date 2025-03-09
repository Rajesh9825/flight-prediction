from flask import Flask,request,jsonify
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application

# Route for home page
@app.route('/')
def index():
    return "Hello Wolrd"


@app.route('/predict',methods=['POST'])
def predict_data():
    try:
        data = CustomData( airline =request.form.get("airline") ,
            source_city=request.form.get("source_city"),
            departure_time= request.form.get("departure_time"),
            stops= request.form.get("stops"),
            arrival_time=request.form.get("arrival_time"),
            destination_city=request.form.get("destination_city"),
            Class=request.form.get("Class"),
            duration=float(request.form.get("duration")),
            days_left=int(request.form.get("days_left"))
            )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)

        return jsonify({"Prediction" : results[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)



