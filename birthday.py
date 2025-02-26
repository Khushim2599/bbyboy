import streamlit as st

# Hardcoded name
birthday_person = "Dhruv"  # Change this to any name you want

st.title(f"🎂 Happy Birthday {birthday_person}! 🎉")

# Session state to track candles
if "candles" not in st.session_state:
    st.session_state.candles = [True] * 5  # 5 candles (True = lit, False = blown out)

# Display the cake with candles
st.write("Click on the heart to get your present! ❤️")

# Create buttons for each candle
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        if st.session_state.candles[i]:
            if st.button(f"❤️", key=f"candle_{i}"):
                st.session_state.candles[i] = False  # Blow out the candle
        else:
            st.write("😘")  # Show extinguished candle

# Check if all candles are blown out
if all(not c for c in st.session_state.candles):
    st.success(f"🎉 Happy Birthday Baby! Make a wish! 🎂")
    st.balloons()  # Fun animation
