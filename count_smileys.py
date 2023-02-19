def count_smileys(arr):
    valid_eyes = [':', ';']
    valid_nose = ['-', '~']
    valid_smile = [')', 'D']
    
    result = 0
    
    for i in arr:
        l = len(i)
        if i[0] in valid_eyes:
            if l==3:
                if i[1] in valid_nose:
                    if i[2] in valid_smile:
                        result += 1
            else:
                if i[1] in valid_smile:
                    result += 1
    return result #the number of valid smiley faces in array/list