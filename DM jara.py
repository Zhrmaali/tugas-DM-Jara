import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Aplikasi Analisis & Proyek Akhir")
st.write("Selamat datang di web app interaktif saya!")

# Membuat input sidebar (misalnya untuk parameter)
st.sidebar.header("Pengaturan Parameter")
nilai_input = st.sidebar.slider("Pilih nilai:", 0, 100, 50)

# Menampilkan output
st.write(f"Nilai yang Anda pilih di sidebar adalah: {nilai_input}")

# Contoh menampilkan tabel data
data = {"Kolom A": [1, 2, 3], "Kolom B": [4, 5, 6]}
df = pd.DataFrame(data)
st.dataframe(df)