# candles_row = pd.DataFrame(
#     columns=['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Patterns'])
# candles_row.loc[0] = [prev_day, ticker, prev_o, prev_h, prev_l, prev_c, '']
# candles_row.loc[1] = [today, ticker,
#                       today_o, today_h, today_l, today_c, '']
# candles_row.loc[2] = [next_day, ticker, next_o, next_h, next_l, next_c, '']
# # concat the rows to candles_df
# candles_df = pd.concat([candles_df, candles_row], ignore_index=True)
# # sort the candles_df by date and ticker
# candles_df = candles_df.sort_values(by=['Date'])
# # drop duplicates
# candles_df = candles_df.drop_duplicates(
#     subset=['Date', 'Ticker'], keep='last')
# # reset the index
# candles_df = candles_df.reset_index(drop=True)
# patterns_df = candles_df.sort_values(by=['Ticker', 'Date'])
# # new df for each ticker
# ticker_df = patterns_df[patterns_df['Ticker'] == ticker]
# # take the last 3 rows
# ticker_df = ticker_df.tail(3)
# #drop patterns column
# ticker_df = ticker_df.drop(columns=['Patterns'])
# #reset index
# ticker_df = ticker_df.reset_index(drop=True)
# ticker_df = pattern.all_patterns(ticker_df, single=True)
# print(f"ticker_df \n {ticker_df}")
# # go through the ticker_df and update the candles_df
# for index, row in ticker_df.iterrows():
#     candles_df.loc[(candles_df['Date'] == row['Date']) & (
#         candles_df['Ticker'] == row['Ticker']), 'Patterns'] = row['Patterns']
