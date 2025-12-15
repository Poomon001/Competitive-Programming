# This is a sample Python script.
from collections import defaultdict


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
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
