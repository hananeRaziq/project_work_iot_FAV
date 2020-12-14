import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np

##aggiunti
from io import BytesIO
import base64
import markdown


def show_footer():
    st.markdown("***")
    st.markdown("**Like this tool?** Follow me on "
                "[Twitter](https://twitter.com/infomanager).")

def image_formatter(im):
    return f'<img src="data:image/jpeg;base64,{image_base64(im)}">'

def image_base64(im):
    if isinstance(im, str):
        im = get_thumbnail(im)
    with BytesIO() as buffer:
        im.save(buffer, 'jpeg')
        return base64.b64encode(buffer.getvalue()).decode()

def get_thumbnail(path):
    i = Image.open(path)
    i.thumbnail((300, 300), Image.LANCZOS)
    return i


def main():
    st.button("Re-run")
    # set up layout
    st.title("Dati raccolti")

    df  =  pd.read_csv("data.csv", names=["date","check","urls"])
    
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d-%H-%M-%S", errors='ignore')
    df = df.sort_values(by=['date'], ascending=False)    

    opts = ["mask","no-mask","all"]
    sel_opt = st.selectbox('Filtro mascherina',options=opts, index=1)
    dates_opts = df["date"].dt.date.unique()
    sel_date_opt = st.selectbox('Filtro data',options=dates_opts, index=0)
    
    
    if sel_opt== "no-mask":
        df_f = df[ (df["check"]=="no-mask") & (df["date"].dt.date==sel_date_opt) ]
        
        # st.dataframe(data = df_f)
        st.write(df_f.to_html(escape=False ,formatters=dict(urls=image_formatter)) , unsafe_allow_html=True)        
    elif sel_opt== "mask":
        df_f = df[ (df["check"]=="mask") & (df["date"].dt.date==sel_date_opt) ]
        st.write(df_f.to_html(escape=False ,formatters=dict(urls=image_formatter)) , unsafe_allow_html=True)        
    else:
        st.markdown(df.to_html(escape=False ,formatters=dict(urls=image_formatter)) , unsafe_allow_html=True)

    show_footer()

if __name__ == "__main__":
    main()


