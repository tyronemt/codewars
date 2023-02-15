def longest_consec(strarr, k):
    # your code
    lst = []
    max = 0
    result = ""
    if k ==0 :
        return result
    for i in strarr:
        if len(lst) < k:
            lst.append(i)
        
        if len(lst) == k:
            temp = ''.join(lst)
            if len(temp) > max:
                result = temp
                max = len(temp)
            lst.pop(0)
            
    return result