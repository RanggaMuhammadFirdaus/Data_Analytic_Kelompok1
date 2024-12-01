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

# Menambahkan Kolom Nomor Urut
for index, member in enumerate(anggota, start=1):
    member["No"] = index

# Mengubah Data Anggota menjadi DataFrame
df_anggota = pd.DataFrame(anggota)

# Menampilkan Data Anggota dalam Format Tabel tanpa Indeks
st.subheader("Daftar Anggota")
st.write("### Anggota Kelompok")
st.dataframe(df_anggota.drop(columns=["No"]), use_container_width=True)  # Menyembunyikan indeks

# Menambahkan Gambar atau Logo
st.image("Logo_Data_Analytics.png", caption="Kelompok Kami", use_container_width=True)

# Menambahkan Footer
st.markdown("---")
st.write("© 2024 Kelompok 1")
