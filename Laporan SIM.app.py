import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="Laporan Kuisioner Sistem Absensi",
    page_icon="📊",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
.main {
    background-color: #0d1b2a;
}

.metric-card {
    background: #132032;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
}

.big-number {
    font-size: 40px;
    font-weight: bold;
    color: #5ecfcc;
}

.section-title {
    font-size: 32px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
}

.highlight {
    padding: 25px;
    border-radius: 15px;
    background: #132032;
    border-left: 5px solid #0ea5a0;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<div style='text-align:center;padding:20px'>
<h1>📊 Laporan Kuisioner Sistem Absensi Mahasiswa</h1>
<p>
Survei persepsi mahasiswa terhadap kemudahan, kecepatan,
akurasi, dan efektivitas sistem absensi kampus
</p>
</div>
""", unsafe_allow_html=True)

# ======================
# METRIC
# ======================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Responden", "42")

with col2:
    st.metric("Variabel", "5")

with col3:
    st.metric("Fakultas", "3")

with col4:
    st.metric("Rata-rata Skor", "3.46")

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

st.dataframe(
    variabel,
    use_container_width=True,
    hide_index=True
)

# ======================
# DEMOGRAFI
# ======================
st.header("👨‍🎓 Profil Responden")

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
        hole=0.55,
        title="Jenis Kelamin"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    usia = pd.DataFrame({
        "Kategori": ["18-25 Tahun", "26-35 Tahun"],
        "Jumlah": [29, 13]
    })

    fig = px.pie(
        usia,
        names="Kategori",
        values="Jumlah",
        hole=0.55,
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
        hole=0.55,
        title="Asal Fakultas"
    )

    st.plotly_chart(fig, use_container_width=True)

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

st.dataframe(
    likert,
    use_container_width=True,
    hide_index=True
)

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

fig = px.bar(
    avg_df,
    x="Nilai",
    y="Variabel",
    orientation="h",
    text="Nilai",
    title="Rata-rata Skor Likert"
)

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

# ======================
# HIGHLIGHT
# ======================
st.header("⭐ Temuan Utama")

c1, c2 = st.columns(2)

with c1:
    st.success("""
### Skor Tertinggi

**Akurasi Data**

Nilai rata-rata: **3,76**

Mahasiswa sangat mempercayai keakuratan data kehadiran yang ditampilkan sistem.
""")

with c2:
    st.warning("""
### Skor Terendah

**Kemudahan Pemahaman**

Nilai rata-rata: **3,05**

Perlu peningkatan panduan penggunaan dan sosialisasi sistem.
""")

# ======================
# KESIMPULAN
# ======================
st.header("📝 Kesimpulan")

st.markdown("""
<div class='highlight'>

Berdasarkan hasil pengolahan data kuesioner terhadap **42 responden**,
sistem absensi kampus secara keseluruhan dinilai **cukup baik**.

### Keunggulan
✅ Akurasi Data = **3,76**

✅ Kendala Sistem = **3,52**

✅ Kemudahan Pencatatan = **3,50**

### Perlu Perbaikan
⚠️ Kemudahan Pemahaman = **3,05**

Disarankan menyediakan panduan penggunaan,
pelatihan singkat, dan sosialisasi sistem kepada mahasiswa.

</div>
""", unsafe_allow_html=True)

st.divider()

st.caption("""
Laporan Hasil Kuisioner Sistem Absensi Mahasiswa

Disusun oleh:
Ega Irza'ul Fanani (142223067)

Program Studi Teknik Industri
Universitas Maarif Hasyim Latif
""")
