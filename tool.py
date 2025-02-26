import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    """Fetch historical stock data for the given ticker."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")  # Get past 1-month data
    
    if hist.empty:
        return "Invalid ticker symbol or no data available."
    
    # Save the stock trend as an image
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist['Close'], label=f"{ticker} Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Trend")
    plt.legend()
    plt.savefig("stock_trend.png")
    
    return f"Stock data fetched for {ticker}. See 'stock_trend.png'."
