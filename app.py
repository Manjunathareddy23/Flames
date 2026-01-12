import streamlit as st
import random
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FLAMES Game",
    page_icon="🔥",
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

/* ===== PAGE BACKGROUND ===== */
html, body, [data-testid="stApp"] {{
    height: 100%;
}}

[data-testid="stApp"] {{
    background-image: url("data:image/jfif;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* ===== CENTER WRAPPER ===== */
.app-wrapper {{
    max-width: 420px;
    margin: 6vh auto;
    padding: 28px;
    background: rgba(18, 16, 28, 0.78);
    backdrop-filter: blur(16px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 12px 35px rgba(0,0,0,0.45);
}}

/* ===== TITLE ===== */
.app-title {{
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 22px;
    color: #ffffff;
    letter-spacing: 1px;
}}

/* ===== SUBTEXT ===== */
.app-sub {{
    text-align: center;
    font-size: 14px;
    color: #cfcfe6;
    margin-bottom: 28px;
}}

/* ===== INPUTS ===== */
input {{
    background: rgba(255,255,255,0.08) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    padding: 12px !important;
    font-size: 15px !important;
}}

/* ===== BUTTON ===== */
.stButton button {{
    width: 100%;
    background: #ff4d6d;
    color: #fff;
    font-size: 16px;
    padding: 12px;
    border-radius: 14px;
    font-weight: 600;
    border: none;
    margin-top: 10px;
    transition: background 0.25s ease;
}}

.stButton button:hover {{
    background: #ff3357;
}}

/* ===== RESULT ===== */
.result {{
    text-align: center;
    font-size: 26px;
    font-weight: 600;
    margin-top: 24px;
    color: #ffd166;
}}

/* ===== EMOJI FLOAT ===== */
.emoji {{
    position: fixed;
    bottom: -40px;
    font-size: 28px;
    animation: floatUp 5.5s linear infinite;
}}

@keyframes floatUp {{
    0% {{transform: translateY(0); opacity: 0;}}
    10% {{opacity: 1;}}
    100% {{transform: translateY(-120vh); opacity: 0;}}
}}

@media (max-width: 480px) {{
    .app-wrapper {{
        margin: 4vh 16px;
        padding: 22px;
    }}
    .app-title {{
        font-size: 34px;
    }}
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
<div class="app-wrapper">
    <div class="app-title">🔥 FLAMES Game</div>
    <div class="app-sub">Just for fun — not serious ❤️</div>
""", unsafe_allow_html=True)

name1 = st.text_input("Your Name")
name2 = st.text_input("Crush / Friend Name")

if st.button("Calculate"):
    if name1 and name2:
        r = flames_result(name1, name2)
        meanings = {
            "F": ("Friends 🤝", "🤝"),
            "L": ("Love ❤️", "❤️"),
            "A": ("Affection 😊", "😊"),
            "M": ("Marriage 💍", "💍"),
            "E": ("Enemy 😡", "😡"),
            "S": ("Sister 😇", "😇"),
        }
        text, emoji = meanings[r]
        st.markdown(f"<div class='result'>{text}</div>", unsafe_allow_html=True)

        for _ in range(18):
            st.markdown(
                f"<div class='emoji' style='left:{random.randint(0,100)}%; animation-delay:{random.uniform(0,3)}s'>{emoji}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("Please enter both names")

st.markdown("</div>", unsafe_allow_html=True)
