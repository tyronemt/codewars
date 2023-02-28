def to_camel_case(text):
    
    if "-" in text:
        text = text.replace("-",",")
    if "_" in text:
        text = text.replace("_",",")
    temp = text.split(",")
    result = ""
    for i in range(len(temp)):
        if i == 0:
            result += temp[i]
        else:
            result += temp[i][0].upper() + temp[i][1::]
    return result