def render_header():
    import streamlit as st

    theme = "light"

    bg_color = "#ffffff" if theme == "light" else "#1f1f1f"
    text_color = "#140479" if theme == "light" else "#ffffff"

    st.markdown(f"""
    <style>
    .header {{
        background-color: {bg_color};
        color: {text_color};
        padding: 1em;
        text-align: center;
        font-size: 2.2em;
        border-bottom: 1px solid #ddd;
        font-weight: bold; 

    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">အမျိုးသားဉာဏ်ရည်တုနည်းပညာဖွံ့ဖြိုးတိုးတက်ရေးစီမံကိန်း</div>', unsafe_allow_html=True)