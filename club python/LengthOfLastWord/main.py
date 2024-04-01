'''
    Link: https://leetcode.com/problems/length-of-last-word/
    Purpose: Find the length of the last word in a string
    parameter: string s - a string
    return: int lastWordCount - a length of the last word
    Pre-Condition: 1 <= s.length <= 104
                 : s consists of only English letters and spaces ' '.
                 : There will be at least one word in s.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def lengthOfLastWord_m1(s: str) -> int:
    # currChar is alphabet then true. if currChar is a space then false
    metAlphabet = False
    lastWordCount = 0

    # search for the last char in the word. When found, start count alphabet until meeting another space
    for i in range(len(s)-1, -1, -1):
        if s[i] == " ":
            # meet a space after meeting an alphabet then exit.
            if metAlphabet == True:
                break
            # meet a space before meeting an alphabet then keep searching
            continue
        else:
            # meet an alphabet then count it
            metAlphabet = True
            lastWordCount += 1

    return lastWordCount

'''
    Link: https://leetcode.com/problems/length-of-last-word/
    Purpose: Find the length of the last word in a string
    parameter: string s - a string
    return: int lastWordCount - a length of the last word
    Pre-Condition: 1 <= s.length <= 104
                 : s consists of only English letters and spaces ' '.
                 : There will be at least one word in s.
    Post-Condition: none
'''
# 2 year later: O(n), memory: O(1)
def lengthOfLastWord_m2(s: str) -> int:
    s = s.strip()
    i = len(s) - 1
    count = 0
    while(i >= 0):
        if s[i] == " ":
            return count
        count += 1
        i -= 1

    return count

if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(lengthOfLastWord_m1("H x ")) # 1
    print(lengthOfLastWord_m1("Hello World")) # 5
    print(lengthOfLastWord_m1("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord_m1("luffy is still joyboy"))  # 6
    print(lengthOfLastWord_m1("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord_m1("helloworld"))  # 10

    print("\n === solution 2 === \n")
    print(lengthOfLastWord_m2("H x "))  # 1
    print(lengthOfLastWord_m2("Hello World"))  # 5
    print(lengthOfLastWord_m2("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord_m2("luffy is still joyboy"))  # 6
    print(lengthOfLastWord_m2("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord_m2("helloworld"))  # 10

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
