import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Load data
def load_data(path="data/traffic_samples.csv"):
    df = pd.read_csv(path)
    return df

# Prepare features (no IPs or timestamps)
def preprocess_data(df):
    features = df[["packet_size", "latency_ms"]].copy()
    # Optional: Add protocol encoding
    protocol_encoded = pd.get_dummies(df["protocol"], prefix="proto")
    features = pd.concat([features, protocol_encoded], axis=1)
    return features, df["is_anomaly"]

# Train Isolation Forest
def train_model(X):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    return model

# Save model
def save_model(model, path="models/anomaly_detector.pkl"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f"[✓] Model saved to {path}")

# Full pipeline
def run_training():
    df = load_data()
    X, y = preprocess_data(df)
    model = train_model(X)
    save_model(model)
    # Evaluate
    predictions = model.predict(X)
    df["predicted"] = [1 if p == -1 else 0 for p in predictions]  # -1: anomaly
    accuracy = (df["predicted"] == y).mean()
    print(f"[📊] Accuracy on synthetic data: {accuracy:.2%}")

if __name__ == "__main__":
    run_training()
