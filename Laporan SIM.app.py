```python
import streamlit as st
import pandas as pd

try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except:
    PLOTLY_AVAILABLE = False

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Laporan Sistem Absensi",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        135deg,
        #0d1b2a 0%,
        #132032 50%,
        #1a2f47 100%
    );
}

.block-container{
    padding-top:2rem;
}

.hero{
    background: linear-gradient(
        135deg,
        #0ea5a0,
        #1a2f47
    );
    padding:40px;
    border-radius:25px;
    text-align:center;
    color:white;
    margin-bottom:25px;
    box-shadow:0 8px 25px rgba(0,0,0,.3);
}

.metric-card{
    background:#132032;
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,.1);
    margin-bottom:15px;
}

.metric-number{
    font-size:38px;
    font-weight:bold;
    color:#5ecfcc;
}

.metric-title{
    color:#cbd5e1;
    font-size:14px;
}

.highlight{
    background:linear-gradient(
        135deg,
        #0ea5a0,
        #1a2f47
    );
    padding:25px;
    border-radius:20px;
    color:white;
}

.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:
    st.title("📊 Dashboard")
    st.markdown("---")

    st.info("""
    **Laporan Kuisioner**
    
    Sistem Absensi Mahasiswa
    """)

    st.markdown("---")

    st.write("### Informasi")
    st.write("👨‍🎓 Responden : 42")
    st.write("📋 Variabel : 5")
    st.write("🏫 Fakultas : 3")

# =====================================
# HERO
# =====================================
st.markdown("""
<div class="hero">
    <h1>📊 Sistem Absensi Mahasiswa</h1>
    <h3>Laporan Analisis Kuisioner</h3>
    <p>
    Universitas Maarif Hasyim Latif
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================
# KPI
# =====================================
c1,c2,c3,c4 = st.columns(4)

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

# =====================================
# VARIABEL
# =====================================
st.header("🧩 Variabel yang Diukur")

variabel = pd.DataFrame({
    "Kode":["E","F","G","H","I"],
    "Variabel":[
        "Kemudahan Pemahaman",
        "Kecepatan Proses",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Akurasi Data"
    ],
    "Keterangan":[
        "Sistem mudah dipahami mahasiswa",
        "Kecepatan proses absensi",
        "Gangguan atau error sistem",
        "Kemudahan pencatatan",
        "Ketepatan data kehadiran"
    ]
})

st.dataframe(
    variabel,
    use_container_width=True,
    hide_index=True
)

# =====================================
# DEMOGRAFI
# =====================================
st.header("👨‍🎓 Profil Responden")

if PLOTLY_AVAILABLE:

    col1,col2,col3 = st.columns(3)

    with col1:

        gender = pd.DataFrame({
            "Kategori":["Laki-laki","Perempuan"],
            "Jumlah":[25,17]
        })

        fig = px.pie(
            gender,
            values="Jumlah",
            names="Kategori",
            hole=.65,
            title="Jenis Kelamin"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        usia = pd.DataFrame({
            "Kategori":["18-25 Tahun","26-35 Tahun"],
            "Jumlah":[29,13]
        })

        fig = px.pie(
            usia,
            values="Jumlah",
            names="Kategori",
            hole=.65,
            title="Kelompok Usia"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col3:

        fakultas = pd.DataFrame({
            "Fakultas":["Teknik","Ekonomi","FIKES"],
            "Jumlah":[15,15,12]
        })

        fig = px.pie(
            fakultas,
            values="Jumlah",
            names="Fakultas",
            hole=.65,
            title="Asal Fakultas"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =====================================
# LIKERT
# =====================================
st.header("📋 Distribusi Jawaban Likert")

likert = pd.DataFrame({
    "Pernyataan":[
        "Kemudahan Pemahaman",
        "Kecepatan Proses",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Akurasi Data"
    ],
    "STS":[2,0,0,1,1],
    "TS":[6,5,5,5,7],
    "N":[25,17,13,13,5],
    "S":[6,15,21,18,17],
    "SS":[3,5,3,5,12]
})

st.dataframe(
    likert,
    use_container_width=True,
    hide_index=True
)

# =====================================
# RATA-RATA
# =====================================
st.header("📈 Nilai Rata-rata Variabel")

nilai = {
    "Kemudahan Pemahaman":3.05,
    "Kecepatan Proses":3.48,
    "Kendala Sistem":3.52,
    "Kemudahan Pencatatan":3.50,
    "Akurasi Data":3.76
}

for nama,skor in nilai.items():
    st.write(f"**{nama} ({skor})**")
    st.progress(skor/5)

# =====================================
# HIGHLIGHT
# =====================================
st.header("⭐ Temuan Utama")

st.markdown("""
<div class="highlight">

<h2>🏆 Ringkasan Hasil</h2>

<h3>Skor Tertinggi</h3>
<p>
Akurasi Data memperoleh skor rata-rata
<b>3.76</b>.
</p>

<h3>Perlu Perbaikan</h3>
<p>
Kemudahan Pemahaman memperoleh skor
<b>3.05</b>.
</p>

<p>
Perlu peningkatan sosialisasi,
panduan penggunaan,
dan pelatihan singkat bagi mahasiswa.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================
# KESIMPULAN
# =====================================
st.header("📝 Kesimpulan")

st.success("""
Sistem absensi kampus secara umum dinilai baik.

Keunggulan utama terdapat pada aspek:

✅ Akurasi Data (3.76)

✅ Kendala Sistem (3.52)

✅ Kemudahan Pencatatan (3.50)

Aspek yang perlu ditingkatkan:

⚠️ Kemudahan Pemahaman (3.05)
""")

# =====================================
# FOOTER
# =====================================
st.markdown("""
<div class="footer">
<hr>

<b>Laporan Hasil Kuisioner Sistem Absensi Mahasiswa</b>

<br><br>

Disusun oleh:
<br>
Ega Irza'ul Fanani (142223067)

<br><br>

Program Studi Teknik Industri
<br>
Universitas Maarif Hasyim Latif

</div>
""", unsafe_allow_html=True)
```
