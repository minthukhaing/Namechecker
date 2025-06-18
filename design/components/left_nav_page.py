def render_left_nav_bar(cookies):
    import streamlit as st

   

    #### page title , logo ချိန်းရန်


    current_page = cookies.get("page", "home")
    role = cookies.get("role", "user")
    lang = cookies.get("language", "en")

#     encoded_img=r"C:\Users\user\Desktop\NAME\name-checker-comment\Namechecker\design\assets\logo1.png"
#     page_bg_img = f'''
#     <style>
#     .stApp {{
#         background-image: url(data:image/jpg;base64,{encoded_img});
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     '''
# # Streamlit တွင် CSS ထည့်ပါ
#     st.markdown(page_bg_img, unsafe_allow_html=True)

     # Sidebar မှာ logo ကို center ပြပေးတဲ့ styling
    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 50%;
        }
        .logo {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    #Logo Image
    #st.logo("assets/logo.png",size="large")
  
    #st.sidebar.image("assets/logo3.jpg")

    # Sidebar header with logo
    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            width: 100%;
            max-width: 300px;
        }
       
        .nav-button {
            background-color: #f0f0f0;
            color: #333;
            border: none;
            width: 100%;
            text-align: left;
            padding: 10px 15px;
            margin: 5px 0;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .nav-button:hover { background-color: #e0e0e0; }
        .active {
            background-color: #d1ecf1 !important;
            color: #0c5460;
            font-weight: bold;
        }
        .sub-menu { margin-left: 20px; }
        .search-box input {
            width: 100%;
            padding: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    #st.image("assets/logo3.jpg")
    # Search box
    search_term = st.text_input("🔍 Search", placeholder="Search menu...", key="menu_search")

    ###### nav - bar မှာ button ထပ်ထည့်ရန်

    # Menu items with roles and icons
    menu_items = {
        "Dashboard": {"key":"dashboard" , "icon": "🏠"},       
        "အကြောင်းအရာ": {"key": "about", "icon": "🖨️"},  
         "မြန်မာအညွှန်း": {"key": "mm", "icon": "📗"},
         "ပါဠိအညွှန်း": {"key": "parli", "icon": "📗"},       
       
      
    }

    # Render filtered menu
    for label, item in menu_items.items():
        if isinstance(item, dict):
            if "roles" in item and role not in item["roles"]:
                continue

            has_nested_items = any(isinstance(sub_item, dict) for sub_label, sub_item in item.items())

            if has_nested_items:
                with st.expander(f"📁 {label}"):
                    for sub_label, sub_item in item.items():
                        if not isinstance(sub_item, dict):
                            continue
                        if "roles" in sub_item and role not in sub_item["roles"]:
                            continue

                        icon = sub_item.get("icon", "")
                        btn_label = f"{icon} {sub_label}"

                        is_active = current_page == sub_item.get("key", "")
                        btn_class = "nav-button active" if is_active else "nav-button"

                        if search_term.lower() in sub_label.lower():
                            if st.button(btn_label, key=f"btn_{sub_item['key']}", use_container_width=True):
                                cookies["page"] = sub_item["key"]
            else:
                icon = item.get("icon", "")
                btn_label = f"{icon} {label}"

                is_active = current_page == item.get("key", "")
                btn_class = "nav-button active" if is_active else "nav-button"

                if search_term.lower() in label.lower():
                    if st.button(btn_label, key=f"btn_{item['key']}", use_container_width=True):
                        cookies["page"] = item["key"]

        else:
            # Fallback for plain string entries (shouldn't happen if all are dicts)
            if search_term.lower() in label.lower():
                if st.button(label, key=f"btn_{label}", use_container_width=True):
                    cookies["page"] = label.lower()

    st.markdown("---")
    st.markdown("#### 🎨 Theme")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌞", key="btn_light", help="Switch to Light Mode"):
            cookies["theme"] = "light"
            st.rerun()
    with col2:
        if st.button("🌙", key="btn_dark", help="Switch to Dark Mode"):
            cookies["theme"] = "dark"
            st.rerun()
            
    st.markdown("---")

