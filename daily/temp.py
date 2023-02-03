from datetime import datetime, timedelta
import requests
def get_response(url):
    response = requests.get(url)
    return response

def get_fifty_two_week_h_l(ticker):
    today = '2023-01-26'
    #from_time is today - 1 year from today not prev_day
    from_time = datetime.strptime(today, '%Y-%m-%d') - timedelta(days=365)
    from_time = from_time.strftime('%Y-%m-%d')
    to_time = today
    print(f"from_time: {from_time}")
    print(f"to_time: {to_time}")
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/year/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey=i4FD6ltLyeM_7fLvcb7JtaJpifMG5D6M")
    fifty_two_week_h = None
    fifty_two_week_l = None
    try:
        results = resp.json()["results"]
        fifty_two_week_h = results[0]["h"]
        fifty_two_week_l = results[0]["l"]
    except:
        pass
    return fifty_two_week_h, fifty_two_week_l

print(get_fifty_two_week_h_l('AAPL'))