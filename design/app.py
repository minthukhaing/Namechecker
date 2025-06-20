import streamlit as st
import base64
from utils.session_utils import initialize_session_state
from streamlit_cookies_manager import CookieManager
from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="Name Checker App",
#     layout="wide",
#     page_icon="😊",
#     initial_sidebar_state="expanded"
# )



# Initialize session state
initialize_session_state()

cookies = CookieManager(prefix="myapp_")

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()


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
         width: 300px !important;

     }}
     </style>
 """

# # Apply custom background
st.markdown(bg, unsafe_allow_html=True)

# # Display image in sidebar
st.logo("./assets/MLLIP.png",size="large")
#Sidebar image
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded}"

# Convert the image to base64
bg_image_base64 = image_to_base64("./assets/mllip-logo1.png")

# Inject CSS
st.markdown(
    """
    <style>
    .sidebar-logo {
        width: 250px;
        height: 250px;
        border-radius: 50%;
        object-fit: cover;
        border: 1px solid #4CAF50;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.8);
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the base64 image in sidebar with custom class
st.sidebar.markdown(
    f"""
    <img src="{bg_image_base64}" class="sidebar-logo" alt="Logo">
    """,
    unsafe_allow_html=True
)
with st.sidebar:

    selected=option_menu(
        menu_title="Name Checker App",
        options=["Dashboard","အကြောင်းအရာ","မြန်မာအညွှန်း","ပါဠိအညွှန်း","Use API"],
        menu_icon="cast",
        icons=["house","bi bi-envelope-fill","bi bi-book-half","bi bi-book-half", "bi bi-terminal-fill"],
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


 
   
   