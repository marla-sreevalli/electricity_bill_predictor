from flask import Flask, render_template, request
import pickle
import os
from bill_calculator import calculate_bill

app = Flask(__name__)

# 🔹 Absolute path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "electricity_model.pkl")

# 🔹 Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# 🔹 Season mapping
season_map = {
    "winter": 0,
    "monsoon": 1,
    "summer": 2
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        units = int(request.form['units'])
        season = request.form['season'].lower()
        appliances = int(request.form['appliances'])
        family = int(request.form['family'])

        season_value = season_map.get(season, 0)

        predicted_bill = model.predict(
            [[units, season_value, appliances, family]]
        )[0]

        actual_bill = calculate_bill(units)

        if predicted_bill > actual_bill:
            suggestions = [
                "Reduce heavy appliance usage",
                "Use energy-efficient appliances",
                "Avoid peak-hour usage"
            ]
        else:
            suggestions = [
                "Your usage is efficient",
                "Continue current energy habits"
            ]

        return render_template(
            "index.html",
            bill=int(predicted_bill),
            actual_bill=actual_bill,
            suggestions=suggestions
        )

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

