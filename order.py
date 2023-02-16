def order(sentence):
  # code here
    temp = sentence.split(" ")
    lst = []
    result = ""
    for i in temp:
        for char in i:
            if char.isnumeric():
                if int(char) > 0:
                    lst.append((int(char), i))
    lst.sort()
    for i in lst:
        result += i[1] + " "
   
    return result[:-1]