# Given two strings, check to see if they are anagrams. 
# An anagram is when the two strings can be written using the exact same letters (so you can just rearrange 
# the letters to get a different phrase or word).

# For example:
# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"
# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

#Solution1 o(n) time and space

def anagram(s1,s2):
    s1 = "".join(s1.lower().split())
    s2 = "".join(s2.lower().split())

    if len(s1) != len(s2):
        return False

    counter = {}
    for letter in s1: #O(n)
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in s2: #O(n)
        if letter in counter:
            counter[letter] -= 1
        else:
            return False

    for letter in counter: #O(n)
        if counter[letter] != 0:
            return False

    return True
    pass





print(anagram('dog','god'))
print(anagram('Clint eastwood','old west aCtion'))
print(anagram('aa','bb'))



#Solution2 O(nlogn) time and O(1) space for sorting

# 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)
def anagram2(s1,s2):
    s1 = "".join(s1.lower().split())
    s2 = "".join(s2.lower().split())
    
    return sorted(s1) == sorted(s2)

print(anagram2('dog','god'))
print(anagram2('Clint eastwood','old west aCtion'))
print(anagram2('aa','bb'))