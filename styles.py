CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], * {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    box-sizing: border-box;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

.stApp { background: #d6e4e0 !important; }
.block-container { padding: 1rem 0 4rem 0 !important; max-width: 400px !important; margin: 0 auto !important; }

/* ── Phone wrapper ── */
.phone {
    background: #ffffff;
    border-radius: 32px;
    overflow: hidden;
    box-shadow: 0 24px 60px rgba(0,0,0,0.25);
    min-height: 760px;
    padding-bottom: 20px;
}

/* ── Status bar ── */
.sbar {
    background: #1a3c34;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 10px 22px 8px;
    display: flex;
    justify-content: space-between;
}

/* ── Top nav ── */
.topnav {
    background: #1a3c34;
    padding: 10px 20px 18px;
}
.topnav-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.screen-title { font-size: 19px; font-weight: 800; color: #ffffff; margin: 0; }
.screen-sub   { font-size: 12px; color: #8fccc5; margin: 2px 0 0; }

/* ── Avatar ── */
.av {
    width: 36px; height: 36px; border-radius: 50%;
    background: #2a9d8f; color: #ffffff;
    font-size: 13px; font-weight: 700;
    display: inline-flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}

/* ── Section label ── */
.slabel {
    font-size: 10px; font-weight: 800; color: #9aabb5;
    letter-spacing: 0.1em; text-transform: uppercase;
    padding: 14px 20px 6px;
}

/* ── Generic card ── */
.card {
    background: #ffffff;
    border-radius: 18px;
    box-shadow: 0 2px 14px rgba(0,0,0,0.07);
    padding: 16px 18px;
    margin: 0 16px 12px;
}

/* ── Activity row inside card ── */
.arow {
    display: flex; align-items: center; gap: 12px;
    padding: 11px 0; border-bottom: 1px solid #f0f5f4;
}
.arow:last-child { border-bottom: none; }
.aicon {
    width: 44px; height: 44px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
}
.atitle { font-size: 14px; font-weight: 700; color: #1a3c34; margin: 0 0 2px; }
.asub   { font-size: 12px; color: #8a9ba8; margin: 0; }

/* ── Pills ── */
.pill {
    display: inline-block; border-radius: 20px;
    padding: 3px 10px; font-size: 11px; font-weight: 700;
    white-space: nowrap;
}
.p-teal   { background: #d0f0ec; color: #1a6b61; }
.p-amber  { background: #fdeec9; color: #9a6b00; }
.p-green  { background: #d4edda; color: #196b35; }
.p-grey   { background: #e8ecef; color: #5a6a74; }
.p-coral  { background: #fce0d5; color: #a83a1a; }

/* ── Stats strip ── */
.stats { display: flex; gap: 10px; padding: 0 16px 12px; }
.sbox  {
    flex: 1; background: #f3f8f7; border-radius: 14px;
    padding: 12px 8px; text-align: center;
}
.snum { font-size: 21px; font-weight: 800; color: #1a3c34; }
.slbl { font-size: 10px; color: #8a9ba8; font-weight: 600; margin-top: 2px; }

/* ── Chat bubbles ── */
.bmsg { margin-bottom: 10px; }
.bname { font-size: 10px; font-weight: 700; color: #8a9ba8; margin-bottom: 3px; }
.bin {
    display: inline-block; background: #e8f5f3; color: #1a3c34;
    border-radius: 16px 16px 16px 4px;
    padding: 10px 14px; font-size: 13px; max-width: 82%;
}
.bout {
    display: block; background: #2a9d8f; color: #ffffff;
    border-radius: 16px 16px 4px 16px;
    padding: 10px 14px; font-size: 13px;
    max-width: 82%; margin-left: auto; text-align: left;
}
.btime { font-size: 10px; color: #aab8c0; margin-top: 3px; }
.btime-r { font-size: 10px; color: #aab8c0; margin-top: 3px; text-align: right; }

/* ── Scheme card ── */
.scheme {
    border: 1.5px solid #dde8e6; border-radius: 14px;
    padding: 13px 15px; margin: 0 16px 10px;
}
.sname   { font-size: 14px; font-weight: 700; color: #1a3c34; }
.samount { font-size: 20px; font-weight: 800; color: #2a9d8f; margin: 3px 0; }
.smeta   { font-size: 11px; color: #8a9ba8; }

/* ── Form fields (read-only style) ── */
.ff { margin-bottom: 13px; }
.flabel {
    font-size: 10px; font-weight: 700; color: #9aabb5;
    text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px;
}
.fval {
    font-size: 14px; font-weight: 600; color: #1a3c34;
    background: #f3f8f7; border-radius: 10px; padding: 10px 13px;
}

/* ── Alert banners ── */
.alert-warn  { background: #fff8e6; border-left: 4px solid #f4a261; border-radius: 10px; padding: 11px 13px; margin-bottom: 12px; }
.alert-ok    { background: #e6f7f4; border-left: 4px solid #2a9d8f; border-radius: 10px; padding: 11px 13px; margin-bottom: 12px; }
.alert-red   { background: #fde8e8; border-left: 4px solid #e76f51; border-radius: 10px; padding: 11px 13px; margin-bottom: 12px; }
.alert-title { font-size: 12px; font-weight: 800; margin-bottom: 3px; }
.alert-body  { font-size: 12px; }

/* ── Bar chart ── */
.bars {
    display: flex; align-items: flex-end; gap: 3px;
    height: 52px; background: #f3f8f7; border-radius: 10px;
    padding: 6px 8px;
}
.bar {
    flex: 1; border-radius: 4px 4px 0 0; align-self: flex-end;
}

/* ── Progress bar ── */
.pbar-bg   { background: #e0eeec; border-radius: 6px; height: 8px; overflow: hidden; margin-bottom: 10px; }
.pbar-fill { height: 8px; border-radius: 6px; background: #2a9d8f; }

/* ── Timeline ── */
.tl { display: flex; gap: 12px; margin-bottom: 12px; }
.tl-left { display: flex; flex-direction: column; align-items: center; padding-top: 2px; }
.tl-dot  { width: 11px; height: 11px; border-radius: 50%; background: #2a9d8f; flex-shrink: 0; }
.tl-line { width: 2px; background: #c8e8e4; flex: 1; margin-top: 3px; }
.tl-title { font-size: 13px; font-weight: 700; color: #1a3c34; }
.tl-meta  { font-size: 11px; color: #8a9ba8; margin-top: 1px; }

/* ── Streamlit button override ── */
div.stButton > button {
    background: #2a9d8f !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    width: 100% !important;
    padding: 13px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    transition: background 0.2s !important;
    margin: 2px 0 !important;
}
div.stButton > button:hover  { background: #237a6e !important; }
div.stButton > button:active { background: #1a5c55 !important; }

/* Select box styling */
div[data-baseweb="select"] {
    border-radius: 10px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1a3c34 !important;
    min-width: 220px !important;
}
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown h3,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #ffffff !important;
}
section[data-testid="stSidebar"] div.stButton > button {
    background: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    font-size: 13px !important;
    padding: 9px !important;
    border-radius: 10px !important;
    text-align: left !important;
    margin: 2px 0 !important;
}
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: rgba(255,255,255,0.22) !important;
}
</style>
"""
