def count_bits(n):
    a = 0
    answer = 0
    while 2**a <= n:
        a += 1
    a -=1
    while n != 0:
        if 2**a <= n:
            n-=2**a
            a-=1
            answer+=1
        else:
            a-=1
    return answer