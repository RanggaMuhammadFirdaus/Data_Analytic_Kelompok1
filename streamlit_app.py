import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
st.write("### Anggota Kelompok")
st.dataframe(df_anggota.drop(columns=["No"]), use_container_width=True)  # Menyembunyikan indeks

# Menambahkan Gambar atau Logo
st.image("Logo_Data_Analytics.png", caption="Kelompok Kami", use_container_width=True)

st.title("Dataset MAPB Historical Data")
# Membaca Data dari File CSV
data = pd.read_csv("MAPB Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Mengonversi kolom 'Price' dan 'Change %' ke tipe numerik
data['Price'] = data['Price'].str.replace(',', '').astype(float)
data['Change %'] = data['Change %'].str.replace('%', '').astype(float)

# Membuat Grafik Harga
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Price'], marker='o', linestyle='-')
ax.set_title('Pergerakan Harga dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga')
ax.grid()

# Menampilkan Grafik
st.pyplot(fig)

# Insight
with st.expander("Lihat Insight"):
    st.write(
        f"**Harga Tertinggi:** {data['Price'].max()} pada {data['Date'][data['Price'].idxmax()].date()}\n"
        f"**Harga Terendah:** {data['Price'].min()} pada {data['Date'][data['Price'].idxmin()].date()}\n"
        f"**Perubahan Harga Rata-rata:** {data['Change %'].mean():.2f}%"
    )

st.title("Dataset FAST Historical Data")
# Membaca Data dari File CSV
data = pd.read_csv("FAST Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Mengonversi kolom 'Price' dan 'Change %' ke tipe numerik
data['Price'] = data['Price'].str.replace(',', '').astype(float)
data['Change %'] = data['Change %'].str.replace('%', '').astype(float)

# Membuat Grafik Harga
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Price'], marker='o', linestyle='-')
ax.set_title('Pergerakan Harga dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga')
ax.grid()

# Menampilkan Grafik
st.pyplot(fig)

# Insight
with st.expander("Lihat Insight"):
    st.write(
        f"**Harga Tertinggi:** {data['Price'].max()} pada {data['Date'][data['Price'].idxmax()].date()}\n"
        f"**Harga Terendah:** {data['Price'].min()} pada {data['Date'][data['Price'].idxmin()].date()}\n"
        f"**Perubahan Harga Rata-rata:** {data['Change %'].mean():.2f}%"
    )


# Menambahkan Footer
st.markdown("---")
st.write("© 2024 Kelompok 1")
