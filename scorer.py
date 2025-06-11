import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

class InterviewScorer:
    def __init__(self):
        self.model = joblib.load("models/model.pkl")
        self.scaler = joblib.load("models/scaler.pkl")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')

    def score(self, transcript: str, resume: str):
        text = transcript + " " + resume
        embedding = self.embedder.encode([text])
        embedding_scaled = self.scaler.transform(embedding)

        prediction = self.model.predict(embedding_scaled)[0]
        proba = self.model.predict_proba(embedding_scaled)[0][prediction]
        score = int(proba * 100)

        return {
            "label": "Selected" if prediction == 1 else "Rejected",
            "score": score,
            "proba": proba,
        }
