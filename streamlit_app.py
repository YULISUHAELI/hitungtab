import streamlit as st
import math, time
st.title("Menghitung volume tabung  :blue[cool] :sunglasses:")
r = st.number_input("Masukan jari-jari (cm):",0)
t = st.number_input("Masukan tinggi (cm):",0)

if st.button("hitung volume","type=primary"):
 loading=st.progress(0)
 for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
 vi=math.pi*(r**2)*t
 st.success(f"jadi Vulume tabung tersebut adalah :{vi:.2f}")
