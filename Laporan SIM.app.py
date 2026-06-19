ranking = pd.DataFrame({
    "Variabel":[
        "Akurasi Data",
        "Kendala Sistem",
        "Kemudahan Pencatatan",
        "Kecepatan Proses",
        "Kemudahan Pemahaman"
    ],
    "Nilai":[3.76,3.52,3.50,3.48,3.05]
})

fig = px.bar(
    ranking,
    x="Nilai",
    y="Variabel",
    orientation="h",
    text="Nilai"
)

st.plotly_chart(fig, use_container_width=True)
