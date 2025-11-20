import streamlit as st 
from functions import *
# streamlit run My_app/login_page.py to run the app

st.title("Login Page")

if "Username" not in st.session_state:
    st.session_state["Username"] = None



if "stock_list" not in st.session_state or st.session_state["stock_list"] is None:
    st.session_state["stock_list"] = []



with st.form("Login", enter_to_submit=True):
    username = st.text_input("Enter username:", placeholder="Enter username")
    password = st.text_input("Enter password:", type="password", placeholder="Enter password")
    

    button = st.form_submit_button("Login")


    if button:
        error=[]
        if not username or not password:
            error.append("All fields are required. Please fill in all details.")
        if password_checker(username, password) == False:
            error.append("Incorrect username or password")    
        
        if error:
            for err in error:
                st.error(err)
        else:
            st.success("You have been logged in successfully.")
            st.session_state["logged_in"]=True
            st.rerun()



            
            
            
