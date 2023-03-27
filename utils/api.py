from datetime import timedelta
from utils.date_helpers import *
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv("apiKey")


def get_response(url):
    response = requests.get(url)
    return response


def get_ticker_info(ticker):
    resp = get_response(
        f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apiKey}")
    name = None
    ticker = None
    primary_exchange = None
    list_date = None
    market_cap = None
    share_class_shares_outstanding = None
    try:
        result = resp.json()["results"]
    except:
        return name, ticker, primary_exchange, list_date, market_cap, share_class_shares_outstanding
    # absolute fields - name, ticker
    name = result["name"]
    ticker = result["ticker"]
    try:
        primary_exchange = result["primary_exchange"]
    except:
        pass
    try:
        list_date = result["list_date"]
    except:
        pass
    try:
        market_cap = result["market_cap"]
    except:
        pass
    try:
        share_class_shares_outstanding = result["share_class_shares_outstanding"]
    except:
        pass
    return name, ticker, primary_exchange, list_date, market_cap, share_class_shares_outstanding


def get_custom_day_data(ticker, day):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{day}/{day}?adjusted=true&sort=asc&apiKey={apiKey}")
    c, h, l, o, v, vw, n = None, None, None, None, None, None, None
    try:
        results = resp.json()["results"]
    except:
        return c, h, l, o, v, vw, n
    result = results[0]
    c = result["c"]
    h = result["h"]
    l = result["l"]
    o = result["o"]
    v = result["v"]
    try:
        vw = result["vw"]
    except:
        pass
    try:
        n = result["n"]
    except:
        pass
    return c, h, l, o, v, vw, n


def get_2_minute_data(ticker, from_time, to_time):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/2/minute/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey={apiKey}")
    results = None
    try:
        results = resp.json()["results"]
    except:
        pass
    return results


def get_fifty_two_week_h_l(ticker, today):
    from_time = today
    to_time = today
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/year/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey={apiKey}")
    fifty_two_week_h = None
    fifty_two_week_l = None
    try:
        results = resp.json()["results"]
        fifty_two_week_h = results[0]["h"]
        fifty_two_week_l = results[0]["l"]
    except:
        pass
    return fifty_two_week_h, fifty_two_week_l
