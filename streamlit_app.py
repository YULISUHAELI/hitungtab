import streamlit as st
import math
st.title("Menghitung volume tabung  :blue[cool] :sunglasses:")
r = st.number_input("Masukan jari-jari (cm):",0)
t = st.number_input("Masukan tinggi (cm):",0)

if st.button("hitung volume","type=primary"):
 vi=math.pi*(r**2)*t
 st.success(f"Vulume tabung adalah{vi.2f}")
