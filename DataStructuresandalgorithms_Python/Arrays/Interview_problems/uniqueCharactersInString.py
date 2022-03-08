

#Method 1 using set datastructure(not for interview)
def uni_char1(s):
    return len(set(s)) == len(s)

# print(uni_char1('goo'))
# print(uni_char1(('abcdefg')))

# Method 2 (for interview)

def uni_char2(s):
    chars = set()
    
    for i in s:
        if i in chars:
            return False
        else:
            chars.add(i)
    return True


print(uni_char2('goo'))
print(uni_char2(('abcdefg')))







# My method ( O(N) time and space complexity)
def uni_char(s):
    r = ""
    l = len(s)
    i = 0

    if l == 0:
        return True

    while i < l:
        if s[i] in r:
            return False
        else:
            r = r + s[i]
        i += 1
    return True

# print(uni_char('goo'))
# print(uni_char(('abcdefg')))
