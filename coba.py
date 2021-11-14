import streamlit as st

st.title("Menghitung Volume Bola")
r = st.number_input("Jari-jari")

phi=22/7
volume=4/3*(phi*r*r*r)

if st.button("Hasil"):
   st.success('Volume Bola adalah {} cm3'.format(volume))