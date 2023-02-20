def find_outlier(integers):
    prev = integers[0] % 2
    if prev != integers[1] % 2 and prev != integers[2] % 2:
        return integers[0]
    for i in integers[1:]:
        if i%2 != prev:
            return i
    return None