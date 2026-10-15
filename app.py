import datetime
import random
import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Just For Mrigakshi 💖",
    page_icon="💖",
    layout="centered"
)

# App Title & Subtitle
st.title("The Official Vibe Check ✨")
st.subheader("Welcome, Mrigakshi!")
st.write("*A mini-app created specifically to brighten your day.*")

st.divider()

# Interactive Mood Section
vibe = st.selectbox(
    "How are you feeling right now?",
    [
        "Select your mood...",
        "Energetic & Unstoppable ⚡",
        "Cozy & Chill ☕",
        "Stressed / Need a break 🛑",
        "Ready for an adventure 🗺️",
    ],
)

if vibe != "Select your mood...":
    if st.button("Generate Your Vibe Report"):
        with st.spinner("Analyzing your aura... (totally scientific)"):
            time.sleep(1)

        st.balloons()

        # Customized responses
        if "Energetic" in vibe:
            st.success("🔥 **Vibe Report:** Main Character Energy! Time to conquer the day.")
        elif "Cozy" in vibe:
            st.info("☕ **Vibe Report:** Warm drink, comfy blanket, and pure relaxation mode.")
        elif "Stressed" in vibe:
            st.warning("💆 **Vibe Report:** Deep breath in... hold... exhale. Take it easy today!")
        else:
            st.success("🗺️ **Vibe Report:** Adventure mode activated! Spontaneous plans encouraged.")

# Personal Compliments Section
st.divider()
compliments = [
    "Fun fact: You have an incredible smile that lights up the room.",
    "Your energy and vibe are completely unmatched.",
    "You bring so much warmth and positivity wherever you go.",
    "Just a reminder: You're doing amazing, keep being awesome!",
]

st.markdown("### 💌 A Little Note For You:")
st.write(f"*{random.choice(compliments)}*")

# ---------------------------------------------------------
# 🎯 PLAYFUL DATE REQUEST SECTION
# ---------------------------------------------------------
st.divider()
st.subheader("Important Question Ahead... 👀")

# Initialize session state for playful answers
if "date_accepted" not in st.session_state:
    st.session_state.date_accepted = False

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

if not st.session_state.date_accepted:
    st.write("Now that your vibe check is complete, I have a mandatory follow-up question:")
    st.markdown("### **Would you like to go on a date with me? ☕✨**")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes! Absolutely 🥰", type="primary", use_container_width=True):
            st.session_state.date_accepted = True
            st.rerun()

    with col2:
        # Playful responses if she clicks No
        no_responses = [
            "Are you sure? Try clicking 'Yes' instead! 😉",
            "Error 404: 'No' button is currently malfunctioning! 🤖",
            "Nice try, but 'No' is temporarily out of service! 😜",
            "Okay, now you're just teasing! 'Yes' is right there 👉",
        ]
        
        if st.button("No 😜", use_container_width=True):
            st.session_state.no_count += 1
            idx = min(st.session_state.no_count - 1, len(no_responses) - 1)
            st.warning(no_responses[idx])

# If she clicks "Yes!"
if st.session_state.date_accepted:
    st.balloons()
    st.success("🎉 **BEST ANSWER EVER!** 🎉")
    st.markdown("### Let's plan our ideal date! 👇")

    # Interactive Date Customizer
    date_type = st.radio(
        "Pick your favorite vibe for the date:",
        [
            "Coffee & long cozy walk ☕🚶‍♀️",
            "Delicious food & dessert hunting 🍕🍰",
            "Sunset views & chill conversations 🌅✨",
            "Surprise me! 🎁",
        ],
    )

    preferred_day = st.selectbox(
        "Which day works best for you?",
        ["This Weekend", "Sometime next week", "Whenever you're free!"],
    )

    special_note = st.text_input("Any special request or favorite spot in mind? (Optional):")

    if st.button("Confirm Our Date Plan 💌"):
        st.snow()
        st.balloons()
        st.markdown("---")
        st.markdown("### 📝 **Date Summary Confirmed!**")
        st.write(f"• **Vibe:** {date_type}")
        st.write(f"• **When:** {preferred_day}")
        if special_note:
            st.write(f"• **Note:** {special_note}")
        
        st.success("Can't wait! Take a screenshot of this and send it to me on WhatsApp/Instagram! 📲❤️")

st.divider()
st.caption("*(P.S. Custom coded just for you! 😉)*")