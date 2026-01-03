import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# Base directory (project folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to CSV file
DATA_PATH = os.path.join(BASE_DIR, "data", "electricity_data.csv")

# Load dataset
data = pd.read_csv(DATA_PATH)

# Encode season
data["season"] = data["season"].map({
    "winter": 0,
    "monsoon": 1,
    "summer": 2
})

# Features and target
X = data[["units", "season", "appliances", "family_members"]]
y = data["bill"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model
MODEL_PATH = os.path.join(BASE_DIR, "electricity_model.pkl")
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully as electricity_model.pkl")