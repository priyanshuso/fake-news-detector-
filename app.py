import streamlit as st
import pickle

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# ---------------- Load CSS ---------------- #
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- Load Model ---------------- #
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# ---------------- Header ---------------- #
st.markdown("""
<div class="hero">
<h1>📰 Fake News Detector</h1>
<p>Detect whether a news article is <b>Real</b> or <b>Fake</b> using Machine Learning.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.title("🤖 Model Information")

    st.success("Model : Linear SVM")
    st.success("Accuracy : 99.30%")
    st.success("Vectorizer : TF-IDF")
    st.success("Dataset : Fake + True News")

    st.markdown("---")

    st.markdown("""
### Features

- Detect Fake News
- Linear SVM Model
- TF-IDF Vectorization
- Fast Prediction
- Professional UI
""")

# ---------------- Main ---------------- #
st.subheader("Paste News Article")

news = st.text_area(
    "News Article",
    height=250,
    placeholder="Paste your news article here..."
)

# ---------------- Prediction ---------------- #
if st.button("🔍 Detect News"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:

        transformed = vectorizer.transform([news])

        prediction = model.predict(transformed)

        if prediction[0] == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

# ---------------- Footer ---------------- #
st.markdown("---")

st.markdown("""
<center>

Developed by **Priyanshu Soni**

Machine Learning | NLP | Streamlit

</center>
""", unsafe_allow_html=True)