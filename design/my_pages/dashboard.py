from models.my_en_convert import myan
from models.pali_my_convert import parli

import asyncio
import streamlit as st
import pyperclip
from streamlit.components.v1 import html


def show(cookies):
    
    from components.header import render_header
    from components.footer import render_footer
    from my_pages.comment import show

    render_header()

    st.markdown("""
    <style>
    .st-key-container1 input {
        background-color: white;
        color: black;
        font-size: 20px;
        border: 2px solid green;
    }
    </style>
    """, unsafe_allow_html=True)
    

    st.write("Name Checker App")
    with st.container(border=True,key="container1"):
        #st.title("NAME CHECKER")
        result=""
        tab1, tab2 = st.tabs(
            ["မြန်မာ-အင်္ဂလိပ်","ပါဠိ-ရိုမန်"] )

        with tab1:
            #st.header("မြန်မာ-အင်္ဂလိပ်")
            my=st.text_input("မြန်မာအမည်များကို ရိုက်ထည့်ပါ",key="txt1") 

             # HTML + JS for copying to clipboard
             # Copy to clipboard functionality using HTML + JS
           
            
            btnmy=st.button("Convert",type="primary",key="btn1",)
            
            if btnmy:
                result=asyncio.run(myan(my))
                out_my=st.text_input("အင်္ဂလိပ်ဘာသာပြန် မြန်မာစကားလုံးများ",value=result,key="txt11" )

                copy_js = f"""
                <script>
                    function copyToClipboard() {{
                        const el = document.createElement('textarea');
                        el.value = '{result}';
                        document.body.appendChild(el);
                        el.select();
                        document.execCommand('copy');
                        document.body.removeChild(el);
                       
                    }}
                </script>
                <button onclick="copyToClipboard()" style=" margin-top: 10px;
                border: 1px solid #4CAF50;
                background-color: red;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                color: white;
                font-family: Arial, sans-serif;
                display: inline-flex;
                align-items: center;
                transition: background-color 0.3s ease;">
                    <span title="Copy to clipboard" style="span style="margin-right: 8px; font-size: 24px;">Copy</span>
                </button>
                """
                
                st.components.v1.html(copy_js,width=100)
                

        with tab2:
            #st.header("ပါဠိ-ရိုမန်")
            my=st.text_input("ပါဠိအမည်များကို ရိုက်ထည့်ပါ",key="txt2")    
            btnmy=st.button("Convert",type="primary",key="btn2")
            if btnmy:
                result1=asyncio.run(parli(my))
                out_my=st.text_input("အင်္ဂလိပ်ဘာသာပြန် ပါဠိစကားလုံးများ",value=result1,key="txt22",disabled =True)

                copy_js = f"""
                <script>
                    function copyToClipboard() {{
                        const el = document.createElement('textarea');
                        el.value = '{result1}';
                        document.body.appendChild(el);
                        el.select();
                        document.execCommand('copy');
                        document.body.removeChild(el);
                       
                    }}
                </script>
                <button onclick="copyToClipboard()" style=" margin-top: 10px;
                border: 1px solid #4CAF50;
                background-color: red;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                color: white;
                font-family: Arial, sans-serif;
                display: inline-flex;
                align-items: center;
                transition: background-color 0.3s ease;">
                    <span title="Copy to clipboard" style="span style="margin-right: 8px; font-size: 24px;">Copy</span>
                </button>
                """
                
                st.components.v1.html(copy_js,width=100)
    
    with st.container(border=True):
        show(cookies)
    render_footer()