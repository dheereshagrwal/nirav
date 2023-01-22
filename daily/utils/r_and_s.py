def get_r4(c, h, l):
    r4 = c + ((h - l)*(1.1/2))
    return r4


def get_r5(c, h, l):
    r5 = c + ((h - l)*(0.865))
    return r5


def get_r6(c, h, l):
    r6 = c*(h/l)
    return r6


def get_s4(c, h, l):
    s4 = c - ((h - l)*(1.1/2))
    return s4


def get_s5(c, h, l):
    s5 = c - ((h - l)*(0.865))
    return s5


def get_s6(c, h, l):
    s6 = (c - (h / l * c - c))
    return s6


def get_tight_r6(prev_r6, curr_r6):
    return True if prev_r6 >= curr_r6 else False

def get_tight_s6(prev_s6, curr_s6):
    return True if curr_s6 >= prev_s6 else False