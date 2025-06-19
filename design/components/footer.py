def render_footer():
    import streamlit as st

    theme = "light"
    bg_color = "#ebeaf3" if theme == "light" else "#2e2e2e"
    text_color = "#200AC1" if theme == "light" else "#fff"

    st.markdown(f"""
    <style>
    .footer {{
        background-color: {bg_color};
        color: {text_color};
        text-align: center;
        padding: 1em;
        margin-top: 2em;
        border-top: 1px solid #ccc;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2025 Name Cheacker App</div>', unsafe_allow_html=True)