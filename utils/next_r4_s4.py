def get_next_r4(next_premarket_h,today_r4):
    if next_premarket_h and today_r4:
        if next_premarket_h>=today_r4:
            return True
        else:
            return False
    else:
        print(f"Error in get_next_r4: next_premarket_h={next_premarket_h}, today_r4={today_r4}")
        return None
def get_next_s4(next_premarket_l,today_s4):
    if next_premarket_l and today_s4:
        if next_premarket_l<=today_s4:
            return True
        else:
            return False
    else:
        print(f"Error in get_next_s4: next_premarket_l={next_premarket_l}, today_s4={today_s4}")
        return None