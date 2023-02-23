def accum(s):
    # your code
    result = ""
    mult = 0
    for i in s:
        result += i.upper()
        result += i.lower() * mult
        mult+=1
        result += "-"
    return result[:-1]