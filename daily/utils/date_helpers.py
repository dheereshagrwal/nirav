from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd


def get_timestamp(date, time):
    date = date + " " + time
    date = pd.to_datetime(date)
    date = date.timestamp()
    date = date * 1000
    return int(date)


load_dotenv()


def get_today():
    try:
        today = os.getenv("today")
        return today
    except:
        print("today not found in .env file, exiting...")
        exit()


def get_prev_day():
    try:
        prev_day = os.getenv("prev_day")
        return prev_day
    except:
        print("prev_day not found in .env file, exiting...")
        exit()
def get_next_day():
    try:
        next_day = os.getenv("next_day")
        return next_day
    except:
        print("next_day not found in .env file, exiting...")
        exit()

def convert_millis_to_local_time(millis):
    #I want only the local time, not the date
    time = datetime.fromtimestamp(millis/1000).strftime("%H:%M:%S")
    return time


def convert_seconds_to_utc_date(seconds):
    #convert to utc not to local time
    return datetime.utcfromtimestamp(seconds).strftime('%Y-%m-%d')

def convert_YYYY_MM_DD_to_MM_DD_YYYY(date):
    return datetime.strptime(date, '%Y-%m-%d').strftime('%m-%d-%Y')