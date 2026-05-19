import streamlit as st
from helpers import go

def render():
    st.markdown("""
<div class="phone">
  <div class="sbar"><span>09:41</span><span>🔋 74% &nbsp;4G</span></div>
  <div class="topnav">
    <div class="topnav-row">
      <div style="font-size:22px;color:#8fccc5;">&#8592;</div>
      <div style="display:flex;align-items:center;gap:10px;">
        <div class="av" style="background:#f4a261;font-size:12px;width:32px;height:32px;">DR</div>
        <div>
          <div style="font-size:14px;font-weight:700;color:#ffffff;">Dr. Arina Zulkifli</div>
          <div style="font-size:11px;color:#8fccc5;">NASOM Johor Bahru &nbsp;·&nbsp; Biasanya balas dalam 24j</div>
        </div>
      </div>
      <div style="font-size:20px;color:#8fccc5;">⋮</div>
    </div>
  </div>

  <div style="padding:16px 16px 80px;">

    <div style="text-align:center;margin-bottom:14px;">
      <span class="pill p-grey">Khamis, 15 Mei 2026</span>
    </div>

    <div class="bmsg">
      <div class="bname">Dr. Arina</div>
      <div class="bin">
        Siew Hua, laporan minggu lepas sudah saya terima. Kontak mata Darren meningkat dari 2/5 ke 4/5 — ini sangat positif! 👏
      </div>
      <div class="btime">14:22</div>
    </div>

    <div class="bmsg" style="text-align:right;">
      <div class="bout">
        Terima kasih Doktor. Darren masih susah untuk duduk diam lebih dari 5 minit.
      </div>
      <div class="btime-r">16:05</div>
    </div>

    <div class="bmsg">
      <div class="bname">Dr. Arina</div>
      <div class="bin">
        Normal untuk umur dan tahap dia. Cuba pendekkan sesi kepada 3–4 minit dengan rehat pendek di tengah. Saya akan muat naik video demonstrasi hari Sabtu 🎬
      </div>
      <div class="btime">17:30</div>
    </div>

    <div style="text-align:center;margin:14px 0;">
      <span class="pill p-grey">Hari ini, 19 Mei 2026</span>
    </div>

    <div class="bmsg" style="text-align:right;">
      <div class="bout">
        <div style="font-size:10px;color:rgba(255,255,255,0.7);margin-bottom:4px;font-weight:700;">📊 LAPORAN SESI — 19 MEI</div>
        Kontak mata: 4/5 &nbsp;·&nbsp; Mood: 🙂 &nbsp;·&nbsp; 9 min<br>
        <span style="font-size:11px;opacity:0.8;">Latihan Perhatian Bersama, Fasa 1</span>
      </div>
      <div class="btime-r">09:41 &nbsp;✓✓</div>
    </div>

    <div class="alert-warn">
      <div class="alert-title" style="color:#9a6b00;">⏱ MENUNGGU BALASAN</div>
      <div class="alert-body" style="color:#7a5500;">Dr. Arina biasanya membalas dalam 24 jam.</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

    if st.button("← Kembali ke Utama", key="chat_back"):
        go("home")
