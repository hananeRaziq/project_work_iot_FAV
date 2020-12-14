import streamlit as st
import markdown
import matplotlib.image as mpimg

def main():
    st.title("Implementazione su Raspberry")

    show_footer()

def show_footer():
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")

    img=mpimg.imread('pag5_part1.png')
    st.image(img, caption='',use_column_width=True)

    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    st.markdown("\r\n")
    
    img2=mpimg.imread('pag5_part2.png')
    st.image(img2, caption='',use_column_width=True)



if __name__ == "__main__":
    main()