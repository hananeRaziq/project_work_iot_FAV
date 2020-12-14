import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.image as mpimg


def main():
    img=mpimg.imread('lowrisk_logo.png')
    st.image(img, caption='',use_column_width=True)

    st.title("Introduzione")

    show_footer()

def show_footer():
 
    img1=mpimg.imread('pag1_infografica.png')
    st.image(img1, caption='',use_column_width=True)
            

if __name__ == "__main__":
    main()


