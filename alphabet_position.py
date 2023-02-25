def alphabet_position(text):
    result = ""
    for i in text:
        temp = ord(i)
        if temp >= 97 and temp <= 122:
            temp -= 96
            result += str(temp)
            result += " "
        elif temp >= 65 and temp <= 90:
            temp -= 64
            result += str(temp)
            result += " "
    return result[:-1]