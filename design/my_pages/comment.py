import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import uuid
from streamlit_modal import Modal
import hashlib
import os

def show(cookies):
    # MongoDB Connection
    client = MongoClient("mongodb://localhost:27017/")
    db = client["comment_system"]
    comments_collection = db["comments1"]
    users_collection = db["users"]

    

    POST_ID = "namecheckerapp"

    # CSS Styling
    st.markdown("""
    <style>
        .comment-box {
            border-left: 3px solid #4CAF50;
            padding: 10px;
            margin-left: 20px;
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .user {
            font-weight: bold;
            color: #1E90FF;
        }
        .timestamp {
            font-size: 0.8em;
            color: gray;
        }
        .stButton>button {
            padding: 4px 8px;
            font-size: 12px;
            margin: 2px 1px;
            border-radius: 8px;
        }
        @media screen and (max-width: 600px) {
            div[data-modal-container='true'] {
                width: 95% !important;
                left: 2.5% !important;
                padding: 5px !important;
            }
            div[data-modal-container='true'] > div:first-child {
                padding: 0.5rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # Modal for Reply Form
    modal = Modal(key="Reply Modal", title="🖋️ Write a Reply")

    # User Authentication Functions
    def create_user(username, password):
        """Create a new user account"""
        if users_collection.find_one({"username": username}):
            return False
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        users_collection.insert_one({
            "username": username,
            "password": hashed_pw,
            "created_at": datetime.utcnow()
        })
        return True

    def authenticate(username, password):
        """Authenticate user"""
        user = users_collection.find_one({"username": username})
        if user:
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            if user["password"] == hashed_pw:
                return True
        return False

    # Authentication UI
    def show_auth():
        """Show login/signup forms"""
        st.subheader("Login ဝင်ပါ",divider=True)
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            with st.form("Login"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("Login"):
                    if authenticate(username, password):
                        cookies["user"] = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
        
        with tab2:
            with st.form("Sign Up"):
                new_user = st.text_input("New Username")
                new_pw = st.text_input("New Password", type="password")
                confirm_pw = st.text_input("Confirm Password", type="password")
                if st.form_submit_button("Create Account"):
                    if new_pw != confirm_pw:
                        st.error("Passwords don't match")
                    elif create_user(new_user, new_pw):
                        st.success("Account created! Please login")
                    else:
                        st.error("Username already exists")

    def display_comments(parent_id=None, depth=0):
        """Recursively display comments"""
        query = {"postId": POST_ID, "parentId": parent_id}
        comments = list(comments_collection.find(query).sort("createdAt", 1))
        
        for comment in comments:
            likes = comment.get('likes', 0)
            unlikes = comment.get('unlikes', 0)
            
            with st.container():
                st.markdown(f"""
                <div class='comment-box' style='margin-left: {depth * 20}px;'>
                        <span class='user'>{comment['userId']}</span>: {comment['text']}<br> 
                        <div class='timestamp'>{comment['createdAt'].strftime('%Y-%m-%d %H:%M')}</div>
                    </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns([1,1,1])
                with col1:
                    if cookies.get("user")!= "" and st.button(f"👍 {likes}", key=f"like_{comment['_id']}"):
                        comments_collection.update_one(
                            {"_id": comment["_id"]},
                            {"$inc": {"likes": 1}}
                        )
                        st.rerun()
                with col2:
                    if cookies.get("user")!= "" and st.button(f"👎 {unlikes}", key=f"unlike_{comment['_id']}"):
                        comments_collection.update_one(
                            {"_id": comment["_id"]},
                            {"$inc": {"unlikes": 1}}
                        )
                        st.rerun()
                with col3:
                    if cookies.get("user")!= "" and st.button("💬 Reply", key=f"reply_{comment['_id']}"):
                        cookies["replying_to"] = comment["_id"]

                # Show expander if this is the one we're replying to
                if cookies.get("replying_to") == comment["_id"]:
                    with st.expander("🖋️ Write your reply", expanded=True):
                        reply_text = st.text_area("Your Reply", key=f"reply_input_{comment['_id']}")

                        col=st.columns(4,gap="small",)
                        
                        if col[0].button("📤 Submit Reply", key=f"submit_reply_{comment['_id']}",use_container_width=True):
                            if reply_text.strip():
                                reply_data = {
                                    "_id": uuid.uuid4().hex,
                                    "userId": cookies.get("user"),
                                    "postId": POST_ID,
                                    "text": reply_text,
                                    "parentId": comment["_id"],
                                    "likes": 0,
                                    "unlikes": 0,
                                    "createdAt": datetime.utcnow()
                                }
                                comments_collection.insert_one(reply_data)
                                st.success("✅ Reply added!")
                                cookies["replying_to"] = ""
                                st.rerun()
                        if col[1].button("Cancel",use_container_width=True):
                            cookies["replying_to"] = ""
                            st.rerun()

                # Recursively show replies
                display_comments(comment["_id"], depth + 1)
                
    def add_comment():
        st.subheader("🗨️ Comments")
        display_comments()
        
   
        if cookies.get("user")!= "":

            # New Comment
            st.subheader("➕ Add a New Comment")
            new_comment = st.text_area("Write your comment here:", key="main_comment")
            if st.button("📤 Post Comment"):
                if new_comment.strip():
                    comment_data = {
                        "_id": uuid.uuid4().hex,
                        "userId": cookies.get("user"),
                        "postId": POST_ID,
                        "text": new_comment,
                        "parentId": None,
                        "likes": 0,
                        "unlikes": 0,
                        "createdAt": datetime.utcnow()
                    }
                    comments_collection.insert_one(comment_data)
                    st.success("✅ Comment posted!")
                    cookies["clear_text"] = True
                    st.rerun()

    # Main App Logic
    add_comment()
    if cookies.get("user")!= "":    
        st.sidebar.success(f"Logged in as {cookies.get("user")}")
        if st.sidebar.button("🔓 Logout ",help="Logout from your account", use_container_width=True, type="primary"):
            print("user logout")
            cookies["user"]=""
            print(cookies.get("user"))
            cookies["logged_in"] = False
            st.rerun()            
    else:
        show_auth()