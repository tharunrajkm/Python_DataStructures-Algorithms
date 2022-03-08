# RUN LENGTH COMPRESSION ALGORITHM

# The solution below should yield us with a Time and Space complexity of O(n).
# use of indices in a string


def compress(s):
    r = ""
    l = len(s)
    
    #Two edge cases for l=0 and l=1
    if l == 0:
        return r

    if l == 1:
        return s+ "1"

    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i+=1
    
    r = r + s[i-1] + str(cnt)
    return r

print(compress('AAAAABBBBCCCC'))
print(compress(''))
print(compress('AAABCCDDDDD'))
print(compress('C'))
