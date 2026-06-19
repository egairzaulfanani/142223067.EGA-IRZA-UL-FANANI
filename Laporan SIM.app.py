import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Dashboard Sistem Absensi",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CSS MODERN
# =====================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background:linear-gradient(
135deg,
#07111f,
#0f172a,
#172554,
#0f172a
);
}

[data-testid="stSidebar"]{
background:#081220;
}

.hero{
padding:45px;
border-radius:25px;
background:linear-gradient(
135deg,
#06b6d4,
#2563eb
);
text-align:center;
color:white;
margin-bottom:25px;
box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.kpi{
background:rgba(255,255,255,.05);
padding:20px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,.1);
}

.kpi-number{
font-size:40px;
font-weight:bold;
color:#22d3ee;
}

.kpi-title{
color:white;
font-size:14px;
}

.footer{
text-align:center;
margin-top:40px;
color:#cbd5e1;
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
    Sistem Absensi Mahasiswa
    
    Universitas Maarif Hasyim Latif
    """)

    st.markdown("---")

    st.write("### Statistik")
    st.write("👨‍🎓 Responden : 42")
    st.write("📋 Variabel : 5")
    st.write("🏫 Fakultas : 3")

# =====================================
# HERO
# =====================================
st.markdown("""
<div class='hero'>
<h1>📊 Dashboard Analisis Sistem Absensi</h1>
<h3>Universitas Maarif Hasyim Latif</h3>
<p>Visualisasi Hasil Kuisioner Mahasiswa</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# KPI
# =====================================
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='kpi'>
        <div class='kpi-number'>42</div>
        <div class='kpi-title'>RESPONDEN</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='kpi'>
        <div class='kpi-number'>5</div>
        <div class='kpi-title'>VARIABEL</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='kpi'>
        <div class='kpi-number'>3</div>
        <div class='kpi-title'>FAKULTAS</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='kpi'>
        <div class='kpi-number'>3.46</div>
        <div class='kpi-title'>RATA-RATA</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =====================================
# DONUT CHART
# =====================================
st.header("👨‍🎓 Profil Responden")

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
        hole=0.65,
        title="Jenis Kelamin"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    usia = pd.DataFrame({
        "Kategori":["18-25 Tahun","26-35 Tahun"],
        "Jumlah":[29,13]
    })

    fig = px.pie(
        usia,
        values="Jumlah",
        names="Kategori",
        hole=0.65,
        title="Kelompok Usia"
    )

    st.plotly_chart(fig, use_container_width=True)

with col3:

    fakultas = pd.DataFrame({
        "Kategori":["Teknik","Ekonomi","FIKES"],
        "Jumlah":[15,15,12]
    })

    fig = px.pie(
        fakultas,
        values="Jumlah",
        names="Kategori",
        hole=0.65,
        title="Asal Fakultas"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================
# GAUGE
# =====================================
st.header("🎯 Tingkat Kepuasan Sistem")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=3.46,
    title={"text":"Rata-rata Kepuasan"},
    gauge={
        "axis":{"range":[0,5]},
        "bar":{"color":"cyan"},
        "steps":[
            {"range":[0,2],"color":"#7f1d1d"},
            {"range":[2,4],"color":"#854d0e"},
            {"range":[4,5],"color":"#14532d"}
        ]
    }
))

st.plotly_chart(fig, use_container_width=True)

# =====================================
# RADAR CHART
# =====================================
st.header("🕸 Analisis Variabel")

kategori = [
    "Pemahaman",
    "Kecepatan",
    "Kendala",
    "Pencatatan",
    "Akurasi"
]

nilai = [
    3.05,
    3.48,
    3.52,
    3.50,
    3.76
]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=nilai,
    theta=kategori,
    fill='toself',
    name='Skor'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,5]
        )
    )
)

st.plotly_chart(fig, use_container_width=True)

# =====================================
# PROGRESS
# =====================================
st.header("📈 Nilai Rata-rata Variabel")

data = {
    "Kemudahan Pemahaman":3.05,
    "Kecepatan Proses":3.48,
    "Kendala Sistem":3.52,
    "Kemudahan Pencatatan":3.50,
    "Akurasi Data":3.76
}

for nama, skor in data.items():
    st.write(f"**{nama} ({skor})**")
    st.progress(skor/5)

# =====================================
# RANKING
# =====================================
st.header("🏆 Ranking Variabel")

ranking = pd.DataFrame({
    "Variabel":[
        "Akurasi Data",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Kecepatan Proses",
        "Kemudahan Pemahaman"
    ],
    "Nilai":[
        3.76,
        3.52,
        3.50,
        3.48,
        3.05
    ]
})

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

# =====================================
# INSIGHT
# =====================================
top = ranking.iloc[0]
bottom = ranking.iloc[-1]

c1,c2 = st.columns(2)

with c1:
    st.success(
        f"""
🏆 Variabel Terbaik

{top['Variabel']}

Nilai : {top['Nilai']}
"""
    )

with c2:
    st.warning(
        f"""
⚠️ Perlu Ditingkatkan

{bottom['Variabel']}

Nilai : {bottom['Nilai']}
"""
    )

# =====================================
# KESIMPULAN
# =====================================
st.header("📝 Kesimpulan")

st.info("""
Sistem absensi mahasiswa secara umum dinilai baik.

Keunggulan utama terdapat pada aspek Akurasi Data.

Aspek yang perlu ditingkatkan adalah Kemudahan Pemahaman
melalui sosialisasi dan panduan penggunaan sistem.
""")

# =====================================
# FOOTER
# =====================================
st.markdown("""
<div class='footer'>
<hr>
<b>Laporan Kuisioner Sistem Absensi Mahasiswa</b><br><br>
Ega Irza'ul Fanani (142223067)<br>
Program Studi Teknik Industri<br>
Universitas Maarif Hasyim Latif
</div>
""", unsafe_allow_html=True)
