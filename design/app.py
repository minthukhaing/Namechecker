import streamlit as st
import base64
from utils.session_utils import initialize_session_state
from streamlit_cookies_manager import CookieManager
from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="Name Cheacker App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
    
# )


# Initialize session state
initialize_session_state()

cookies = CookieManager(prefix="myapp_")

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()


# Inject CSS with correct formatting using f-string
bg_image = "./assets/mllip-logo.jpg"
  # Ensure the file exists in this relative path

# Local Image (background.jpg) ကို Base64 အဖြစ် encode လုပ်ပါ
with open("assets/img1.jpg", "rb") as f:
    img_data = f.read()
encoded_img = base64.b64encode(img_data).decode()

# # CSS style
bg = f"""
     <style>
     [data-testid="stAppViewContainer"] {{
         background-color: {"#9FDABDF8"};
         color: {"#09189FF8"};
         font-family: "Segoe UI", Roboto, sans-serif;
         background-image: url(data:image/jpeg;base64,{encoded_img});
         background-size: cover;
         background-position: bottom;
       
        
     }}

    /* [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
    }} */

    [data-testid="stSidebar"] > div:first-child {{
         //background-color: {"#88B3BDFF"};  /* Sidebar transparency */

          background-image: url(data:image/jpeg;base64,{encoded_img});
         background-size: cover;
         background-position: bottom;

     }}
     </style>
 """

# # Apply custom background
st.markdown(bg, unsafe_allow_html=True)
# # Display image in sidebar
st.logo("./assets/MLLIP.png",size="large")
st.sidebar.image(bg_image,use_container_width=True,output_format="auto",channels="BGR",clamp=True)


with st.sidebar:

    selected=option_menu(
        menu_title="Name Checker App",
        options=["Dashboard","အကြောင်းအရာ","မြန်မာအညွှန်း","ပါဠိအညွှန်း","Use API"],
        menu_icon="cast",
        icons=["house","file-earmark-slides-fill","file-earmark-ppt-fill","file-earmark-ppt-fill"],
        default_index=0,
        orientation="vertical"
    )

    st.markdown("---")
   

if selected == "Dashboard":
    print("Dashboard")
    cookies["page"]="Dashboard"
    from my_pages.dashboard import show
    show(cookies)
elif selected== "အကြောင်းအရာ":
    print("About")
    from my_pages.about import show
    show()
elif selected == "မြန်မာအညွှန်း":
    from my_pages.mm_indicator import show
    show()
elif selected == "ပါဠိအညွှန်း":
    from my_pages.parli_indicator import show
    show()
elif selected == "Use API":
    from my_pages.use_api import show
    show()


 
   
   