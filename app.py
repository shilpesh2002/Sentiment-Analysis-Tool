import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "Positive 😊", score['compound']
    elif score['compound'] <= -0.05:
        return "Negative 😞", score['compound']
    else:
        return "Neutral 😐", score['compound']

# Set page config
st.set_page_config(page_title="Sentiment Analysis", page_icon="🔍", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stTextArea textarea {
            font-size: 18px;
            padding: 10px;
        }
        .stButton button {
            background-color: #FF4B4B !important;
            color: white !important;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
        }
        .result-box {
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
        }
        .sidebar-text {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar info
st.sidebar.header("ℹ️ About the Tool")
st.sidebar.write("""
This tool uses **VADER Sentiment Analysis** to analyze the sentiment of your text in real time.
It categorizes text into **Positive**, **Negative**, or **Neutral** based on the words used.
""")

st.sidebar.markdown("---")
st.sidebar.write("📌 **How it Works?**")
st.sidebar.write("""
- Enter your text in the text box.
- Click the **Analyze Sentiment** button.
- Get instant sentiment results with a confidence score!
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 **Developed for On-Job Training Assignment**")

# Main Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🔍 Sentiment Analysis Tool</h1>", unsafe_allow_html=True)
st.markdown("### Analyze the sentiment of your text using AI-powered VADER analysis.")

st.markdown("---")

# Text Input
user_input = st.text_area("✍️ Enter text below:", height=150, placeholder="Type your text here...")

# Button click event
if st.button("Analyze Sentiment"):
    if user_input:
        sentiment, score = analyze_sentiment(user_input)
        st.session_state.sentiment = sentiment
        st.session_state.score = score
    else:
        st.warning("⚠️ Please enter some text for analysis!")

# Display results instantly after clicking the button
if "sentiment" in st.session_state:
    st.markdown(f"<div class='result-box'>Sentiment: {st.session_state.sentiment}</div>", unsafe_allow_html=True)
    st.progress((st.session_state.score + 1) / 2)  # Normalizing compound score for progress bar

    # Sentiment Message
    if "Positive" in st.session_state.sentiment:
        st.success("🎉 Your text has a **Positive** sentiment!")
    elif "Negative" in st.session_state.sentiment:
        st.error("💔 Your text has a **Negative** sentiment!")
    else:
        st.info("🙂 Your text has a **Neutral** sentiment!")
