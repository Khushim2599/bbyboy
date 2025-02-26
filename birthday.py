import streamlit as st

# Hardcoded name
birthday_person = "Dhuv"  # Change this to the name you want

# Custom CSS for background and styling
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("https://images.unsplash.com/photo-1513558161293-cdaf765ed2c5");
        background-size: cover;
        background-position: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #ff69b4; /* Cute pink color */
    }}
    .stApp {{
        background: rgba(255, 255, 255, 0.7); /* White transparent background for readability */
        padding: 10px;
        border-radius: 15px;
    }}
    .title {{
        font-size: 50px;
        text-align: center;
        font-weight: bold;
        color: #ff69b4;
        text-shadow: 2px 2px #ffb6c1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom cute style
st.markdown(f'<h1 class="title">🎂 Happy Birthday {birthday_person}! 🎉</h1>', unsafe_allow_html=True)

# Session state to track candles
if "candles" not in st.session_state:
    st.session_state.heart = [True] * 5  # 5 candles (True = lit, False = blown out)

# Display the cake with candles
st.write("Click on the hearts twice to get your present! ❤️")

# Create buttons for each candle
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        if st.session_state.candles[i]:
            if st.button(f"❤️", key=f"heart_{i}"):
                st.session_state.heart[i] = False  # Blow out the candle
        else:
            st.write("😘")  # Show extinguished candle

# Check if all candles are blown out
if all(not c for c in st.session_state.heart):
    st.success(f"🎉 Happy Birthdat Baby! Make a wish! 🎂")
    st.balloons()  # Fun animation
