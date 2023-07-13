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
img_portfolio = Image.open("/Users/victorgz/Documents/zarco_ideas/website/images/portfolio.png")

# HEADER SECTION #
with st.container():
    st.subheader("hi, I am victor")
    st.title("financial geek specializing in portfolio allocation and wealth management")
    st.write("I am passionate about finding ways to use next-gen tech to solve everyday problems.")
    st.write("[linkedin](https://www.linkedin.com/in/victor-gutierrez-z/)")

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
