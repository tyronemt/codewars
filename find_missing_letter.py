def find_missing_letter(chars):
    prev = ord(chars[0])
    for i in chars[1:]:
        if ord(i) != prev + 1:
            return chr(prev+1)
        prev = ord(i)
    
