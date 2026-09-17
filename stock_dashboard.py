import yfinance as yf
import streamlit as st
import altair as alt
import plotly.graph_objects as go

@st.cache_data
def fetch_stock_info(symbol):
    stock=yf.Ticker(symbol)
    return stock.info

@st.cache_data
def fetch_quarterly_financials(symbol):
    stock=yf.Ticker(symbol)
    return stock.quarterly_financials.T

@st.cache_data
def fetch_annual_financials(symbol):
    stock=yf.Ticker(symbol)
    return stock.financials.T

@st.cache_data
def fetch_weekly_price_history(symbol):
    stock=yf.Ticker(symbol)
    return stock.history(period="1y", interval="1wk")


st.title('Stock Dashboard')
symbol=st.text_input("Enter a stock symbol (e.g., AAPL, MSFT, GOOGL):")
if symbol:
    information = fetch_stock_info(symbol)

    st.header("Company Information")

    st.subheader(f"Name: {information['longName']}")
    st.subheader(f"Market Cap: ${information['marketCap']:,}")
    st.subheader(f"Sector: {information['sector']}")      