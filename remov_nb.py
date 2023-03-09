def remov_nb(n):
    # your code
    total = n * (n + 1) // 2
    t = []
    for i in range(1, n + 1):
        temp = (total - i) // (i + 1) 
        if temp <= n and i * temp == (total - i - temp):
            t.append((i,temp))
    return t