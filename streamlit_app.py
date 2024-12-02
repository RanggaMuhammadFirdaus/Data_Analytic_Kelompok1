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

# Judul untuk Dataset
st.title("Dataset MAPB Historical Data")

# Membaca Data dari File CSV
data = pd.read_csv("MAPB Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Memastikan kolom 'Price' adalah string sebelum melakukan penggantian
data['Price'] = data['Price'].astype(str).str.replace(',', '').astype(float)
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
        f"**Harga Tertinggi:** {data['Price'].max()} pada {data['Date'][data['Price'].idxmax()].date()}\n\n"
        f"**Harga Terendah:** {data['Price'].min()} pada {data['Date'][data['Price'].idxmin()].date()}\n\n"
        f"**Perubahan Harga Rata-rata:** {data['Change %'].mean():.2f}%"
    )

# Judul untuk Dataset FAST Historical Data
st.title("Dataset FAST Historical Data")

# Membaca Data dari File CSV
data_fast = pd.read_csv("FAST Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Memastikan kolom 'Price' adalah string sebelum melakukan penggantian
data_fast['Price'] = data_fast['Price'].astype(str).str.replace(',', '').astype(float)
data_fast['Change %'] = data_fast['Change %'].str.replace('%', '').astype(float)

# Membuat Grafik Harga untuk FAST
fig, ax = plt.subplots()
ax.plot(data_fast['Date'], data_fast['Price'], marker='o', linestyle='-')
ax.set_title('Pergerakan Harga FAST dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga')
ax.grid()

# Menampilkan Grafik
st.pyplot(fig)

# Insight untuk FAST
with st.expander("Lihat Insight FAST"):
    st.write(
        f"**Harga Tertinggi FAST:** {data_fast['Price'].max()} pada {data_fast['Date'][data_fast['Price'].idxmax()].date()}\n\n"
        f"**Harga Terendah FAST:** {data_fast['Price'].min()} pada {data_fast['Date'][data_fast['Price'].idxmin()].date()}\n\n"
        f"**Perubahan Harga Rata-rata FAST:** {data_fast['Change %'].mean():.2f}%"
    )

# Judul untuk Dataset PZZA Historical Data
st.title("Dataset PZZA Historical Data")

# Membaca Data dari File CSV
data_pzza = pd.read_csv("PZZA Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Memastikan kolom 'Price' adalah string sebelum melakukan penggantian
data_pzza['Price'] = data_pzza['Price'].astype(str).str.replace(',', '').astype(float)
data_pzza['Change %'] = data_pzza['Change %'].str.replace('%', '').astype(float)

# Membuat Grafik Harga untuk PZZA
fig, ax = plt.subplots()
ax.plot(data_pzza['Date'], data_pzza['Price'], marker='o', linestyle='-')
ax.set_title('Pergerakan Harga PZZA dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga')
ax.grid()

# Menampilkan Grafik
st.pyplot(fig)

# Insight untuk PZZA
with st.expander("Lihat Insight PZZA"):
    st.write(
        f"**Harga Tertinggi PZZA:** {data_pzza['Price'].max()} pada {data_pzza['Date'][data_pzza['Price'].idxmax()].date()}\n\n"
        f"**Harga Terendah PZZA:** {data_pzza['Price'].min()} pada {data_pzza['Date'][data_pzza['Price'].idxmin()].date()}\n\n"
        f"**Perubahan Harga Rata-rata PZZA:** {data_pzza['Change %'].mean():.2f}%"
    )

# Judul untuk Dataset UNVR Historical Data
st.title("Dataset UNVR Historical Data")

# Membaca Data dari File CSV
data_unvr = pd.read_csv("UNVR Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Memastikan kolom 'Price' adalah string sebelum melakukan penggantian
data_unvr['Price'] = data_unvr['Price'].astype(str).str.replace(',', '').astype(float)
data_unvr['Change %'] = data_unvr['Change %'].str.replace('%', '').astype(float)

with st.expander("Lihat Insight"):
    st.write(
        f"**Harga Tertinggi:** {data['Price'].max()} pada {data['Date'][data['Price'].idxmax()].date()}\n\n"
        f"**Harga Terendah:** {data['Price'].min()} pada {data['Date'][data['Price'].idxmin()].date()}\n\n"
        f"**Perubahan Harga Rata-rata:** {data['Change %'].mean():.2f}%"
    )



# Menampilkan Grafik
st.pyplot(fig)
# Membaca Data dari File CSV
data_unvr = pd.read_csv("UNVR Historical Data.csv", parse_dates=["Date"], dayfirst=True)

# Memastikan kolom 'Price' adalah string sebelum melakukan penggantian
data_unvr['Price'] = data_unvr['Price'].astype(str).str.replace(',', '').astype(float)
data_unvr['Change %'] = data_unvr['Change %'].str.replace('%', '').astype(float)

# Menghitung rata-rata harga per bulan
data_unvr['Month'] = data_unvr['Date'].dt.to_period('M')
average_price_per_month = data_unvr.groupby('Month')['Price'].mean().reset_index()

# Membuat Bar Chart Horizontal
fig, ax = plt.subplots()
ax.barh(average_price_per_month['Month'].astype(str), average_price_per_month['Price'], color='skyblue')
ax.set_title('Rata-rata Harga UNVR per Bulan')
ax.set_xlabel('Harga Rata-rata')
ax.set_ylabel('Bulan')
ax.grid(axis='x')

# Menampilkan Grafik
st.pyplot(fig)

# Menambahkan Footer
st.markdown("---")
st.write("© 2024 Kelompok 1")
