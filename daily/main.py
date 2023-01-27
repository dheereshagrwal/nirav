import pandas as pd
import os
from utils.api import *
from utils.targets import *
from utils.misc import *
from utils.date_helpers import *
from utils.data_2_minute import *
from utils.finviz import *
from utils.ft import *
from utils.r_and_s import *
from dotenv import load_dotenv
from numerize_denumerize import numerize
load_dotenv()
try:
    file = open("tickers.txt", "r")
    tickers = file.readlines()
    file.close()
    # remove whitespace  from each ticker
    tickers = [x.strip().upper() for x in tickers]
except:
    print('tickers.txt does not exist, quitting....')
    exit()

df = pd.DataFrame()
for ticker in tickers:
    print(f"ticker: {ticker}")

    name, ticker, primary_exchange, list_date, market_cap, share_class_shares_outstanding = get_ticker_info(
        ticker)
    print(f"name: {name}, ticker: {ticker}, primary_exchange: {primary_exchange}, list_date: {list_date}, market_cap: {market_cap}, share_class_shares_outstanding: {share_class_shares_outstanding}")

    prev_day = get_prev_day()
    print(f"prev_day: {prev_day}")

    prev_c, prev_h, prev_l, prev_o, prev_v, prev_vw, prev_n = get_custom_day_data(
        ticker=ticker, day=prev_day)
    print(f"prev_c: {prev_c}, prev_h: {prev_h}, prev_l: {prev_l}, prev_o: {prev_o}, prev_v: {prev_v}, prev_vw: {prev_vw}, prev_n: {prev_n}")

    prev_r3 = get_r3(prev_c, prev_h, prev_l)
    prev_r4 = get_r4(prev_c, prev_h, prev_l)
    prev_r6 = get_r6(prev_c, prev_h, prev_l)
    prev_s3 = get_s3(prev_c, prev_h, prev_l)
    prev_s4 = get_s4(prev_c, prev_h, prev_l)
    prev_s6 = get_s6(prev_c, prev_h, prev_l)
    print(f"prev_r3: {prev_r3}, prev_r4: {prev_r4}, prev_r6: {prev_r6}, prev_s3: {prev_s3}, prev_s4: {prev_s4}, prev_s6: {prev_s6}")

    tight_r6 = get_tight_r6(prev_c, prev_h, prev_l)
    tight_s6 = get_tight_s6(prev_c, prev_h, prev_l)
    print(f"tight_r6: {tight_r6}, tight_s6: {tight_s6}")

    fifty_two_week_high, fifty_two_week_low = get_fifty_two_week_high_low(
        ticker)
    print(
        f"fifty_two_week_high: {fifty_two_week_high}, fifty_two_week_low: {fifty_two_week_low}")
    
    today = get_today()
    print(f"today: {today}")

    today_c, today_h, today_l, today_o, today_v, today_vw, today_n = get_custom_day_data(
        ticker=ticker, day=today)
    print(f"today_c: {today_c}, today_h: {today_h}, today_l: {today_l}, today_o: {today_o}, today_v: {today_v}, today_vw: {today_vw}, today_n: {today_n}")

    today_r3 = get_r3(today_c, today_h, today_l)
    today_r4 = get_r4(today_c, today_h, today_l)
    today_r6 = get_r6(today_c, today_h, today_l)
    today_s3 = get_s3(today_c, today_h, today_l)
    today_s4 = get_s4(today_c, today_h, today_l)
    today_s6 = get_s6(today_c, today_h, today_l)
    print(f"today_r3: {today_r3}, today_r4: {today_r4}, today_r6: {today_r6}, today_s3: {today_s3}, today_s4: {today_s4}, today_s6: {today_s6}")

    next_day = get_next_day()
    print(f"next_day: {next_day}")

    next_c, next_h, next_l, next_o, next_v, next_vw, next_n = get_custom_day_data(
        ticker=ticker, day=next_day)
    print(f"next_c: {next_c}, next_h: {next_h}, next_l: {next_l}, next_o: {next_o}, next_v: {next_v}, next_vw: {next_vw}, next_n: {next_n}")

    
    total_range_percent = get_total_range_percent(ticker,today)
    print(f"total_range_percent: {total_range_percent}")
    
    gap_percent = get_gap_percent(ticker)
    print(f"gap_percent: {gap_percent}")

    premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast = get_misc_2_min_data_premarket(
        ticker, today)
    print(f"premarket_v_cumulative: {premarket_v_cumulative}, premarket_h: {premarket_h}, premarket_h_timestamp: {premarket_h_timestamp}, premarket_l: {premarket_l}, premarket_l_timestamp: {premarket_l_timestamp}, premarket_range_percent: {premarket_range_percent}, daily_volume_forecast: {daily_volume_forecast}")

    first_hour_v = get_misc_2_min_data_first_hour(ticker, today)
    print(f"first_hour_v: {first_hour_v}")

    regular_market_h_timestamp, regular_market_l_timestamp = get_misc_2_min_data_regular_market(
        ticker, today)
    print(
        f"regular_market_h_timestamp: {regular_market_h_timestamp}, regular_market_l_timestamp: {regular_market_l_timestamp}")
    
    highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent = get_misc_2_min_data_till_3_58(
        ticker, today)
    print(f"highest_v_timestamp: {highest_v_timestamp}, highest_v_n: {highest_v_n}, highest_v: {highest_v}, aggregate_v_before_highest_v: {aggregate_v_before_highest_v}, highest_bar_v_ratio_percent: {highest_bar_v_ratio_percent}")

    abs_h, abs_h_timestamp = get_abs_h(ticker, today)
    print(f"abs_h {abs_h} abs_h_timestamp {abs_h_timestamp}")

    l_after_abs_h = get_l_after_abs_h(abs_h, abs_h_timestamp, ticker, today)
    print(f"l_after_abs_h {l_after_abs_h}")

    target_0, target_25, target_50, target_75, target_100 = get_targets(
        prev_c, abs_h, l_after_abs_h)
    print(f"target_0: {target_0}, target_25: {target_25}, target_50: {target_50}, target_75: {target_75}, target_100: {target_100}")

    shs_float, atr = get_finviz_data(ticker)
    daily_ft_percent = get_daily_ft_percent(today_v, shs_float)
    print(f"daily_ft_percent {daily_ft_percent}")

    pm_ft_percent = get_premarket_ft_percent(premarket_v_cumulative, shs_float)
    print(f"pm_ft_percent {pm_ft_percent}")
    
    first_hour_ft_percent = get_first_hour_ft_percent(first_hour_v, shs_float)
    print(f"first_hour_ft_percent {first_hour_ft_percent}")
