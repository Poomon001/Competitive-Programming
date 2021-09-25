from typing import List

li1 = ["fol", "flower", "flow", "fly", "flown"] #f
li2 = ["flower", "flow", "fly", "flown"] #fl
li3 = ["flower", "flow", "fly", "cat" ,"flown"] #""

'''
    Link: https://leetcode.com/problems/longest-common-prefix/
    Purpose: find the longest common prefix string amongst an array of strings.
    parameter: array - contains words
    return: string - longest common prefix
    Pre-Condition: only lower-case English letters.
                 : number of words is between 1 and 200
                 : number of chars in a word is between 0 and 200
    Post-Condition: none
'''

# this is solution 1. Solution 2 is in java
def commonLongestPrefix(words: List[str]) -> str:
    globalLongestPrefix = words[0]
    for word in words:
        currLongestPrefix = ""
        j = 0
        for char in word:
            # reach the end of globalLongestPrefix, then exit
            if(j == len(globalLongestPrefix)):
                break

            # Add char to currLongestPrefix if the char match the current globalLongestPrefix char
            if (char == globalLongestPrefix[j]):
                currLongestPrefix = currLongestPrefix + char
                j += 1

            # found an unmatching character break out of the loop, then exit
            else:
                break

        # update globalLongestPrefix
        globalLongestPrefix = currLongestPrefix
    return globalLongestPrefix

print(commonLongestPrefix(li1))
print(commonLongestPrefix(li2))
print(commonLongestPrefix(li3))


