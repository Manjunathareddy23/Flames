import streamlit as st
import random
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🔥 FLAMES Game",
    page_icon="❤️",
    layout="centered"
)

# ---------------- LOAD BACKGROUND ----------------
def load_bg(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = load_bg("bg.jfif")

# ---------------- CSS ----------------
st.markdown(f"""
<style>

/* ===== BACKGROUND ===== */
html, body, [data-testid="stApp"] {{
    height: 100%;
}}

[data-testid="stApp"] {{
    background: url("data:image/jfif;base64,{bg_img}") no-repeat center center fixed;
    background-size: cover;
}}

/* ===== PAGE CONTAINER ===== */
.block-container {{
    padding-top: 2rem;
}}

/* ===== HEADER BOX (FIXED POSITIONING) ===== */
.header-box {{
    max-width: 600px;
    margin: auto;
    text-align: center;
    padding: 15px 0 30px 0;
}}

/* ===== TITLE (NO ANIMATION, NO MOVEMENT) ===== */
.title {{
    font-size: 56px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #ffe6f2;
    text-shadow:
        0 0 12px rgba(255, 80, 180, 1),
        0 0 30px rgba(255, 0, 150, 0.8),
        0 0 60px rgba(255, 0, 150, 0.6);
}}

/* ===== GLASS CARD ===== */
.glass {{
    max-width: 520px;
    margin: auto;
    background: rgba(15, 8, 35, 0.75);
    backdrop-filter: blur(18px);
    border-radius: 26px;
    padding: 40px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 30px rgba(255, 0, 150, 0.4);
}}

/* ===== INPUTS ===== */
input {{
    background: rgba(0,0,0,0.65) !important;
    color: #ffffff !important;
    border-radius: 16px !important;
    border: 1px solid #ff5fbf !important;
    padding: 14px !important;
}}

/* ===== BUTTON ===== */
.stButton button {{
    width: 100%;
    background: linear-gradient(135deg, #ff3cac, #784ba0, #2b86c5);
    color: white;
    font-size: 20px;
    border-radius: 20px;
    padding: 16px;
    font-weight: 800;
    border: none;
    box-shadow: 0 0 25px rgba(255, 60, 172, 0.9);
}}

.stButton button:hover {{
    transform: scale(1.05);
}}

/* ===== RESULT ===== */
.result {{
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    margin-top: 30px;
    color: #fff0b3;
}}

/* ===== EMOJI ===== */
.emoji {{
    position: fixed;
    bottom: -60px;
    font-size: 36px;
    animation: floatUp 6s linear infinite;
}}

@keyframes floatUp {{
    0% {{transform: translateY(0); opacity: 0;}}
    10% {{opacity: 1;}}
    100% {{transform: translateY(-140vh); opacity: 0;}}
}}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIC ----------------
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
st.markdown("""
<div class="header-box">
    <div class="title">🔥 FLAMES Game 🔥</div>
</div>
""", unsafe_allow_html=True)

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
            delay = random.uniform(0, 3)
            st.markdown(
                f"<div class='emoji' style='left:{left}%; animation-delay:{delay}s'>{emoji}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter both names")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("Made by Manjunathareddy💻")
