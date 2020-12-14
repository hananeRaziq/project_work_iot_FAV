import streamlit as st
import markdown
import matplotlib.image as mpimg

def main():
    st.title("Ipotesi di Business plan")

    show_footer()

def show_footer():
   
    st.markdown(""" 
    ## Business model canvas
   
     """)
    img2=mpimg.imread('p5_bmc.png')
    st.image(img2, caption='',use_column_width=True)


if __name__ == "__main__":
    main()