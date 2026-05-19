import streamlit as st

def init():
    defaults = {
        "screen":       "home",
        "therapy_step": 0,
        "t_resps":      ["✅", "✅", "🔶", "✅", "🔶"],
        "t_mood":       "🙂",
        "ms_done":      False,
        "ms_vals":      {},
        "ref_sent":     False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def go(screen):
    st.session_state.screen = screen
    st.rerun()

def sidebar():
    with st.sidebar:
        st.markdown("### 🤝 SayangASD")
        st.markdown("---")
        st.markdown("**👩 Siew Hua — Caregiver**")
        if st.button("🏠  Home"):              go("home")
        if st.button("🗣️  Therapy Session"):   go("therapy")
        if st.button("💬  Specialist Chat"):   go("chat")
        st.markdown("---")
        st.markdown("**🏥 Fadzli — CHW**")
        if st.button("📋  Milestone Check"):   go("milestone")
        st.markdown("---")
        st.markdown("**🏘️ Dato' Razak — Ketua Kampung**")
        if st.button("💰  Financial Aid"):     go("aid")
        if st.button("📨  Referral Form"):     go("referral")
        st.markdown("---")
        st.markdown("**Edge Cases**")
        if st.button("📵  Offline Mode"):      go("offline")
        if st.button("⚠️  Sync Conflict"):     go("conflict")
