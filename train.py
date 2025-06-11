import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv('dataset.csv')
df['full_text'] = df['Transcript'].fillna('') + " " + df['Resume'].fillna('')
X = df['full_text'].tolist()
y = df['decision'].map({'select': 1, 'reject': 0})

# Embedding
embedder = SentenceTransformer('all-MiniLM-L6-v2')
X_embeddings = embedder.encode(X)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_embeddings)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
