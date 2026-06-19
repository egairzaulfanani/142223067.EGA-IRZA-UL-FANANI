import streamlit as st
import pandas as pd

# Coba import Plotly
try:
    import plotly.express as px
    PLOTLY = True
except:
    PLOTLY = False

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Laporan Sistem Absensi",
    page_icon="📊",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#0d1b2a,#132032,#1a2f47);
}

.block-container {
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg,#0ea5a0,#1e3a5f);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.metric-card {
    background: #132032;
    border: 1px solid rgba(255,255,255,.1);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.metric-number {
    font-size: 36px;
    font-weight: bold;
    color: #5ecfcc;
}

.metric-title {
    color: #cbd5e1;
}

.footer {
    text-align:center;
    color:#94a3b8;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("📊 Dashboard")
    st.markdown("---")
    st.write("### Informasi")
    st.write("👨‍🎓 Responden : 42")
    st.write("📋 Variabel : 5")
    st.write("🏫 Fakultas : 3")

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
<h1>📊 Sistem Absensi Mahasiswa</h1>
<h3>Laporan Analisis Kuisioner</h3>
<p>Universitas Maarif Hasyim Latif</p>
</div>
""", unsafe_allow_html=True)

# =========================
# KPI
# =========================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">42</div>
    <div class="metric-title">RESPONDEN</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">5</div>
    <div class="metric-title">VARIABEL</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">3</div>
    <div class="metric-title">FAKULTAS</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">3.46</div>
    <div class="metric-title">RATA-RATA</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# VARIABEL
# =========================
st.header("🧩 Variabel yang Diukur")

variabel = pd.DataFrame({
    "Kode": ["E","F","G","H","I"],
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
        "Kemudahan pencatatan",
        "Ketepatan data kehadiran"
    ]
})

st.dataframe(variabel, use_container_width=True)

# =========================
# DEMOGRAFI
# =========================
st.header("👨‍🎓 Profil Responden")

if PLOTLY:

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
            hole=0.6,
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
            hole=0.6,
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
            hole=0.6,
            title="Asal Fakultas"
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Plotly belum terinstall.")

# =========================
# LIKERT
# =========================
st.header("📋 Distribusi Jawaban Likert")

likert = pd.DataFrame({
    "Pernyataan": [
        "Kemudahan Pemahaman",
        "Kecepatan Proses",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Akurasi Data"
    ],
    "STS": [2,0,0,1,1],
    "TS": [6,5,5,5,7],
    "N": [25,17,13,13,5],
    "S": [6,15,21,18,17],
    "SS": [3,5,3,5,12]
})

st.dataframe(likert, use_container_width=True)

# =========================
# RATA-RATA
# =========================
st.header("📈 Nilai Rata-rata Variabel")

nilai = {
    "Kemudahan Pemahaman": 3.05,
    "Kecepatan Proses": 3.48,
    "Kendala Sistem": 3.52,
    "Kemudahan Pencatatan": 3.50,
    "Akurasi Data": 3.76
}

for nama, skor in nilai.items():
    st.write(f"**{nama} ({skor})**")
    st.progress(skor / 5)

# =========================
# TEMUAN
# =========================
st.header("⭐ Temuan Utama")

k1, k2 = st.columns(2)

with k1:
    st.success("""
    Skor Tertinggi

    Akurasi Data : 3.76
    """)

with k2:
    st.warning("""
    Skor Terendah

    Kemudahan Pemahaman : 3.05
    """)

# =========================
# KESIMPULAN
# =========================
st.header("📝 Kesimpulan")

st.info("""
Sistem absensi kampus secara umum dinilai baik.

Keunggulan:
- Akurasi Data (3.76)
- Kendala Sistem (3.52)
- Kemudahan Pencatatan (3.50)

Perlu perbaikan:
- Kemudahan Pemahaman (3.05)
""")

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
<hr>
<b>Laporan Hasil Kuisioner Sistem Absensi Mahasiswa</b><br><br>
Ega Irza'ul Fanani (142223067)<br>
Program Studi Teknik Industri<br>
Universitas Maarif Hasyim Latif
</div>
""", unsafe_allow_html=True)
