import streamlit as st

# Hardcoded name
birthday_person = "Dhuv"  # Change this to the name you want

# Background image URL (replace this with your uploaded image link)
background_image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fpink-heart-cas-background--511369732702023413%2F&psig=AOvVaw2Vm7vnDszQPlrlSujkLbhr&ust=1740683434176000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKCB6p-F4osDFQAAAAAdAAAAABAI"  # CHANGE THIS!

# Apply CSS with Online Background Image & Bubble Font
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500&display=swap');

    body {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        font-family: 'Baloo 2', cursive;
        color: #ff69b4; /* Cute pink color */
    }}
    .stApp {{
        background_image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fpink-heart-cas-background--511369732702023413%2F&psig=AOvVaw2Vm7vnDszQPlrlSujkLbhr&ust=1740683434176000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKCB6p-F4osDFQAAAAAdAAAAABAI"  # CHANGE THIS!

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
    .instructions {{
        font-size: 20px;
        font-weight: bold;
        color: black;
        text-align: center;
        margin-top: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom bubble-style font
st.markdown(f'<h1 class="title">🎂 Happy Birthday {birthday_person}! 🎉</h1>', unsafe_allow_html=True)

# Instruction text in black
st.markdown('<p class="instructions">Click on the hearts twice to get your present! ❤️</p>', unsafe_allow_html=True)

# Session state to track hearts
if "hearts" not in st.session_state:
    st.session_state.hearts = [0] * 5  # 0 means not clicked, 1 means clicked once, 2 means present unlocked

# Create columns for heart buttons
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        if st.session_state.hearts[i] == 0:  # First click
            if st.button(f"❤️", key=f"heart_{i}"):
                st.session_state.hearts[i] = 1  # First click registers
        elif st.session_state.hearts[i] == 1:  # Second click
            if st.button(f"💖", key=f"heart_clicked_{i}"):  # Change button appearance
                st.session_state.hearts[i] = 2  # Unlock present
        else:
            st.write("🎁")  # Show present after second click

# Check if all hearts are unlocked
if all(h == 2 for h in st.session_state.hearts):
    st.success(f"🎉 Happy Birthday Baby! Make a wish! 🎂")
    st.balloons()  # Fun animation
