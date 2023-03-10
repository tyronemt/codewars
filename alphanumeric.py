def alphanumeric(password):
    if password == "":
        return False
    for i in password:
        if not (ord('z') >= ord(i) >= ord('a') or ord('Z') >= ord(i) >= ord('A') or ord('9') >= ord(i) >= ord('0')) :
            print(i)
            return False
    return True