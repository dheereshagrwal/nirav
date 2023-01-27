from finvizfinance.quote import finvizfinance


def get_finviz_data(ticker):
    shs_float = None
    atr = None
    try:
        stock = finvizfinance(ticker)
        ticker_fundament = stock.ticker_fundament()
        shs_float = ticker_fundament["Shs Float"]
        atr = ticker_fundament["ATR"]
    except:
        pass
    return shs_float, atr
