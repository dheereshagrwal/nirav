def get_gap_percent(today_o, prev_c):
    if today_o and prev_c:
        gap_percent = 100*(today_o - prev_c)/prev_c
        return gap_percent
    else:
        print(f"Error in get_gap_percent: today_o={today_o}, prev_c={prev_c}")
    return None
