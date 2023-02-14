import os
from dotenv import load_dotenv
load_dotenv()
eq_cam_threshold_percent = float(os.getenv("eq_cam_threshold_percent"))

def is_valid(cam_pp,h_or_l):
    if cam_pp and h_or_l:
        threshold_percent = abs(100*(cam_pp -h_or_l)/h_or_l)
        if threshold_percent <= eq_cam_threshold_percent:
            return True
        else:
            return False
    else:
        print(f"Error in is_valid: cam_pp={cam_pp}, h_or_l={h_or_l}")
        return None
    
def get_last_H_eq_cam(today_r3,today_s3, today_r4,today_s4,today_r6,today_s6,next_h):
    last_H_eq_cam = None
    if not (today_r3 and today_s3 and today_r4 and today_s4 and today_r6 and today_s6 and next_h):
        print(f"Error in get_last_H_eq_cam: today_r3={today_r3}, today_s3={today_s3}, today_r4={today_r4}, today_s4={today_s4}, today_r6={today_r6}, today_s6={today_s6}, next_h={next_h}")
        return last_H_eq_cam 
    if is_valid(today_r3,next_h):
        last_H_eq_cam = 'R3H'
    elif is_valid(today_s3,next_h):
        last_H_eq_cam = 'S3H'
    elif is_valid(today_r4,next_h):
        last_H_eq_cam = 'R4H'
    elif is_valid(today_s4,next_h):
        last_H_eq_cam = 'S4H'
    elif is_valid(today_r6,next_h):
        last_H_eq_cam = 'R6H'
    elif is_valid(today_s6,next_h):
        last_H_eq_cam = 'S6H'
    return last_H_eq_cam

def get_last_L_eq_cam(today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, next_l):
    last_L_eq_cam = None
    if not (today_r3 and today_s3 and today_r4 and today_s4 and today_r6 and today_s6 and next_l):
        print(f"Error in get_last_L_eq_cam: today_r3={today_r3}, today_s3={today_s3}, today_r4={today_r4}, today_s4={today_s4}, today_r6={today_r6}, today_s6={today_s6}, next_l={next_l}")
        return last_L_eq_cam
    if is_valid(today_r3,next_l):
        last_L_eq_cam = 'R3L'
    elif is_valid(today_s3,next_l):
        last_L_eq_cam = 'S3L'
    elif is_valid(today_r4,next_l):
        last_L_eq_cam = 'R4L'
    elif is_valid(today_s4,next_l):
        last_L_eq_cam = 'S4L'
    elif is_valid(today_r6,next_l):
        last_L_eq_cam = 'R6L'
    elif is_valid(today_s6,next_l):
        last_L_eq_cam = 'S6L'
    return last_L_eq_cam

def get_fifty_two_week_H_eq_cam(today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, fifty_two_week_h):
    fifty_two_week_H_eq_cam = None
    if not (today_r3 and today_s3 and today_r4 and today_s4 and today_r6 and today_s6 and fifty_two_week_h):
        print(f"Error in get_fifty_two_week_H_eq_cam: today_r3={today_r3}, today_s3={today_s3}, today_r4={today_r4}, today_s4={today_s4}, today_r6={today_r6}, today_s6={today_s6}, fifty_two_week_h={fifty_two_week_h}")
        return fifty_two_week_H_eq_cam
    if is_valid(today_r3,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'R3H52'
    elif is_valid(today_s3,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'S3H52'
    elif is_valid(today_r4,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'R4H52'
    elif is_valid(today_s4,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'S4H52'
    elif is_valid(today_r6,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'R6H52'
    elif is_valid(today_s6,fifty_two_week_h):
        fifty_two_week_H_eq_cam = 'S6H52'
    return fifty_two_week_H_eq_cam

def get_fifty_two_week_L_eq_cam(today_r3, today_s3, today_r4, today_s4, today_r6, today_s6, fifty_two_week_l):
    fifty_two_week_L_eq_cam = None
    if not (today_r3 and today_s3 and today_r4 and today_s4 and today_r6 and today_s6 and fifty_two_week_l):
        print(f"Error in get_fifty_two_week_L_eq_cam: today_r3={today_r3}, today_s3={today_s3}, today_r4={today_r4}, today_s4={today_s4}, today_r6={today_r6}, today_s6={today_s6}, fifty_two_week_l={fifty_two_week_l}")
        return fifty_two_week_L_eq_cam
    if is_valid(today_r3,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'R3L52'
    elif is_valid(today_s3,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'S3L52'
    elif is_valid(today_r4,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'R4L52'
    elif is_valid(today_s4,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'S4L52'
    elif is_valid(today_r6,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'R6L52'
    elif is_valid(today_s6,fifty_two_week_l):
        fifty_two_week_L_eq_cam = 'S6L52'
    return fifty_two_week_L_eq_cam