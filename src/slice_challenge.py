def first_4(item):
    str =list(item)
    return str[:4]

def first_and_last_4(item):
    strk =list(item)
    str1 = strk[:4]
    str2 = strk[-4:]
    return str1+str2

def odds(item):
    strk =list(item)
    return strk[1::2]

def reverse_evens(item):
    strk  = list(item)
    strk2 = strk[::2]
    return strk2[::-1]

#print(odds("12345"))
print(reverse_evens("012345"))