import streamlit as st
from helpers import go

OPTS = ["✅ Dicapai", "🔶 Hampir", "❌ Belum"]

def render():
    S = st.session_state
    step = S.therapy_step

    # ── header (same for both steps) ────────────────────────────
    st.markdown("""
<div class="phone">
  <div class="sbar"><span>09:41</span><span>🔋 74% &nbsp;4G</span></div>
  <div class="topnav">
    <div class="topnav-row">
      <div style="font-size:22px;color:#8fccc5;cursor:pointer;">&#8592;</div>
      <div style="text-align:center;">
        <div class="screen-title" style="font-size:16px;">Latihan Perhatian Bersama</div>
        <div class="screen-sub">Fasa 1 · Hari 14</div>
      </div>
      <div style="font-size:20px;color:#8fccc5;">🔊</div>
    </div>
  </div>
""", unsafe_allow_html=True)

    # ── STEP 0: log activity ─────────────────────────────────────
    if step == 0:
        st.markdown("""
  <div style="padding:16px;">
    <div style="background:#1a3c34;border-radius:18px;padding:20px;text-align:center;margin-bottom:14px;">
      <div style="font-size:50px;">🎯</div>
      <div style="font-size:15px;font-weight:700;color:#ffffff;margin-top:8px;">Tunjukkan benda kepada Darren</div>
      <div style="font-size:13px;color:#8fccc5;margin-top:6px;line-height:1.5;">
        Sebut namanya dengan jelas, tunggu dia melihat muka anda. Ulang 5 kali.
      </div>
    </div>
    <div class="alert-ok">
      <div class="alert-title" style="color:#1a6b61;">🔊 ARAHAN AUDIO AKTIF</div>
      <div class="alert-body" style="color:#1a3c34;font-style:italic;">
        "Ambil bola merah, tunjuk kepada Darren dan katakan 'bola'. Tunggu dia tengok muka awak..."
      </div>
    </div>
    <div style="font-size:11px;font-weight:800;color:#9aabb5;letter-spacing:0.08em;margin-bottom:8px;">REKOD SETIAP PERCUBAAN</div>
  </div>
""", unsafe_allow_html=True)

        cols = st.columns(5)
        resps = []
        for i, col in enumerate(cols):
            with col:
                v = st.selectbox(f"#{i+1}", OPTS, key=f"tr{i}",
                                 index=OPTS.index(S.t_resps[i]) if i < len(S.t_resps) else 0)
                resps.append(v)

        mood = st.select_slider(
            "Mood Darren hari ini",
            options=["😢", "😕", "😐", "🙂", "😄"],
            value="🙂"
        )

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("✅  Simpan & Selesai", key="therapy_save"):
            S.therapy_step = 1
            S.t_resps = resps
            S.t_mood  = mood
            st.rerun()

    # ── STEP 1: results ─────────────────────────────────────────
    elif step == 1:
        score = sum(1 for r in S.t_resps if "✅" in r)
        mood  = S.t_mood

        heights = [18, 20, 16, 22, 25, 19, 28, 24, 30, 26, 32, 28, 35, min(score * 9 + 10, 46)]
        bars_html = "".join(
            f'<div class="bar" style="height:{h}px;background:{"#2a9d8f" if i==13 else "#b8ddd9"};"></div>'
            for i, h in enumerate(heights)
        )

        st.markdown(f"""
  <div style="padding:16px;">
    <div style="text-align:center;padding:18px 0 14px;">
      <div style="font-size:54px;">🎉</div>
      <div style="font-size:22px;font-weight:800;color:#1a3c34;margin-top:8px;">Sesi Selesai!</div>
      <div style="font-size:13px;color:#8a9ba8;margin-top:3px;">Darren melakukan dengan baik hari ini</div>
    </div>

    <div class="stats" style="padding:0;margin-bottom:16px;">
      <div class="sbox"><div class="snum">{score}/5</div><div class="slbl">Kontak mata</div></div>
      <div class="sbox"><div class="snum">{mood}</div><div class="slbl">Mood</div></div>
      <div class="sbox"><div class="snum">9 min</div><div class="slbl">Tempoh</div></div>
    </div>

    <div style="font-size:11px;font-weight:800;color:#9aabb5;letter-spacing:0.08em;margin-bottom:8px;">
      TREND 14 HARI — KONTAK MATA
    </div>
    <div class="bars">{bars_html}</div>

    <div class="alert-ok" style="margin-top:14px;">
      <div class="alert-title" style="color:#1a6b61;">💾 DISIMPAN SECARA TEMPATAN</div>
      <div class="alert-body" style="color:#1a3c34;">
        Akan disegerakkan ke awan apabila dalam talian.
      </div>
    </div>
  </div>
""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📤  Hantar ke Pakar", key="therapy_send"):
                go("chat")
        with col2:
            if st.button("🏠  Utama", key="therapy_home"):
                S.therapy_step = 0
                go("home")

    st.markdown("</div>", unsafe_allow_html=True)
