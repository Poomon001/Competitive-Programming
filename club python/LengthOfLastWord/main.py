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
def lengthOfLastWord(s: str) -> int:
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

if __name__ == '__main__':
    print(lengthOfLastWord("H x ")) # 1
    print(lengthOfLastWord("Hello World")) # 5
    print(lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord("luffy is still joyboy"))  # 6
    print(lengthOfLastWord("   fly me   to   the moon  "))  # 4

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
