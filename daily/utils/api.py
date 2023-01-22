from utils.date_helpers import *
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv("apiKey")


def get_response(url):
    response = requests.get(url)
    return response


def get_basic_info(ticker):
    resp = get_response(
        f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apiKey}")
    name, ticker, primary_exchange, list_date, market_cap, share_class_shares_outstanding = None, None, None, None, None, None
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


def get_curr_day_data(ticker):
    curr_day = get_curr_day()
    return get_custom_day_data(ticker, curr_day)


def get_prev_day_data(ticker):
    prev_day = get_prev_day()
    return get_custom_day_data(ticker, prev_day)


def get_next_day_data(ticker):
    next_day = get_next_day()
    return get_custom_day_data(ticker, next_day)


def get_2_minute_data(ticker, from_time, to_time):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/2/minute/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey={apiKey}")
    results = None
    try:
        results = resp.json()["results"]
    except:
        pass
    return results

def get_52W_high_and_low(ticker):
    curr_day = get_curr_day()
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/year/{curr_day}/{curr_day}?adjusted=true&sort=asc&apiKey={apiKey}")
    fifty_two_week_high = None
    fifty_two_week_low = None
    try:
        results = resp.json()["results"]
        fifty_two_week_high = results[0]["h"]
        fifty_two_week_low = results[0]["l"]
    except:
        pass
    return fifty_two_week_high, fifty_two_week_low