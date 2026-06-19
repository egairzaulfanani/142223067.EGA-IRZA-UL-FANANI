<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Laporan Kuisioner Sistem Absensi Mahasiswa</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --navy: #0d1b2a;
      --navy-mid: #1a2f47;
      --teal: #0ea5a0;
      --teal-light: #5ecfcc;
      --gold: #f0a500;
      --white: #f8fafc;
      --soft: #e2e8f0;
      --muted: #94a3b8;
      --card-bg: #132032;
      --accent-red: #e05252;
      --accent-green: #3ecf8e;
    }


*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--navy);
  color: var(--white);
  font-family: 'Plus Jakarta Sans', sans-serif;
  overflow-x: hidden;
}

/* ── NOISE OVERLAY ── */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: .5;
}

/* ── HERO ── */
header {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 24px 60px;
  overflow: hidden;
}

header::after {
  content: '';
  position: absolute;
  width: 700px; height: 700px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(14,165,160,.22) 0%, transparent 70%);
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

.badge {
  display: inline-block;
  border: 1px solid var(--teal);
  color: var(--teal-light);
  font-size: .7rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  padding: 6px 16px;
  border-radius: 999px;
  margin-bottom: 28px;
  backdrop-filter: blur(4px);
  animation: fadeUp .8s ease both;
}

h1 {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(2.4rem, 6vw, 4.5rem);
  line-height: 1.1;
  max-width: 780px;
  animation: fadeUp .9s .1s ease both;
}
h1 span { color: var(--teal); font-style: italic; }

.hero-sub {
  color: var(--muted);
  font-size: .95rem;
  margin-top: 18px;
  max-width: 520px;
  line-height: 1.7;
  animation: fadeUp 1s .2s ease both;
}

.hero-meta {
  display: flex; gap: 32px; margin-top: 48px;
  animation: fadeUp 1s .35s ease both;
  flex-wrap: wrap; justify-content: center;
}
.hero-meta-item { text-align: center; }
.hero-meta-item .num {
  font-family: 'DM Serif Display', serif;
  font-size: 2.8rem;
  color: var(--teal-light);
  line-height: 1;
}
.hero-meta-item .lbl { font-size: .72rem; color: var(--muted); text-transform: uppercase; letter-spacing: .1em; margin-top: 4px; }

.divider { width: 48px; height: 2px; background: var(--teal); margin: 48px auto 0; opacity: .5; }

/* ── SCROLL ARROW ── */
.scroll-hint {
  position: absolute;
  bottom: 36px; left: 50%;
  transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  color: var(--muted); font-size: .7rem; letter-spacing: .1em;
  text-transform: uppercase;
  animation: fadeUp 1s .6s ease both;
}
.scroll-hint svg { animation: bob 1.8s ease-in-out infinite; }
@keyframes bob { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }

/* ── SECTION WRAPPER ── */
main { position: relative; z-index: 1; }
section { padding: 100px 24px; max-width: 1100px; margin: 0 auto; }

.section-label {
  font-size: .68rem; letter-spacing: .18em; text-transform: uppercase;
  color: var(--teal); font-weight: 600; margin-bottom: 12px;
}
.section-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  line-height: 1.2;
  margin-bottom: 48px;
}

/* ── GRID CARDS ── */
.cards { display: grid; gap: 20px; }
.cards-2 { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.cards-3 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }

.card {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 16px;
  padding: 28px 24px;
  position: relative;
  overflow: hidden;
  transition: transform .3s, border-color .3s;
}
.card:hover { transform: translateY(-4px); border-color: var(--teal); }
.card::before {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(14,165,160,.06) 0%, transparent 60%);
  pointer-events: none;
}

.card-icon {
  width: 42px; height: 42px; border-radius: 10px;
  background: rgba(14,165,160,.15);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem; margin-bottom: 16px;
}
.card h3 { font-size: 1rem; font-weight: 600; margin-bottom: 6px; }
.card p { color: var(--muted); font-size: .85rem; line-height: 1.6; }

/* ── BIG STAT CARD ── */
.stat-card {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px;
  padding: 32px;
  display: flex; align-items: center; gap: 24px;
  transition: transform .3s, border-color .3s;
}
.stat-card:hover { transform: translateY(-4px); border-color: var(--gold); }
.stat-num {
  font-family: 'DM Serif Display', serif;
  font-size: 3.2rem;
  line-height: 1;
  color: var(--gold);
  white-space: nowrap;
}
.stat-info h4 { font-size: 1rem; font-weight: 600; margin-bottom: 4px; }
.stat-info p { font-size: .82rem; color: var(--muted); line-height: 1.5; }

/* ── PIE CHART (CSS) ── */
.pie-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
}
.pie-wrap {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px;
  padding: 32px 28px;
  display: flex; flex-direction: column; align-items: center;
  gap: 24px;
  transition: transform .3s;
}
.pie-wrap:hover { transform: translateY(-4px); }
.pie-wrap h3 { font-size: 1rem; font-weight: 600; text-align: center; }

.donut {
  position: relative;
  width: 160px; height: 160px;
}
.donut svg { width: 100%; height: 100%; transform: rotate(-90deg); }
.donut-label {
  position: absolute; inset: 0;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
}
.donut-label .pct {
  font-family: 'DM Serif Display', serif;
  font-size: 1.9rem;
  line-height: 1;
}
.donut-label .sub { font-size: .65rem; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }

.legend { display: flex; flex-direction: column; gap: 10px; width: 100%; }
.legend-item { display: flex; align-items: center; gap: 10px; font-size: .82rem; }
.legend-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.legend-label { color: var(--soft); flex: 1; }
.legend-pct { color: var(--muted); font-weight: 600; }

/* ── BAR CHART ── */
.bar-section { background: var(--card-bg); border: 1px solid rgba(255,255,255,.07); border-radius: 20px; padding: 36px 32px; }
.bar-section h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; }
.bar-section .desc { color: var(--muted); font-size: .83rem; margin-bottom: 32px; line-height: 1.6; }

.bar-group { margin-bottom: 20px; }
.bar-head { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: .82rem; }
.bar-head .col-name { color: var(--soft); font-weight: 600; }
.bar-head .col-val { color: var(--teal-light); font-weight: 700; }
.bar-track { background: rgba(255,255,255,.07); border-radius: 999px; height: 10px; overflow: hidden; }
.bar-fill {
  height: 100%; border-radius: 999px;
  background: linear-gradient(90deg, var(--teal), var(--teal-light));
  transform-origin: left;
  animation: growBar 1s ease both;
}
@keyframes growBar { from { transform: scaleX(0); } to { transform: scaleX(1); } }
.bar-tag { font-size: .72rem; margin-top: 5px; }
.tag-netral { color: var(--muted); }
.tag-setuju { color: var(--teal-light); }

/* ── LIKERT TABLE ── */
.likert-grid {
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px;
  overflow: hidden;
}
.likert-header {
  display: grid;
  grid-template-columns: 2fr repeat(5, 1fr);
  background: rgba(14,165,160,.12);
  padding: 14px 24px;
  font-size: .72rem; text-transform: uppercase; letter-spacing: .1em;
  color: var(--teal-light); font-weight: 700;
  gap: 8px;
}
.likert-row {
  display: grid;
  grid-template-columns: 2fr repeat(5, 1fr);
  padding: 16px 24px;
  border-top: 1px solid rgba(255,255,255,.05);
  gap: 8px;
  font-size: .85rem;
  align-items: center;
  transition: background .2s;
}
.likert-row:hover { background: rgba(255,255,255,.03); }
.likert-row .col-q { color: var(--soft); font-weight: 500; }
.likert-row .col-n { color: var(--muted); text-align: center; }
.likert-row .col-avg {
  text-align: center;
  font-family: 'DM Serif Display', serif;
  font-size: 1.1rem;
  color: var(--gold);
}

/* ── CONCLUSION ── */
.conclusion {
  background: linear-gradient(135deg, rgba(14,165,160,.15), rgba(240,165,0,.08));
  border: 1px solid rgba(14,165,160,.3);
  border-radius: 24px;
  padding: 48px 40px;
  position: relative;
  overflow: hidden;
}
.conclusion::before {
  content: '"';
  position: absolute; top: -20px; left: 24px;
  font-family: 'DM Serif Display', serif;
  font-size: 14rem;
  color: rgba(14,165,160,.1);
  line-height: 1;
  pointer-events: none;
}
.conclusion p { font-size: .95rem; line-height: 1.8; color: var(--soft); max-width: 720px; }
.conclusion p + p { margin-top: 16px; }

/* ── FOOTER ── */
footer {
  border-top: 1px solid rgba(255,255,255,.07);
  text-align: center;
  padding: 40px 24px;
  color: var(--muted);
  font-size: .8rem;
  line-height: 1.7;
}

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
.reveal {
  opacity: 0; transform: translateY(32px);
  transition: opacity .7s ease, transform .7s ease;
}
.reveal.visible { opacity: 1; transform: none; }

/* ── RESPONSIVE ── */
@media (max-width: 600px) {
  .likert-header, .likert-row { grid-template-columns: 1.5fr repeat(5, 1fr); font-size: .72rem; padding: 12px 14px; }
  .stat-card { flex-direction: column; text-align: center; }
}


  </style>
</head>
<body>

<!-- ═══════════════ HERO ═══════════════ -->

<header>
  <div class="badge">Laporan Statistik Deskriptif · 2026</div>
  <h1>Kuisioner <span>Sistem Absensi</span> Mahasiswa</h1>
  <p class="hero-sub">
    Survei persepsi mahasiswa terhadap kemudahan, kecepatan, akurasi, dan efektivitas
    sistem absensi kampus — Universitas Maarif Hasyim Latif.
  </p>
  <div class="hero-meta">
    <div class="hero-meta-item">
      <div class="num">42</div>
      <div class="lbl">Responden</div>
    </div>
    <div class="hero-meta-item">
      <div class="num">5</div>
      <div class="lbl">Variabel</div>
    </div>
    <div class="hero-meta-item">
      <div class="num">3</div>
      <div class="lbl">Fakultas</div>
    </div>
    <div class="hero-meta-item">
      <div class="num">3,46</div>
      <div class="lbl">Rata-rata Skor</div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="scroll-hint">
    <span>Scroll</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M12 5v14M5 12l7 7 7-7"/>
    </svg>
  </div>
</header>

<main>

  <!-- ═══════════════ METODOLOGI ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Metodologi</div>
    <div class="section-title">Variabel yang Diukur</div>
    <div class="cards cards-2">
      <div class="card">
        <div class="card-icon">🧩</div>
        <h3>Kolom E — Kemudahan Pemahaman</h3>
        <p>Apakah sistem absensi mudah dipahami oleh mahasiswa.</p>
      </div>
      <div class="card">
        <div class="card-icon">⚡</div>
        <h3>Kolom F — Kecepatan Proses</h3>
        <p>Seberapa cepat proses absensi dapat diselesaikan.</p>
      </div>
      <div class="card">
        <div class="card-icon">🔧</div>
        <h3>Kolom G — Kendala Sistem</h3>
        <p>Tingkat gangguan atau error yang dialami pada sistem.</p>
      </div>
      <div class="card">
        <div class="card-icon">📋</div>
        <h3>Kolom H — Kemudahan Pencatatan</h3>
        <p>Apakah sistem memudahkan pencatatan kehadiran mahasiswa.</p>
      </div>
      <div class="card">
        <div class="card-icon">✅</div>
        <h3>Kolom I — Akurasi Data</h3>
        <p>Ketepatan dan keakuratan informasi kehadiran yang ditampilkan.</p>
      </div>
    </div>
  </section>

  <!-- ═══════════════ DEMOGRAFI ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Karakteristik Responden</div>
    <div class="section-title">Profil 42 Mahasiswa</div>


<div class="pie-row">

  <!-- Jenis Kelamin -->
  <div class="pie-wrap">
    <h3>Jenis Kelamin</h3>
    <div class="donut">
      <svg viewBox="0 0 36 36">
        <!-- background ring -->
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="3.5"/>
        <!-- Laki-laki 60% = 60/100 * 100 = 60 dasharray -->
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#0ea5a0" stroke-width="3.5"
          stroke-dasharray="60 40" stroke-linecap="round"/>
        <!-- Perempuan 40% -->
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#f0a500" stroke-width="3.5"
          stroke-dasharray="40 60" stroke-dashoffset="-60" stroke-linecap="round"/>
      </svg>
      <div class="donut-label">
        <span class="pct" style="color:var(--teal)">42</span>
        <span class="sub">orang</span>
      </div>
    </div>
    <div class="legend">
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--teal)"></div>
        <span class="legend-label">Laki-laki</span>
        <span class="legend-pct">25 (60%)</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--gold)"></div>
        <span class="legend-label">Perempuan</span>
        <span class="legend-pct">17 (40%)</span>
      </div>
    </div>
  </div>

  <!-- Usia -->
  <div class="pie-wrap">
    <h3>Kelompok Usia</h3>
    <div class="donut">
      <svg viewBox="0 0 36 36">
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="3.5"/>
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#5ecfcc" stroke-width="3.5"
          stroke-dasharray="69 31" stroke-linecap="round"/>
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#e05252" stroke-width="3.5"
          stroke-dasharray="31 69" stroke-dashoffset="-69" stroke-linecap="round"/>
      </svg>
      <div class="donut-label">
        <span class="pct" style="color:var(--teal-light)">69%</span>
        <span class="sub">muda</span>
      </div>
    </div>
    <div class="legend">
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--teal-light)"></div>
        <span class="legend-label">18–25 tahun</span>
        <span class="legend-pct">29 (69%)</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--accent-red)"></div>
        <span class="legend-label">26–35 tahun</span>
        <span class="legend-pct">13 (31%)</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background:rgba(255,255,255,.15)"></div>
        <span class="legend-label">36–45 tahun</span>
        <span class="legend-pct">0 (0%)</span>
      </div>
    </div>
  </div>

  <!-- Fakultas -->
  <div class="pie-wrap">
    <h3>Asal Fakultas</h3>
    <div class="donut">
      <svg viewBox="0 0 36 36">
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="3.5"/>
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#0ea5a0" stroke-width="3.5"
          stroke-dasharray="36 64" stroke-linecap="round"/>
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#f0a500" stroke-width="3.5"
          stroke-dasharray="36 64" stroke-dashoffset="-36" stroke-linecap="round"/>
        <circle cx="18" cy="18" r="15.9" fill="none" stroke="#3ecf8e" stroke-width="3.5"
          stroke-dasharray="28 72" stroke-dashoffset="-72" stroke-linecap="round"/>
      </svg>
      <div class="donut-label">
        <span class="pct" style="color:var(--accent-green)">3</span>
        <span class="sub">Fakultas</span>
      </div>
    </div>
    <div class="legend">
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--teal)"></div>
        <span class="legend-label">Teknik</span>
        <span class="legend-pct">15 (36%)</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--gold)"></div>
        <span class="legend-label">Ekonomi</span>
        <span class="legend-pct">15 (36%)</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background:var(--accent-green)"></div>
        <span class="legend-label">FIKES</span>
        <span class="legend-pct">12 (29%)</span>
      </div>
    </div>
  </div>

</div>


  </section>

  <!-- ═══════════════ DISTRIBUSI LIKERT ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Distribusi Jawaban</div>
    <div class="section-title">Data Skala Likert per Pertanyaan</div>


<div class="likert-grid">
  <div class="likert-header">
    <span>Pernyataan</span>
    <span style="text-align:center">STS (1)</span>
    <span style="text-align:center">TS (2)</span>
    <span style="text-align:center">N (3)</span>
    <span style="text-align:center">S (4)</span>
    <span style="text-align:center">SS (5)</span>
  </div>
  <div class="likert-row">
    <span class="col-q">E — Kemudahan Pemahaman</span>
    <span class="col-n">2</span>
    <span class="col-n">6</span>
    <span class="col-n">25</span>
    <span class="col-n">6</span>
    <span class="col-n">3</span>
  </div>
  <div class="likert-row">
    <span class="col-q">F — Kecepatan Proses</span>
    <span class="col-n">0</span>
    <span class="col-n">5</span>
    <span class="col-n">17</span>
    <span class="col-n">15</span>
    <span class="col-n">5</span>
  </div>
  <div class="likert-row">
    <span class="col-q">G — Kendala Sistem</span>
    <span class="col-n">0</span>
    <span class="col-n">5</span>
    <span class="col-n">13</span>
    <span class="col-n">21</span>
    <span class="col-n">3</span>
  </div>
  <div class="likert-row">
    <span class="col-q">H — Kemudahan Pencatatan</span>
    <span class="col-n">1</span>
    <span class="col-n">5</span>
    <span class="col-n">13</span>
    <span class="col-n">18</span>
    <span class="col-n">5</span>
  </div>
  <div class="likert-row">
    <span class="col-q">I — Akurasi Data</span>
    <span class="col-n">1</span>
    <span class="col-n">7</span>
    <span class="col-n">5</span>
    <span class="col-n">17</span>
    <span class="col-n">12</span>
  </div>
</div>


  </section>

  <!-- ═══════════════ BAR CHART RATA-RATA ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Hasil Perhitungan</div>
    <div class="section-title">Nilai Rata-rata per Variabel</div>


<div class="bar-section">
  <h3>Skor Rata-rata (Skala 1–5)</h3>
  <p class="desc">
    Dihitung menggunakan rumus rata-rata tertimbang dari skala Likert dengan n = 42 responden.
    Interpretasi: 1–2 Tidak Setuju · 3 Netral · 4–5 Setuju.
  </p>

  <!-- E: 3.05 / 5 = 61% -->
  <div class="bar-group">
    <div class="bar-head">
      <span class="col-name">E — Kemudahan Pemahaman</span>
      <span class="col-val">3,05</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill" style="width:61%; animation-delay:.1s; background:linear-gradient(90deg,#64748b,#94a3b8)"></div>
    </div>
    <div class="bar-tag tag-netral">→ Netral</div>
  </div>

  <!-- F: 3.48 / 5 = 69.6% -->
  <div class="bar-group">
    <div class="bar-head">
      <span class="col-name">F — Kecepatan Proses</span>
      <span class="col-val">3,48</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill" style="width:69.6%; animation-delay:.2s;"></div>
    </div>
    <div class="bar-tag tag-setuju">→ Cenderung Setuju</div>
  </div>

  <!-- G: 3.52 / 5 = 70.4% -->
  <div class="bar-group">
    <div class="bar-head">
      <span class="col-name">G — Kendala Sistem</span>
      <span class="col-val">3,52</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill" style="width:70.4%; animation-delay:.3s;"></div>
    </div>
    <div class="bar-tag tag-setuju">→ Setuju</div>
  </div>

  <!-- H: 3.50 / 5 = 70% -->
  <div class="bar-group">
    <div class="bar-head">
      <span class="col-name">H — Kemudahan Pencatatan</span>
      <span class="col-val">3,50</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill" style="width:70%; animation-delay:.4s;"></div>
    </div>
    <div class="bar-tag tag-setuju">→ Setuju</div>
  </div>

  <!-- I: 3.76 / 5 = 75.2% -->
  <div class="bar-group">
    <div class="bar-head">
      <span class="col-name">I — Akurasi Data ⭐</span>
      <span class="col-val" style="color:var(--gold)">3,76</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill" style="width:75.2%; animation-delay:.5s; background:linear-gradient(90deg,var(--gold),#ffe08a)"></div>
    </div>
    <div class="bar-tag" style="color:var(--gold)">→ Setuju (tertinggi)</div>
  </div>
</div>


  </section>

  <!-- ═══════════════ HIGHLIGHT STATS ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Temuan Utama</div>
    <div class="section-title">Sorotan Hasil Survei</div>
    <div class="cards cards-2">
      <div class="stat-card">
        <div class="stat-num">3,76</div>
        <div class="stat-info">
          <h4>Skor Tertinggi — Akurasi Data</h4>
          <p>Mahasiswa sangat mempercayai keakuratan data kehadiran yang ditampilkan sistem.</p>
        </div>
      </div>
      <div class="stat-card" style="border-color:rgba(148,163,184,.2)">
        <div class="stat-num" style="color:var(--muted)">3,05</div>
        <div class="stat-info">
          <h4>Skor Terendah — Kemudahan Pemahaman</h4>
          <p>Aspek yang paling perlu ditingkatkan: panduan & sosialisasi penggunaan sistem.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════ KESIMPULAN ═══════════════ -->

  <section class="reveal">
    <div class="section-label">Kesimpulan</div>
    <div class="section-title">Analisis & Rekomendasi</div>
    <div class="conclusion">
      <p>
        Berdasarkan hasil pengolahan data kuesioner dengan skala Likert (1–5) terhadap 42 responden,
        sistem absensi kampus secara keseluruhan dinilai <strong style="color:var(--teal-light)">cukup baik</strong>.
        Aspek <strong>akurasi data kehadiran</strong> (rata-rata 3,76) menjadi keunggulan utama,
        diikuti stabilitas sistem (3,52) dan kemudahan pencatatan (3,50).
      </p>
      <p>
        Namun demikian, aspek <strong style="color:var(--muted)">kemudahan pemahaman</strong> (rata-rata 3,05)
        masih berada pada kategori netral dan menjadi prioritas perbaikan.
        Diperlukan upaya seperti penyediaan <em>panduan penggunaan</em>, pelatihan singkat, atau
        sosialisasi sistem kepada seluruh mahasiswa guna meningkatkan efektivitas penggunaan
        sistem absensi di lingkungan kampus secara menyeluruh.
      </p>
    </div>
  </section>

</main>

<!-- ═══════════════ FOOTER ═══════════════ -->

<footer>
  <p><strong>Laporan Hasil Kuisioner Sistem Absensi Mahasiswa</strong></p>
  <p>Disusun oleh: Ega Irza'ul Fanani (142223067)</p>
  <p>Program Studi Teknik Industri · Fakultas Teknik · Universitas Maarif Hasyim Latif · 2026</p>
</footer>

<script>
  // Scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  reveals.forEach(el => io.observe(el));
</script>

</body>
</html>