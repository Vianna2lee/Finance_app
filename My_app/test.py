
import streamlit as st
from functions import *
import numpy as np

if not hasattr(np, "float"): 
    np.float = float

from optionprice import Option #pip install option-price
from streamlit_searchbox import st_searchbox
import datetime
import numpy as np #pip install --upgrade numpy
s0_input_type =0



if s0_input_type == "Manual":
    s0 = st.number_input("spot price (current stock price): ", placeholder="Type current stock price...")
else:
    selected = st_searchbox(stock_search_suggestions, placeholder="Type to search for stocks ...",
                             key=st.session_state["stock_searchbox"])
    if selected:
        stock_symbol = str(selected.split(' — ')[0] )
        s0 = yf.Ticker(stock_symbol).fast_info["last_price"]

s0 = round(s0, 2)