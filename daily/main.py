import pandas as pd
from utils.api import *
from utils.targets import *
from utils.gap_percent import *
from utils.date_helpers import *
from utils.data_2_minute import *
from utils.finviz import *
from utils.ft import *
from utils.r_and_s import *
from utils.eq_cam import *
from utils.next_r4_s4 import *
from numerize_denumerize import numerize
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

    fifty_two_week_h, fifty_two_week_l = get_fifty_two_week_h_l(
        ticker)
    print(
        f"fifty_two_week_h: {fifty_two_week_h}, fifty_two_week_l: {fifty_two_week_l}")

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

    tight_r6 = get_tight_r6(prev_r6, today_r6)
    tight_s6 = get_tight_s6(prev_s6, today_s6)
    print(f"tight_r6: {tight_r6}, tight_s6: {tight_s6}")

    next_day = get_next_day()
    print(f"next_day: {next_day}")

    next_c, next_h, next_l, next_o, next_v, next_vw, next_n = get_custom_day_data(
        ticker=ticker, day=next_day)
    print(f"next_c: {next_c}, next_h: {next_h}, next_l: {next_l}, next_o: {next_o}, next_v: {next_v}, next_vw: {next_vw}, next_n: {next_n}")

    total_range_percent = get_total_range_percent(ticker, today)
    print(f"total_range_percent: {total_range_percent}")

    gap_percent = get_gap_percent(today_o, prev_c)
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

    next_h_timestamp,next_l_timestamp = get_misc_2_min_data_regular_market(ticker, next_day)
    print(f"next_h_timestamp {next_h_timestamp} next_l_timestamp {next_l_timestamp}")

    next_premarket_h, next_premarket_l = get_next_premarket_h_l(ticker, next_day)
    print(f"next_premarket_h {next_premarket_h} next_premarket_l {next_premarket_l}")
    
    next_r4 = get_next_r4(next_premarket_h, today_r4)
    print(f"next_r4 {next_r4}")
    next_s4 = get_next_s4(next_premarket_l, today_s4)
    print(f"next_s4 {next_s4}")

    last_H_eq_cam = get_last_H_eq_cam(
        today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, next_h)
    print(f"last_H_eq_cam {last_H_eq_cam}")
    last_L_eq_cam = get_last_L_eq_cam(
        today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, next_l)
    print(f"last_L_eq_cam {last_L_eq_cam}")
    fifty_two_week_H_eq_cam = get_fifty_two_week_H_eq_cam(
        today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, fifty_two_week_l)
    print(f"fifty_two_week_H_eq_cam {fifty_two_week_H_eq_cam}")
    fifty_two_week_L_eq_cam = get_fifty_two_week_L_eq_cam(
        today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, fifty_two_week_l)
    print(f"fifty_two_week_L_eq_cam {fifty_two_week_L_eq_cam}")



    if highest_v_timestamp:
        highest_v_timestamp = convert_millis_to_local_time(
            highest_v_timestamp)
    if premarket_h_timestamp:
        premarket_h_timestamp = convert_millis_to_local_time(
            premarket_h_timestamp)
    if premarket_l_timestamp:
        premarket_l_timestamp = convert_millis_to_local_time(
            premarket_l_timestamp)
    if regular_market_h_timestamp:
        regular_market_h_timestamp = convert_millis_to_local_time(
            regular_market_h_timestamp)
    if regular_market_l_timestamp:
        regular_market_l_timestamp = convert_millis_to_local_time(
            regular_market_l_timestamp)
    if next_h_timestamp:
        next_h_timestamp = convert_millis_to_local_time(next_h_timestamp)
    if next_l_timestamp:
        next_l_timestamp = convert_millis_to_local_time(next_l_timestamp)

    if prev_day:
        prev_day = convert_YYYY_MM_DD_to_MM_DD_YYYY(prev_day)
    if today:
        today = convert_YYYY_MM_DD_to_MM_DD_YYYY(today)
    if list_date:
        list_date = convert_YYYY_MM_DD_to_MM_DD_YYYY(list_date)
    if next_day:
        next_day = convert_YYYY_MM_DD_to_MM_DD_YYYY(next_day)

    if market_cap:
        market_cap = numerize.numerize(market_cap,currency="$")

    if prev_c:
        prev_c = "$"+str(round(prev_c, 2))
    if prev_h:
        prev_h = "$" + str(round(prev_h, 2))
    if prev_l:
        prev_l = "$" + str(round(prev_l, 2))
    if prev_o:
        prev_o = "$" + str(round(prev_o, 2))
    if prev_vw:
        prev_vw = "$" + str(round(prev_vw, 2))
    if prev_v:
        #if prev_v is 2000000, then prev_v = 2,000,000
        prev_v = "{:,}".format(prev_v)
    if prev_n:
        prev_n = "{:,}".format(prev_n)
    if prev_r3:
        prev_r3 = "$" + str(round(prev_r3, 2))
    if prev_r4:
        prev_r4 = "$" + str(round(prev_r4, 2))
    if prev_r6:
        prev_r6 = "$" + str(round(prev_r6, 2))
    if prev_s3:
        prev_s3 = "$" + str(round(prev_s3, 2))
    if prev_s4:
        prev_s4 = "$" + str(round(prev_s4, 2))
    if prev_s6:
        prev_s6 = "$" + str(round(prev_s6, 2))

    if today_c:
        today_c = "$" + str(round(today_c, 2))
    if today_h:
        today_h = "$" + str(round(today_h, 2))
    if today_l:
        today_l = "$" + str(round(today_l, 2))
    if today_o:
        today_o = "$" + str(round(today_o, 2))
    if today_vw:
        today_vw = "$" + str(round(today_vw, 2))
    if today_v:
        today_v = "{:,}".format(today_v)
    if today_n:
        today_n = "{:,}".format(today_n)
    if today_r3:
        today_r3 = "$" + str(round(today_r3,2))
    if today_r4:
        today_r4 = "$" + str(round(today_r4,2))
    if today_r6:
        today_r6 = "$" + str(round(today_r6,2))
    if today_s3:
        today_s3 = "$" + str(round(today_s3,2))
    if today_s4:
        today_s4 = "$" + str(round(today_s4,2))
    if today_s6:
        today_s6 = "$" + str(round(today_s6,2))
    
    if fifty_two_week_h:
        fifty_two_week_h = "$" + str(round(fifty_two_week_h, 2))
    if fifty_two_week_l:
        fifty_two_week_l = "$" + str(round(fifty_two_week_l, 2))

    if next_c:
        next_c = "$" + str(round(next_c, 2))
    if next_h:
        next_h = "$" + str(round(next_h, 2))
    if next_l:
        next_l = "$" + str(round(next_l, 2))
    if next_o:
        next_o = "$" + str(round(next_o, 2))
    if next_vw:
        next_vw = "$" + str(round(next_vw, 2))
    if next_v:
        next_v = "{:,}".format(next_v)
    if next_n:
        next_n = "{:,}".format(next_n)

    if premarket_v_cumulative:
        premarket_v_cumulative = "{:,}".format(premarket_v_cumulative)
    if premarket_h:
        premarket_h = "$" + str(round(premarket_h, 2))
    if premarket_l:
        premarket_l = "$" + str(round(premarket_l, 2))
    if daily_volume_forecast:
        daily_volume_forecast = "{:,}".format(daily_volume_forecast)
    if first_hour_v:
        first_hour_v = "{:,}".format(first_hour_v)
    if highest_v:
        highest_v = "{:,}".format(highest_v)
    if highest_v_n:
        highest_v_n = "{:,}".format(highest_v_n)
    if aggregate_v_before_highest_v:
        aggregate_v_before_highest_v = "{:,}".format(aggregate_v_before_highest_v)
    if share_class_shares_outstanding:
        share_class_shares_outstanding = "{:,}".format(share_class_shares_outstanding)

    if gap_percent:
        gap_percent = str(round(gap_percent, 2)) + "%"
    if total_range_percent:
        total_range_percent = str(round(total_range_percent, 2)) + "%"
    if daily_ft_percent:
        daily_ft_percent = str(round(daily_ft_percent, 2)) + "%"
    if pm_ft_percent:
        pm_ft_percent = str(round(pm_ft_percent, 2)) + "%"
    if first_hour_ft_percent:
        first_hour_ft_percent = str(round(first_hour_ft_percent, 2)) + "%"

    try:
        data = {
            'today': today,
            'name': name,
            'ticker': ticker,
            'primary_exchange': primary_exchange,
            'list_date': list_date,
            'market_cap': market_cap,
            'today_c': today_c,
            'today_h': today_h,
            'today_l': today_l,
            'today_o': today_o,
            'today_v': today_v,
            'today_vw': today_vw,
            'today_n': today_n,
            'today_r3': today_r3,
            'today_r4': today_r4,
            'today_r6': today_r6,
            'today_s3': today_s3,
            'today_s4': today_s4,
            'today_s6': today_s6,
            'prev_day': prev_day,
            'prev_c': prev_c,
            'prev_h': prev_h,
            'prev_l': prev_l,
            'prev_o': prev_o,
            'prev_v': prev_v,
            'prev_vw': prev_vw,
            'prev_n': prev_n,
            'prev_r3': prev_r3,
            'prev_r4': prev_r4,
            'prev_r6': prev_r6,
            'prev_s3': prev_s3,
            'prev_s4': prev_s4,
            'prev_s6': prev_s6,
            'tight_r6': tight_r6,
            'tight_s6': tight_s6,
            '52W High': fifty_two_week_h,
            '52W Low': fifty_two_week_l,
            'Candle Pattern':None,
            'STRAT Method':None,
            'ATR 14 Days':atr,
            'next_day': next_day,
            'next_c': next_c,
            'next_h': next_h,
            'next_l': next_l,
            'next_o': next_o,
            'next_v': next_v,
            'next_vw': next_vw,
            'next_n': next_n,
            'next_h_time': next_h_timestamp,
            'next_l_time': next_l_timestamp,
            'R4 Premarket':next_r4,
            'S4 Premarket':next_s4,
            'last_H_eq_cam': last_H_eq_cam,
            'last_L_eq_cam': last_L_eq_cam,
            '52W_H_eq_cam': fifty_two_week_H_eq_cam,
            '52W_L_eq_cam': fifty_two_week_L_eq_cam,
            'Next Earning Date': None,
            'Total Range %': total_range_percent,
            'Gap %': gap_percent,        
            'Premarket Volume (cumm)': premarket_v_cumulative,
            'Premarket High': premarket_h,
            'Premarket High Time': premarket_h_timestamp,
            'Premarket Low': premarket_l,
            'Premarket Low Time': premarket_l_timestamp,
            'Premarket Range %':premarket_range_percent,
            'Daily Volume Forecast': daily_volume_forecast,
            'First Hour Volume': first_hour_v,
            'Regular Market High Time':regular_market_h_timestamp,
            'Regular Market Low Time':regular_market_l_timestamp,
            'Highest Volume Time': highest_v_timestamp,
            'Highest Volume Time - num_trans': highest_v_n,
            'Highest Volume':highest_v,
            'Aggregated Volume Before Highest Volume': aggregate_v_before_highest_v,
            'Highest Bar Volume Ratio %': highest_bar_v_ratio_percent,
            'Target 0%': target_0,
            'Target 25%': target_25,
            'Target 50%': target_50,
            'Target 75%': target_75,
            'Target 100%': target_100,
            'share_class_shares_outstanding': share_class_shares_outstanding,
            'Daily FT %': daily_ft_percent,
            'PM FT %': pm_ft_percent,
            'First Hour FT %': first_hour_ft_percent,
        }
        row = pd.DataFrame([data])
        df = pd.concat([df, row])
        # check if the master csv exists and if it does then append to it
        # with open('master.csv', 'a') as f:
        #     row.to_csv(f, header=False, index=False)

    except:
        print("Error in concat")
    


# write to excel with a sheet number for the date
today = get_today()
today = convert_YYYY_MM_DD_to_MM_DD_YYYY(today)
# if file exists then append the sheet
filename = os.getenv('filename')
if os.path.exists(filename):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
        #if sheet exists then delete it
        if today in writer.book.sheetnames:
            idx = writer.book.sheetnames.index(today)
            writer.book.remove(writer.book.worksheets[idx])
        df.to_excel(writer, sheet_name=today, index=False)
else:
    df.to_excel(filename, sheet_name=today, index=False)



    