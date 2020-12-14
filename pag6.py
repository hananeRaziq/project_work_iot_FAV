import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.image as mpimg


def main():
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")

    show_footer()

def show_footer():

    img = mpimg.imread('pag6_lavoro_team.png')
    st.image(img, caption='',use_column_width=True)

    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    
    img2 = mpimg.imread('pag6_docenti_team.png')
    st.image(img2, caption='',use_column_width=True)

    st.header("Vi ringraziamo per l'attenzione!")
    
    img3 = mpimg.imread('loghi_progetto.PNG')
    st.image(img3, caption='',use_column_width=True)
                     

if __name__ == "__main__":
    main()


