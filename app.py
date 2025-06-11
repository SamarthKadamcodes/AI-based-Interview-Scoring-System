import streamlit as st
from scorer import InterviewScorer

st.set_page_config(page_title="🧠 AI Interview Scorer", layout="centered")

# ---------- Styling ----------
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5f7fa;
        }
        .stTextArea label {
            font-weight: 600;
            color: #1f2937;
        }
        .score-box {
            padding: 1.5rem;
            background: linear-gradient(145deg, #ffffff, #e6ebf1);
            border-radius: 16px;
            border: 1px solid #d1d5db;
            margin-top: 2rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        }
        .score-value {
            font-size: 2rem;
            font-weight: bold;
            margin: 0.5rem 0;
        }
        .prediction-label {
            font-size: 1.5rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center; color: #374151;'>AI Interview Scorer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #6b7280;'>Upload interview and resume content to get an intelligent score prediction.</p>",
    unsafe_allow_html=True)

# ---------- Inputs ----------
transcript = st.text_area("🗣️ Interview Transcript", height=200, placeholder="Paste the full transcript here...")
resume = st.text_area("📄 Candidate Resume", height=200, placeholder="Paste the candidate's resume here...")

# ---------- Prediction ----------
if st.button("🎯 Score Candidate", use_container_width=True):
    scorer = InterviewScorer()
    result = scorer.score(transcript, resume)

    # Score bar color logic
    score = result['score']
    label = result['label']
    label_color = "green" if label == "Selected" else "red"

    # ---------- Display Card ----------
    st.markdown(f"""
        <div class="score-box">
            <div class="prediction-label" style="color: {label_color};">
                Prediction: {label}
            </div>
            <div class="score-value">
                Score: {score}/100
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------- Verdict Feedback ----------
    if score >= 80:
        st.success("🌟 Excellent fit for the role")
    elif score >= 60:
        st.info("Decent potential, consider further evaluation")
    elif score >= 40:
        st.warning("Need improvement")
    else:
        st.error("❌ Not a strong match")