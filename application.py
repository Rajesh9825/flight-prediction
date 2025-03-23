from flask import Flask, request, jsonify, render_template
import pickle
from huggingface_hub import hf_hub_download
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Load model from Hugging Face
repo_id = "CV-Raju/flight-price-prediction-model"
filename = "model.pkl"
model_path = hf_hub_download(repo_id=repo_id, filename=filename)

with open(model_path, "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_data():
    try:
        data = CustomData(
            airline=request.form.get("airline"),
            source_city=request.form.get("source_city"),
            departure_time=request.form.get("departure_time"),
            stops=request.form.get("stops"),
            arrival_time=request.form.get("arrival_time"),
            destination_city=request.form.get("destination_city"),
            Class=request.form.get("Class"),
            duration=float(request.form.get("duration")),
            days_left=int(request.form.get("days_left"))
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        transformed_data = predict_pipeline.predict(pred_df)
        results = model.predict(transformed_data)

        return jsonify({"prediction": results[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)

    