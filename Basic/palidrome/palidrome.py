def palindrome(txt):
    # input to string
    txt = str(txt)
    # case sensivity
    txt = txt.lower()
    # remove all spaces from the string. (in case if string have spaces)
    txt = txt.replace(" ", "")
    # remove special characters
    txt = "".join(l for l in txt if l.isalnum())
    # checking if string is a palindrome through slicing
    if txt == txt[::-1]:
        return True
    else:
        return False