import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🔥 FLAMES Game",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* ----- BACKGROUND ----- */
.stApp {
    background: url("bg.png");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ----- GLASS CARD ----- */
.glass {
    background: rgba(20, 10, 40, 0.75);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 0 40px rgba(255, 0, 150, 0.4);
    border: 1px solid rgba(255,255,255,0.15);
}

/* ----- TITLE ----- */
.title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff4ecd, #ffcc70);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 25px rgba(255, 0, 200, 0.6);
}

/* ----- INPUTS ----- */
input {
    background: rgba(0,0,0,0.6) !important;
    color: #fff !important;
    border-radius: 12px !important;
    border: 1px solid #ff4ecd !important;
}

/* ----- BUTTON ----- */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #ff4ecd, #ff7eb3);
    color: white;
    font-size: 20px;
    border-radius: 14px;
    padding: 14px;
    font-weight: bold;
    box-shadow: 0 0 20px rgba(255, 78, 205, 0.8);
    transition: 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px rgba(255, 204, 112, 1);
}

/* ----- RESULT TEXT ----- */
.result {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    margin-top: 25px;
    color: #ffcc70;
    text-shadow: 0 0 25px rgba(255, 204, 112, 0.9);
}

/* ----- EMOJI ANIMATION ----- */
.emoji {
    position: fixed;
    bottom: -40px;
    font-size: 32px;
    animation: floatUp 6s linear infinite;
}

@keyframes floatUp {
    0% {transform: translateY(0); opacity: 0;}
    10% {opacity: 1;}
    100% {transform: translateY(-120vh); opacity: 0;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLAMES LOGIC ----------------
def flames_result(name1, name2):
    n1 = list(name1.lower().replace(" ", ""))
    n2 = list(name2.lower().replace(" ", ""))

    for ch in n1[:]:
        if ch in n2:
            n1.remove(ch)
            n2.remove(ch)

    count = len(n1) + len(n2)

    flames = ["F", "L", "A", "M", "E", "S"]
    idx = 0
    while len(flames) > 1:
        idx = (idx + count - 1) % len(flames)
        flames.pop(idx)

    return flames[0]

# ---------------- UI ----------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🔥 FLAMES Game 🔥</div>", unsafe_allow_html=True)

name1 = st.text_input("👤 Your Name")
name2 = st.text_input("❤️ Crush / Friend Name")

if st.button("✨ Calculate FLAMES ✨"):
    if name1 and name2:
        result = flames_result(name1, name2)

        meanings = {
            "F": ("Friends 🤝", "🤝"),
            "L": ("Love ❤️", "❤️"),
            "A": ("Affection 😊", "😊"),
            "M": ("Marriage 💍", "💍"),
            "E": ("Enemy 😡", "😡"),
            "S": ("Sister 😇", "😇"),
        }

        text, emoji = meanings[result]
        st.markdown(f"<div class='result'>{text}</div>", unsafe_allow_html=True)

        # Emoji rain animation
        for i in range(25):
            left = random.randint(0, 100)
            delay = random.uniform(0, 4)
            st.markdown(
                f"<div class='emoji' style='left:{left}%; animation-delay:{delay}s'>{emoji}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter both names")

st.markdown("</div>", unsafe_allow_html=True)
