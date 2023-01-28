import pandas as pd
from candlestick_patterns import candlestick


def get_candle_df(prev_day, prev_o, prev_h, prev_l, prev_c, today, today_o, today_h, today_l, today_c, next_day, next_o, next_h, next_l, next_c):
    df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close'])
    df.loc[0] = (prev_day, prev_o, prev_h, prev_l, prev_c)
    df.loc[1] = (today, today_o, today_h, today_l, today_c)
    df.loc[2] = (next_day, next_o, next_h, next_l, next_c)
    return df


def get_candle_patterns(prev_day, prev_o, prev_h, prev_l, prev_c, today, today_o, today_h, today_l, today_c, next_day, next_o, next_h, next_l, next_c):
    candle_df = get_candle_df(prev_day, prev_o, prev_h, prev_l, prev_c, today,
                              today_o, today_h, today_l, today_c, next_day, next_o, next_h, next_l, next_c)
    dic = candlestick.check_all_patterns(candle_df)
    patterns = []
    for key, df in dic.items():
        if df[key][1] == True:
            patterns.append(key)
    return patterns
