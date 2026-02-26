import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    # historical market data
    df = stock.history(period="1y")

    return df


def save_data(df, ticker):
    filename = f"{ticker}_stock_data.csv"
    df.to_csv(filename)
    print(f"Saved data to {filename}")


if __name__ == "__main__":
    ticker = "AAPL"   # Apple stock
    data = get_stock_data(ticker)
    save_data(data, ticker)