from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="zarco ideas", page_icon=":light_bulb:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://lottie.host/e576f751-d277-4b85-b1cf-9bfff91b6f64/dplNN1iGJD.json")
img_portfolio = Image.open("images/portfolio.png")

# HEADER SECTION #
with st.container():
    st.markdown("""
        <style>
        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<div class='center'>", unsafe_allow_html=True)
    st.subheader("hi, I am victor")
    st.title("financial geek specializing in portfolio allocation and wealth management")
    st.write("I am passionate about finding ways to use next-gen tech to solve everyday problems.")
    st.write("[linkedin](https://www.linkedin.com/in/victor-gutierrez-z/)")
    st.markdown("</div>", unsafe_allow_html=True)

# WHAT I DO #
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("purpose of this page")
        st.write("##")
        st.write(
            """
            in this website I document some solutions to common problems i find interesting, along with other resources
            
            DISCLAIMERS:
            - all of these resources are entirely curiosity driven.
            - non of these are financial, tax, law, or life advise.
            - you should definitely not use any of these for business purposes.
            
            if this sounds interesting to you, message me on twitter:
            
            """
        )
        st.write("[@vicgzarco](https://twitter.com/vicgzarco)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---PROJECTS--- #
with st.container():
    st.write("---")
    st.header(":wrench:&nbsp;&nbsp;&nbsp;tool box")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_portfolio)
    with text_column:
        st.subheader("how much active risk is enough?")
        st.write(
            """
            user-friendly solution to a common investor's problem - choosing an optimal allocation between: \n
            1) market index \n 
            2) factors \n 
            3) active funds \n \n
            
            credits to: \n
            Andrew Ang, Linxi Chen, Michael Gates & Paul D. Henderson (2021) Index + Factors + Alpha, 
            Financial Analysts Journal, 77:4, 45-64, DOI: """
        )
        st.markdown("[10.1080/0015198X.2021.1960782](https://www.tandfonline.com/doi/full/10.1080/0015198X.2021.1960782)")

        st.markdown("[zarco ideas...](https://www.zarcoideas.com/)")

# ---CONTACT---
with st.container():
    st.write("---")
    st.header(":incoming_envelope:&nbsp;&nbsp;&nbsp;shoot me an e-mail:")
    st.write("##")
    contact_form =  """
    <form action="https://formsubmit.co/vgutierrezzarco@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your e-mail" required>
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
