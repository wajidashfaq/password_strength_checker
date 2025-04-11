import re

import streamlit as st

#page styling

st.set_page_config(page_title="Password strength tester by Wajid Ashfaq", page_icon="🔑", layout="centered")
#cutom css
st.markdown("""     
<style>
.main {text-align: center;}
.stTextInput {width: 60% !important; margin: auto; }
.stButton button {width: 50%; background-color 4CAF50; color: white; font-size: 18px; }
.stButton button:hover {background-color: #45a049; }
</style>""", unsafe_allow_html=True)

#page title and description
st.title("🔒 Password Strength Generator")
st.write("Enter your password below for checking security level.")
password = st.text_input("Enter your password")
#fucntion to check password strength 
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1 #increased score by 1

    else: 
        feedback.append("❌ Password should be **atleast 8 characters long**.")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1

        else:
            feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")    

if re.search(r"\d", password):
    score += 1 # type: ignore

else:
    feedback.append("❌ Password should include **at least one number (0-9) **.")  # type: ignore

#special characters
if re.search(r"[!@#$%^&*]", password):
    score += 1

else:
    feedback.append("❌ Include **at least one special character(!@#$%^&*) **.") # type: ignore
    
#displaying password strength results
if score == 4:
    st.success("✅ Your password is **very strong**.")
elif score == 3:
    st.info("**Moderate Password** - Consider improving security by adding more feature")
else:
    st.error    ("❌ Your password is **weak**.")
    
if feedback: # type: ignore
    with st.expander("**improve your password**"):
        for item in feedback: # type: ignore
            st.write(item)                
    
    password = st.text_input("Enter your password", type="password", help="Ensure your password is strong")
    if st.button("Check Password Strength"):
       if password:
        check_password_strength(password)
        
else:        
    st.warning("Please Enter a password first!")
