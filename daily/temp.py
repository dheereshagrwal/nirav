#create a dataframe with column names of Date, Open, High, Low, Close, Volume
import pandas as pd
df = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume'])
#add some data to the dataframe for candlestick chart
df.loc[0] = ['2018-01-01', 100, 110, 90, 100, 1000]
df.loc[1] = ['2018-01-02', 110, 120, 100, 110, 2000]
df.loc[2] = ['2018-01-03', 120, 130, 110, 120, 3000]
df.loc[3] = ['2018-01-04', 130, 140, 120, 130, 4000]

