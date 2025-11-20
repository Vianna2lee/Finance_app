from functions import *
import streamlit as st 
from streamlit_searchbox import st_searchbox # pip install streamlit-searchbox
# streamlit run My_app/navigation_page.py to run the app



if "stock_searchbox" not in st.session_state or st.session_state["stock_searchbox"] is None:
        st.session_state["stock_searchbox"] = 0

selected = st_searchbox(stock_search_suggestions, placeholder="Type to search for stocks ...", key=st.session_state["stock_searchbox"])
 


if selected is not None: # new selection made
    st.session_state['stock_symbol'] =  str(selected.split(' — ')[0] )
    st.session_state['stock_searchbox'] += 1 
    st.switch_page("stock_page.py")
    st.rerun()



st.title("Personal Page")


st.write(f"Welcome, {st.session_state['Username']}!")

st.write(st.session_state["stock_list"])
   

