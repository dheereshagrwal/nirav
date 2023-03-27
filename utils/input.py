import pandas as pd
def input_data():
    ticker_dict = {}
    try:
        df = pd.read_excel("input.xlsx")
        for index, row in df.iterrows():
            #get today from today column
            today = str(row['today'].date())
            #get prev day from prev day column
            prev_day = str(row['prev_day'].date())
            #get next day from next day column
            next_day = str(row['next_day'].date())
            #get ticker from ticker column
            ticker = row['ticker']
            #check if any of the values is empty
            if not today or not prev_day or not next_day or not ticker:
                print('Empty values in input_data(), Exiting...')
                exit()
            #check if prev_day is not greater than or equal to today
            if prev_day >= today or prev_day >= next_day or today>= next_day:
                print('prev_day >= today or prev_day >= next_day or today>= next_day in input_data(), Exiting...')
                exit()
                
            key = ( prev_day,today,next_day)
            if key in ticker_dict:
                ticker_dict[key].append(ticker)
            else:
                ticker_dict[key] = [ticker]
        return ticker_dict
    except Exception as e:
        print(e,'Error in input_data(), Exiting...')
        exit()
        