import math

def make_readable(seconds):
    
    h = str(math.floor(seconds / 3600))
    m = str(math.floor((seconds % 3600) / 60))
    s = str(seconds - (int(h) * 3600) - (int(m) * 60))
    
    lst = [h,m,s]
    result = ""
    for i in lst:
        if len(i) < 2:
            result += "0" + i
        else:
            result += i
        result += ":"
    return result[:-1]