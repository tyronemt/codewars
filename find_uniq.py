def find_uniq(arr):
    # your code here
    prev = arr[0]
    if prev != arr[1] and prev != arr[2]:
        return prev
    for i in arr[1:]:
        if prev != i:
            return i
   