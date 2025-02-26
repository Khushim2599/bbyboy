import streamlit as st
import base64
from PIL import Image

# Hardcoded name
birthday_person = "Dhuv"  # Change this to the name you want

# Function to convert local image to Base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your local image (Make sure it's correct!)
image_path = "C:/Users/khushi/Desktop/Extras/background.jpg"  # Replace with actual path

# Convert image to Base64
base64_image = get_base64_of_image(image_path)

# Apply CSS with Base64-encoded image & custom fonts
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500&display=swap');

    body {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        font-family: 'Baloo 2', cursive;
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
