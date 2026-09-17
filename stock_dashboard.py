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

    price_history = fetch_weekly_price_history(symbol)
    st.header("chart")
    price_history=price_history.rename_axis('Date').reset_index()
    candle_stick_chart=go.Figure(data=[go.Candlestick(x=price_history['Date'], 
                                   open=price_history['Open'], 
                                   high=price_history['High'], 
                                   low=price_history['Low'], 
                                   close=price_history['Close'])])
    candle_stick_chart.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(candle_stick_chart, use_container_width=True)

    quarterly_financials = fetch_quarterly_financials(symbol)
    annual_financials = fetch_annual_financials(symbol)

    st.header("Financials")

    selection = st.segmented_control(
        label="period",
        options=["Quarterly", "Annual"],
        default="Quarterly"
    )

    if selection == "Quarterly":
        quarterly_financials = quarterly_financials.rename_axis('Quarter').reset_index()
        quarterly_financials["Quarter"] = quarterly_financials["Quarter"].astype(str)

        revenue_chart = alt.Chart(quarterly_financials).mark_bar(color='red').encode(
            x=alt.X("Quarter:N", title="Quarter"),
            y=alt.Y("Total Revenue:Q", title="Revenue")
        )

        st.altair_chart(revenue_chart, use_container_width=True)

        netincome_chart = alt.Chart(quarterly_financials).mark_bar(color='blue').encode(
            x=alt.X("Quarter:N", title="Quarter"),
            y=alt.Y("Net Income:Q", title="Net Income")
    )

        st.altair_chart(netincome_chart, use_container_width=True)


    if selection == "Annual":
        annual_financials = annual_financials.rename_axis('Year').reset_index()
        annual_financials["Year"] = annual_financials["Year"].astype(str).transform(
            lambda year: year.split('-')[0]
        )

        revenue_chart = alt.Chart(annual_financials).mark_bar(color='yellow').encode(
            x=alt.X("Year:N", title="Year"),
            y=alt.Y("Total Revenue:Q", title="Revenue")
        )

        st.altair_chart(revenue_chart, use_container_width=True)

        netincome_chart = alt.Chart(annual_financials).mark_bar(color='pink').encode(
            x=alt.X("Year:N", title="Year"),
            y=alt.Y("Net Income:Q", title="Net Income")
        )

        st.altair_chart(netincome_chart, use_container_width=True)