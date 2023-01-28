def get_next_r4(premarket_h,today_r4):
    if premarket_h and today_r4:
        if premarket_h>=today_r4:
            return True
        else:
            return False
    else:
        print(f"Error in get_next_r4: premarket_h={premarket_h}, today_r4={today_r4}")
        return None
def get_next_s4(premarket_l,today_s4):
    if premarket_l and today_s4:
        if premarket_l<=today_s4:
            return True
        else:
            return False
    else:
        print(f"Error in get_next_s4: premarket_l={premarket_l}, today_s4={today_s4}")
        return None