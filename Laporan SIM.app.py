import streamlit as st
import pandas as pd

# Cek Plotly
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ModuleNotFoundError:
    PLOTLY_AVAILABLE = False

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="Laporan Kuisioner Sistem Absensi",
    page_icon="📊",
    layout="wide"
)

# ======================
# HEADER
# ======================
st.title("📊 Laporan Kuisioner Sistem Absensi Mahasiswa")

st.write("""
Survei persepsi mahasiswa terhadap kemudahan, kecepatan,
akurasi, dan efektivitas sistem absensi kampus.
""")

# ======================
# METRICS
# ======================
c1, c2, c3, c4 = st.columns(4)

c1.metric("Responden", "42")
c2.metric("Variabel", "5")
c3.metric("Fakultas", "3")
c4.metric("Rata-rata Skor", "3.46")

st.divider()

# ======================
# VARIABEL
# ======================
st.header("🧩 Variabel yang Diukur")

variabel = pd.DataFrame({
    "Kode": ["E", "F", "G", "H", "I"],
    "Variabel": [
        "Kemudahan Pemahaman",
        "Kecepatan Proses",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Akurasi Data"
    ],
    "Keterangan": [
        "Sistem mudah dipahami mahasiswa",
        "Kecepatan proses absensi",
        "Gangguan atau error sistem",
        "Kemudahan pencatatan kehadiran",
        "Ketepatan data kehadiran"
    ]
})

st.dataframe(variabel, use_container_width=True)

# ======================
# DEMOGRAFI
# ======================
st.header("👨‍🎓 Profil Responden")

if PLOTLY_AVAILABLE:

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = pd.DataFrame({
            "Kategori": ["Laki-laki", "Perempuan"],
            "Jumlah": [25, 17]
        })

        fig = px.pie(
            gender,
            names="Kategori",
            values="Jumlah",
            hole=0.5,
            title="Jenis Kelamin"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        usia = pd.DataFrame({
            "Kategori": ["18–25 Tahun", "26–35 Tahun"],
            "Jumlah": [29, 13]
        })

        fig = px.pie(
            usia,
            names="Kategori",
            values="Jumlah",
            hole=0.5,
            title="Kelompok Usia"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col3:
        fakultas = pd.DataFrame({
            "Fakultas": ["Teknik", "Ekonomi", "FIKES"],
            "Jumlah": [15, 15, 12]
        })

        fig = px.pie(
            fakultas,
            names="Fakultas",
            values="Jumlah",
            hole=0.5,
            title="Asal Fakultas"
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Plotly belum terinstall.")

# ======================
# LIKERT
# ======================
st.header("📋 Distribusi Jawaban Skala Likert")

likert = pd.DataFrame({
    "Pernyataan": [
        "E - Kemudahan Pemahaman",
        "F - Kecepatan Proses",
        "G - Kendala Sistem",
        "H - Kemudahan Pencatatan",
        "I - Akurasi Data"
    ],
    "STS": [2, 0, 0, 1, 1],
    "TS": [6, 5, 5, 5, 7],
    "N": [25, 17, 13, 13, 5],
    "S": [6, 15, 21, 18, 17],
    "SS": [3, 5, 3, 5, 12]
})

st.dataframe(likert, use_container_width=True)

# ======================
# RATA-RATA
# ======================
st.header("📈 Nilai Rata-rata Variabel")

avg_df = pd.DataFrame({
    "Variabel": [
        "Kemudahan Pemahaman",
        "Kecepatan Proses",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Akurasi Data"
    ],
    "Nilai": [3.05, 3.48, 3.52, 3.50, 3.76]
})

if PLOTLY_AVAILABLE:
    fig = px.bar(
        avg_df,
        x="Nilai",
        y="Variabel",
        orientation="h",
        text="Nilai",
        title="Rata-rata Skor Likert"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.dataframe(avg_df, use_container_width=True)

# ======================
# TEMUAN
# ======================
st.header("⭐ Temuan Utama")

c1, c2 = st.columns(2)

with c1:
    st.success("""
**Skor Tertinggi**

Akurasi Data = 3,76

Mahasiswa sangat mempercayai keakuratan data kehadiran.
""")

with c2:
    st.warning("""
**Skor Terendah**

Kemudahan Pemahaman = 3,05

Perlu peningkatan panduan penggunaan sistem.
""")

# ======================
# KESIMPULAN
# ======================
st.header("📝 Kesimpulan")

st.info("""
Berdasarkan hasil pengolahan data terhadap 42 responden,
sistem absensi kampus secara keseluruhan dinilai cukup baik.

Keunggulan utama terdapat pada aspek Akurasi Data (3,76).

Aspek yang perlu ditingkatkan adalah Kemudahan Pemahaman (3,05)
melalui sosialisasi dan panduan penggunaan sistem.
""")

st.divider()

st.caption("""
Disusun oleh:
Ega Irza'ul Fanani (142223067)

Program Studi Teknik Industri
Universitas Maarif Hasyim Latif
""")
