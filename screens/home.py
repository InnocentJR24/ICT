import streamlit as st
from helpers import go

def render():
    st.markdown("""
<div class="phone">
  <div class="sbar"><span>09:41</span><span>🔋 74% &nbsp;4G</span></div>
  <div class="topnav">
    <div class="topnav-row">
      <div>
        <div class="screen-title">Selamat pagi, Siew Hua 👋</div>
        <div class="screen-sub">Isnin, 19 Mei 2026</div>
      </div>
      <div class="av">SH</div>
    </div>

    <div style="background:rgba(255,255,255,0.13);border-radius:14px;padding:13px 15px;margin-top:14px;">
      <div style="font-size:11px;color:#8fccc5;font-weight:800;letter-spacing:0.06em;">DARREN · 6 TAHUN · MINGGU 14</div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:9px;">
        <div>
          <div style="font-size:30px;font-weight:800;color:#4cc9bd;line-height:1;">78%</div>
          <div style="font-size:11px;color:#8fccc5;margin-top:2px;">program selesai</div>
        </div>
        <div style="flex:1;">
          <div style="height:6px;background:rgba(255,255,255,0.2);border-radius:3px;overflow:hidden;">
            <div style="width:78%;height:6px;background:#4cc9bd;border-radius:3px;"></div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:14px;font-weight:700;color:#ffffff;">5 / 7 sesi</div>
          <div style="font-size:11px;color:#8fccc5;">minggu ini</div>
        </div>
      </div>
    </div>
  </div>

  <div class="slabel">AKTIVITI HARI INI</div>
  <div class="card">
    <div class="arow">
      <div class="aicon" style="background:#e8f5f3;">🗣️</div>
      <div style="flex:1;">
        <div class="atitle">Latihan Perhatian Bersama</div>
        <div class="asub">10 min · Fasa 1 · 🔊 Audio</div>
      </div>
      <span class="pill p-amber">Hari ini</span>
    </div>
    <div class="arow">
      <div class="aicon" style="background:#fdf0eb;">👋</div>
      <div style="flex:1;">
        <div class="atitle">Permainan Peniruan</div>
        <div class="asub">8 min · Fasa 1 · 🎬 Video</div>
      </div>
      <span class="pill p-grey">Selepas ini</span>
    </div>
    <div class="arow">
      <div class="aicon" style="background:#fef9ec;">📚</div>
      <div style="flex:1;">
        <div class="atitle">Buku Cerita Sosial</div>
        <div class="asub">12 min · Fasa 2 · ✨ Baru</div>
      </div>
      <span class="pill p-grey">Selepas ini</span>
    </div>
  </div>

  <div class="slabel">MESEJ PAKAR</div>
  <div class="card" style="background:#e8f5f3;">
    <div style="display:flex;gap:10px;align-items:flex-start;">
      <div class="av" style="background:#2a9d8f;width:34px;height:34px;font-size:12px;">DR</div>
      <div>
        <div style="font-size:12px;font-weight:700;color:#1a3c34;">Dr. Arina &nbsp;·&nbsp; NASOM JB</div>
        <div style="font-size:13px;color:#2c3e36;margin-top:4px;line-height:1.5;">
          Kemajuan Darren minggu lepas sangat menggalakkan! Teruskan latihan perhatian bersama setiap hari 💪
        </div>
        <div style="font-size:11px;color:#8a9ba8;margin-top:5px;">Semalam · 14:22</div>
      </div>
    </div>
  </div>

  <div class="slabel">KEMAJUAN MINGGU INI</div>
  <div class="stats">
    <div class="sbox"><div class="snum">4/5</div><div class="slbl">Kontak mata</div></div>
    <div class="sbox"><div class="snum">↑18%</div><div class="slbl">Vokalisasi</div></div>
    <div class="sbox"><div class="snum">7 hari</div><div class="slbl">Berturut</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️  Mulakan Sesi", key="home_start"):
            go("therapy")
    with col2:
        if st.button("💬  Hubungi Pakar", key="home_chat"):
            go("chat")
