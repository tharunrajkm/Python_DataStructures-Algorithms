#My method  
def rev_word(s):
    s = s.strip().split() #Once split strip is not required, learnt later see Method 1 and 2
    new_s = []
    for i in reversed(s):
        new_s.append(i)
    
    return ' '.join(new_s)

# print(rev_word('    space before'))
# print(rev_word('Hi John,   are you ready to go?'))






# Solution 1 and 2 from course but not for interviews
def rev_word1(s):
    return ' '.join(reversed(s.split()))

# print(rev_word1('    space before'))
# print(rev_word1('Hi John,   are you ready to go?'))

                #Or#

def rev_word2(s):
    return ' '.join((s.split())[::-1])

# print(rev_word2('    space before'))
# print(rev_word2('Hi John,   are you ready to go?'))



# Solution 3 from course for inteviews
# Manually splitting on spaces and converting to lists and reversing and joining.

def rev_word3(s):
    words = []
    length = len(s)
    spaces = [" "]

    #index count
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1

    return words      

def final_output(words):
    arr = rev_word3(words)
    rev = len(arr)
    rev_list = []
    for wrd in arr:
        rev = rev - 1
        rev_list.append(arr[rev])

    rev_sen = ' '.join(rev_list)  

    return rev_sen
            
            
print(final_output('    space before'))
print(final_output('Hi John,   are you ready to go?'))



