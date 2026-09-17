# Stock Market Dashboard

A simple interactive stock market dashboard built with Python, Streamlit, yfinance, Altair, and Plotly.

The dashboard allows users to enter a stock symbol and view company information, historical stock prices, and financial performance through interactive charts.

## Features

* Enter a stock symbol such as AAPL, MSFT, or GOOGL
* View basic company information:

  * Company name
  * Market capitalization
  * Sector
* View one year of weekly stock price history
* Interactive candlestick chart showing:

  * Open price
  * High price
  * Low price
  * Close price
* View financial data
* Switch between:

  * Quarterly financials
  * Annual financials
* Revenue charts
* Net income charts
* Data caching using Streamlit to reduce repeated API requests

## Technologies Used

* Python
* Streamlit
* yfinance
* Plotly
* Altair

## How It Works

The application uses the `yfinance` library to retrieve stock market and financial data.

The user enters a stock ticker:

```text
AAPL
```

The application then retrieves the corresponding information from Yahoo Finance and displays it in the dashboard.

The data is divided into three main sections:

### 1. Company Information

Displays basic information about the selected company, including its name, market capitalization, and sector.

### 2. Stock Price Chart

The application retrieves one year of weekly stock data and displays it as a candlestick chart using Plotly.

The chart shows:

* Open
* High
* Low
* Close

### 3. Financials

Financial information can be viewed using the Quarterly/Annual selector.

The dashboard displays:

* Total Revenue
* Net Income

Bar charts are created using Altair.

## Project Structure

```text
Stock Market Dashboard/
│
├── stock_dashboard.py
└── README.md
```

## Installation

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <your-repository-link>
```

Move into the project folder:

```bash
cd "Stock Market Dashboard"
```

Install the required libraries:

```bash
pip install yfinance streamlit altair plotly
```

## Running the Project

Run the following command:

```bash
streamlit run stock_dashboard.py
```

Streamlit will open the dashboard in your browser.

If it does not open automatically, copy the local URL shown in the terminal and open it in your browser.

## Example Stock Symbols

You can try:

```text
AAPL
MSFT
GOOGL
AMZN
TSLA
NVDA
```

For Indian stocks, you can use Yahoo Finance ticker symbols such as:

```text
RELIANCE.NS
TCS.NS
INFY.NS
HDFCBANK.NS
```

## Caching

The project uses Streamlit's caching feature:

```python
@st.cache_data
```

This prevents the application from repeatedly requesting the same data when possible, making the dashboard more efficient.

## Important Note

The financial and stock market data is retrieved from Yahoo Finance through `yfinance`.

This project is intended for educational and demonstration purposes. The displayed information should not be considered financial advice.

## Future Improvements

Possible improvements include:

* Add stock search suggestions
* Add daily/monthly/yearly time periods
* Add technical indicators such as moving averages
* Add stock comparison
* Add P/E ratio and other financial metrics
* Add dividend information
* Add downloadable financial data
* Add portfolio tracking
* Add financial ratios and valuation analysis
* Improve dashboard design and responsiveness

## Author

Spandan Wasnik


GitHub: `spandan-wasnik`
