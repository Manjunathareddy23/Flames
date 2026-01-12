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

/* ===== FULL PAGE BACKGROUND ===== */
.stApp {
    background: url("bg.jpeg") no-repeat center center fixed;
    background-size: cover;
}

/* remove default padding */
.block-container {
    padding-top: 1.5rem;
}

/* ===== TITLE DIRECTLY ON BACKGROUND ===== */
.title {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    margin-bottom: 30px;
    letter-spacing: 2px;
    color: #ffd9f3;
    text-shadow:
        0 0 12px rgba(255, 105, 180, 0.9),
        0 0 30px rgba(255, 20, 147, 0.7),
        0 0 55px rgba(255, 0, 150, 0.6);
}

/* ===== GLASS CARD (CONTENT ONLY) ===== */
.glass {
    background: rgba(20, 10, 40, 0.72);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 35px;
    box-shadow: 0 0 40px rgba(255, 0, 150, 0.45);
    border: 1px solid rgba(255,255,255,0.18);
}

/* ===== LABELS ===== */
label {
    color: #ffe3f5 !important;
    font-weight: 600;
}

/* ===== INPUTS ===== */
input {
    background: rgba(0,0,0,0.55) !important;
    color: #ffffff !important;
    border-radius: 14px !important;
    border: 1px solid #ff4ecd !important;
    padding: 12px !important;
}

/* ===== BUTTON ===== */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #ff4ecd, #ff7eb3);
    color: white;
    font-size: 20px;
    border-radius: 16px;
    padding: 14px;
    font-weight: bold;
    box-shadow: 0 0 25px rgba(255, 78, 205, 0.85);
    transition: all 0.35s ease;
}

.stButton button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 45px rgba(255, 200, 230, 1);
}

/* ===== RESULT ===== */
.result {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 30px;
    color: #fff1b8;
    text-shadow:
        0 0 15px rgba(255, 204, 112, 0.9),
        0 0 30px rgba(255, 153, 51, 0.8);
}

/* ===== EMOJI FLOAT ===== */
.emoji {
    position: fixed;
    bottom: -50px;
    font-size: 34px;
    animation: floatUp 7s linear infinite;
}

@keyframes floatUp {
    0% {transform: translateY(0); opacity: 0;}
    10% {opacity: 1;}
    100% {transform: translateY(-130vh); opacity: 0;}
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

# TITLE ON BACKGROUND (NOT INSIDE GLASS)
st.markdown("<div class='title'>🔥 FLAMES Game 🔥</div>", unsafe_allow_html=True)

# CONTENT CARD
st.markdown("<div class='glass'>", unsafe_allow_html=True)

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

        for _ in range(25):
            left = random.randint(0, 100)
            delay = random.uniform(0, 4)
            st.markdown(
                f"<div class='emoji' style='left:{left}%; animation-delay:{delay}s'>{emoji}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter both names")

st.markdown("</div>", unsafe_allow_html=True)
