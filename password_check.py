import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password strength tester by Wajid Ashfaq", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown("""     
<style>
.main {text-align: center;}
.stTextInput {width: 60% !important; margin: auto; }
.stButton button {
    width: 50%;
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
}
.stButton button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level.")

# Password input
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong")

# Function to check password strength
def check_password_strength(pwd):
    score = 0
    feedback = []

    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", pwd) and re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase (A-Z) and lowercase (a-z)** letters.")

    if re.search(r"\d", pwd):
        score += 1
    else:
        feedback.append("❌ Include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", pwd):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    return score, feedback

# Only call function and use `feedback` if button is clicked
if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Your password is **very strong**.")
        elif score == 3:
            st.info("🔐 Your password is **moderate**. Consider strengthening it.")
        else:
            st.error("❌ Your password is **weak**.")

        if feedback:
            with st.expander("💡 How to improve your password"):
                for item in feedback:
                    st.write(item)
    else:
        st.warning("⚠️ Please enter a password first.")
