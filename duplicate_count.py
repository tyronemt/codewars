from collections import defaultdict

def duplicate_count(text):
    # Your code goes here
    d = defaultdict(int)
    result = 0
    for i in text:
       d[i.lower()] += 1
    for i in d.values():
        if i > 1:
            result+=1
    
    return result

