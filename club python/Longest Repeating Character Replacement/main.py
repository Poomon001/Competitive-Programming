# This is a sample Python script.
from collections import defaultdict

'''
    Link: https://leetcode.com/problems/longest-repeating-character-replacement/
    Purpose: find the longest common character in a string. you can replace a character with an y character k times
    Parameter:  string s - a string
             : int - an integer
    return: int ans - the longest common character in a string
    Pre-Condition: 1 <= s.length <= 105
                 : s consists of only uppercase English letters.
                 : 0 <= k <= s.length
    Post-Condition: None
'''
# sliding window - runtime: O(n), memory: O(1)
def characterReplacement(s: str, k: int) -> int:
    # tips: we can expand window as long as we the window_size <= k + max_fre_char
    count = defaultdict(int)
    left = 0
    maxFreq = 0
    ans = 0

    for right in range(len(s)):
        count[s[right]] += 1
        maxFreq = max(maxFreq, count[s[right]])

        while (right - left + 1) > k + maxFreq:
            count[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(characterReplacement("AABABBA", 1)) # 4
    print(characterReplacement("ABAB", 2))  # 4
    print(characterReplacement("ABAB", 0))  # 1
    print(characterReplacement("Z", 1))  # 4
    print(characterReplacement("ABABACCCCCA", 2))  # 7
    print(characterReplacement("AAAA", 3))  # 4

