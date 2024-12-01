import streamlit as st
import pandas as pd

# Judul Dashboard
st.title("Dashboard Anggota Kelompok")

# Data Anggota
anggota = [
    {"Nama": "Rangga Muhammad Firdaus", "NIM": "210414002"},
    {"Nama": "Malva Alfaza", "NIM": "220434003"},
    {"Nama": "Farid Nur Arif", "NIM": "210414003"},
    {"Nama": "Ega Rahma Arnita", "NIM": "210414029"},
    {"Nama": "Risky Fadillah", "NIM": "210414016"},
]

# Mengubah Data Anggota menjadi DataFrame
df_anggota = pd.DataFrame(anggota)

# Menampilkan Data Anggota dalam Format Tabel tanpa Indeks
st.write("### Anggota Kelompok")
st.table(df_anggota)  # Menggunakan st.table() untuk menyembunyikan indeks

# Menambahkan Gambar atau Logo
st.image("Logo_Data_Analytics.png", caption="Kelompok Kami", use_container_width=True)

# Menambahkan Footer
st.markdown("---")
st.write("© 2024 Kelompok 1")
