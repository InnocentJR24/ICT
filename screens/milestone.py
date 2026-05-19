import streamlit as st
from helpers import go

OPTS  = ["✅ Dicapai", "🔶 Berkembang", "❌ Belum Lagi"]
SCORE = {"✅ Dicapai": 2, "🔶 Berkembang": 1, "❌ Belum Lagi": 0}

SOCIAL_ITEMS = [
    ("ms1", "Balas nama apabila dipanggil",       "🔶 Berkembang"),
    ("ms2", "Hubungan mata semasa berinteraksi",  "🔶 Berkembang"),
    ("ms3", "Minat pada kanak-kanak lain",        "❌ Belum Lagi"),
    ("ms4", "Bermain imaginasi / pura-pura",      "❌ Belum Lagi"),
]
COMM_ITEMS = [
    ("ms5", "Menggunakan frasa 2 patah perkataan","❌ Belum Lagi"),
    ("ms6", "Menunjuk benda untuk tunjuk minat",  "🔶 Berkembang"),
    ("ms7", "Mengikut arahan 2 langkah",          "❌ Belum Lagi"),
    ("ms8", "Memahami soalan mudah",              "🔶 Berkembang"),
]

def render():
    S = st.session_state

    # Seed defaults
    for k, _, default in SOCIAL_ITEMS + COMM_ITEMS:
        if k not in S.ms_vals:
            S.ms_vals[k] = default

    st.markdown("""
<div class="phone">
  <div class="sbar"><span>09:41</span><span>🔋 81% &nbsp;WiFi</span></div>
  <div class="topnav">
    <div class="topnav-row">
      <div style="font-size:22px;color:#8fccc5;">&#8592;</div>
      <div style="text-align:center;">
        <div class="screen-title" style="font-size:16px;">Penilaian Pencapaian</div>
        <div class="screen-sub">Ahmad bin Hassan · 4 tahun</div>
      </div>
      <div class="av" style="background:#f4a261;font-size:12px;width:32px;height:32px;">FB</div>
    </div>
  </div>
""", unsafe_allow_html=True)

    # ── FORM ────────────────────────────────────────────────────
    if not S.ms_done:
        st.markdown('<div class="slabel">SOSIAL</div><div class="card">', unsafe_allow_html=True)
        for k, label, _ in SOCIAL_ITEMS:
            c1, c2 = st.columns([2, 1])
            c1.markdown(
                f"<div style='font-size:13px;font-weight:600;color:#1a3c34;padding-top:10px;'>{label}</div>",
                unsafe_allow_html=True
            )
            with c2:
                S.ms_vals[k] = st.selectbox(
                    label, OPTS, key=f"sel_{k}",
                    index=OPTS.index(S.ms_vals.get(k, OPTS[1])),
                    label_visibility="collapsed"
                )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="slabel">KOMUNIKASI</div><div class="card">', unsafe_allow_html=True)
        for k, label, _ in COMM_ITEMS:
            c1, c2 = st.columns([2, 1])
            c1.markdown(
                f"<div style='font-size:13px;font-weight:600;color:#1a3c34;padding-top:10px;'>{label}</div>",
                unsafe_allow_html=True
            )
            with c2:
                S.ms_vals[k] = st.selectbox(
                    label, OPTS, key=f"sel_{k}",
                    index=OPTS.index(S.ms_vals.get(k, OPTS[1])),
                    label_visibility="collapsed"
                )
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("📊  Jana Laporan Penilaian", key="ms_submit"):
            S.ms_done = True
            st.rerun()

    # ── REPORT ──────────────────────────────────────────────────
    else:
        all_keys  = [k for k, _, _ in SOCIAL_ITEMS + COMM_ITEMS]
        total     = sum(SCORE.get(S.ms_vals.get(k, "🔶 Berkembang"), 1) for k in all_keys)
        max_score = len(all_keys) * 2
        pct       = total / max_score * 100
        s_soc     = sum(SCORE.get(S.ms_vals.get(k, "🔶 Berkembang"), 1) for k, _, _ in SOCIAL_ITEMS)
        s_com     = sum(SCORE.get(S.ms_vals.get(k, "🔶 Berkembang"), 1) for k, _, _ in COMM_ITEMS)

        soc_w = int(s_soc / 8 * 100)
        com_w = int(s_com / 8 * 100)

        st.markdown(f"""
  <div style="padding:16px;">
    <div style="background:#1a3c34;border-radius:18px;padding:18px;color:#ffffff;text-align:center;margin-bottom:14px;">
      <div style="font-size:10px;color:#8fccc5;font-weight:800;letter-spacing:0.08em;">LAPORAN PENILAIAN</div>
      <div style="font-size:14px;font-weight:700;margin-top:3px;">Ahmad bin Hassan · 4 tahun</div>
      <div style="font-size:11px;color:#8fccc5;">Fadzli bin Nordin &nbsp;·&nbsp; 19 Mei 2026</div>
      <div style="font-size:46px;font-weight:800;color:#4cc9bd;margin:10px 0;">{pct:.0f}%</div>
      <div style="font-size:12px;color:#8fccc5;">{total} daripada {max_score} markah</div>
    </div>

    <div class="alert-red">
      <div class="alert-title" style="color:#a83a1a;">🚨 RUJUKAN SEGERA DISYORKAN</div>
      <div class="alert-body" style="color:#7a2a10;">
        Markah di bawah 50%. Hantar ke Hospital Sultanah Aminah dengan segera.
      </div>
    </div>

    <div style="padding:0 2px;">
      <div style="font-size:13px;font-weight:700;color:#1a3c34;margin-bottom:4px;">Sosial &nbsp;<span style="color:#8a9ba8;font-weight:400;">{s_soc}/8</span></div>
      <div class="pbar-bg"><div class="pbar-fill" style="width:{soc_w}%;"></div></div>

      <div style="font-size:13px;font-weight:700;color:#1a3c34;margin-bottom:4px;">Komunikasi &nbsp;<span style="color:#8a9ba8;font-weight:400;">{s_com}/8</span></div>
      <div class="pbar-bg"><div class="pbar-fill" style="width:{com_w}%;"></div></div>
    </div>
  </div>
""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📨  Hantar ke Pakar", key="ms_send"):
                st.toast("✅ Dihantar ke Hospital Sultanah Aminah!", icon="✅")
        with col2:
            if st.button("🔄  Mulakan Semula", key="ms_reset"):
                S.ms_done = False
                S.ms_vals = {}
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
