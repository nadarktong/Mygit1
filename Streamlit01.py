import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็บด้วย Phython")
st.image("pasulol.jpg")
st.header("การนำเสนอข้อมูลกราฟด้วย Phython")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7a/Iris_versicolor.jpg")
with col2:
    st.header("Verginica")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg")
with col3:
    st.header("Setora")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg")