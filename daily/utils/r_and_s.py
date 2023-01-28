def get_pp(c, h, l):
    pp = None
    if c and h and l:
        pp = (c + h + l) / 3
    else:
        print(f"Error: get_pp() - c: {c}, h: {h}, l: {l}")
    return pp


def get_r4(c, h, l):
    r4 = None
    if c and h and l:
        r4 = c + ((h - l)*(1.1/2))
    else:
        print(f"Error: get_r4() - c: {c}, h: {h}, l: {l}")
    return r4


def get_r3(c, h, l):
    r3 = None
    if c and h and l:
        r3 = c + ((h - l)*(1.1/4))
    else:
        print(f"Error: get_r3() - c: {c}, h: {h}, l: {l}")
    return r3


def get_r6(c, h, l):
    r6 = None
    if c and h and l:
        r6 = c*(h/l)
    else:
        print(f"Error: get_r6() - c: {c}, h: {h}, l: {l}")
    return r6


def get_s4(c, h, l):
    s4 = None
    if c and h and l:
        s4 = c - ((h - l)*(1.1/2))
    else:
        print(f"Error: get_s4() - c: {c}, h: {h}, l: {l}")
    return s4


def get_s3(c, h, l):
    s3 = None
    if c and h and l:
        s3 = c - ((h - l)*(1.1/4))
    else:
        print(f"Error: get_s3() - c: {c}, h: {h}, l: {l}")
    return s3


def get_s6(c, h, l):
    s6 = None
    if c and h and l:
        s6 = (c - (h / l * c - c))
    else:
        print(f"Error: get_s6() - c: {c}, h: {h}, l: {l}")
    return s6


def get_tight_r6(prev_r6, today_r6):
    if prev_r6 and today_r6:
        return True if prev_r6 >= today_r6 else False
    else:
        print(
            f"Error: get_tight_r6() - prev_r6: {prev_r6}, today_r6: {today_r6}")
        return None


def get_tight_s6(prev_s6, today_s6):
    if prev_s6 and today_s6:
        return True if prev_s6 <= today_s6 else False
    else:
        print(
            f"Error: get_tight_s6() - prev_s6: {prev_s6}, today_s6: {today_s6}")
        return None
