import streamlit as st

st.title("Menghitung volume tabung  :blue[cool] :sunglasses:")
r = st.number_input("Masukan jari-jari (cm):",0)
t = st.number_input("Masukan tinggi (cm):",0)

if st.bottom("hitung volum",type=primary"):
 v=math.pi*(r**2)*t
st.success(f"Vulume tabung adalah{vi.2f}")
