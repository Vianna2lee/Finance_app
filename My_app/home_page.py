from streamlit_searchbox import st_searchbox
from functions import *
import pandas as pd
import yfinance as yf # pip install yfinance
import streamlit as st
import datetime as dt 
st.set_page_config(layout="wide")

# need to install streamlit-searchbox by trying: pip install streamlit-searchbox
# run with: streamlit run My_app/home_page.py
# streamlit run My_app/navigation_page.py to run the ap


# initialise session state variables
if "stock_searchbox" not in st.session_state or st.session_state["stock_searchbox"] is None:
    st.session_state["stock_searchbox"] = 0


selected = st_searchbox(stock_search_suggestions, placeholder="Type to search for stocks ...", key=st.session_state["stock_searchbox"])
 


if selected is not None: # new selection made
    st.session_state['stock_symbol'] =  str(selected.split(' — ')[0] )
    st.session_state['stock_searchbox'] += 1 
    st.switch_page("stock_page.py")
    st.rerun()







col_left, col_mid, col_right = st.columns([80,10,10])

if col_right.button("refresh"):
    st.cache_data.clear()
    st.rerun()


st.header("Overview of the stock market today")

# === Indices ===
st.subheader("Indices:")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("S&P 500", "SPY")
with col2:
    stock_box("Dow Jones", "DIA")
with col3:
    stock_box("NASDAQ-100", "QQQ")

st.subheader("Performance of each sector:")

#Technology Sector 
st.subheader("Technology Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Apple Inc.", "AAPL")
with col2:
    stock_box("Microsoft Corp.", "MSFT")
with col3:
    stock_box("NVIDIA Corp.", "NVDA")

# Health Care Sector
st.subheader("Health Care Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("UnitedHealth Group Inc.", "UNH")
with col2:
    stock_box("Johnson & Johnson", "JNJ")
with col3:
    stock_box("Pfizer Inc.", "PFE")

#Financials Sector
st.subheader("Financials Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("JPMorgan Chase & Co.", "JPM")
with col2:
    stock_box("Bank of America Corp.", "BAC")
with col3:
    stock_box("Wells Fargo & Co.", "WFC")

#Consumer Discretionary Sector 
st.subheader("Consumer Discretionary Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Amazon.com Inc.", "AMZN")
with col2:
    stock_box("Tesla Inc.", "TSLA")
with col3:
    stock_box("The Home Depot Inc.", "HD")

#Communication Services Sector 
st.subheader("Communication Services Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Alphabet Inc.", "GOOGL")
with col2:
    stock_box("Meta Platforms Inc.", "META")
with col3:
    stock_box("Netflix Inc.", "NFLX")

# Industrials Sector 
st.subheader("Industrials Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("The Boeing Company", "BA")
with col2:
    stock_box("Caterpillar Inc.", "CAT")
with col3:
    stock_box("Honeywell International Inc.", "HON")

#Consumer Staples Sector 
st.subheader("Consumer Staples Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Procter & Gamble Co.", "PG")
with col2:
    stock_box("The Coca-Cola Company", "KO")
with col3:
    stock_box("Costco Wholesale Corp.", "COST")

#Energy Sector 
st.subheader("Energy Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Exxon Mobil Corp.", "XOM")
with col2:
    stock_box("Chevron Corp.", "CVX")
with col3:
    stock_box("ConocoPhillips", "COP")

# Utilities Sector
st.subheader("Utilities Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("NextEra Energy Inc.", "NEE")
with col2:
    stock_box("Duke Energy Corp.", "DUK")
with col3:
    stock_box("The Southern Company", "SO")

#  Real Estate Sector
st.subheader("Real Estate Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("American Tower Corp.", "AMT")
with col2:
    stock_box("Prologis Inc.", "PLD")
with col3:
    stock_box("Realty Income Corp.", "O")

# Materials Sector 
st.subheader("Materials Sector")
col1, col2, col3 = st.columns(3)
with col1:
    stock_box("Linde plc", "LIN")
with col2:
    stock_box("Nucor Corp.", "NUE")
with col3:
    stock_box("The Sherwin-Williams Company", "SHW")





# use middle baseline , and change color based on positive or negative change
#make teh y axis smaller to zoom in graph use Altair
# create auto refresh every minute during market hours






