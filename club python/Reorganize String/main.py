import heapq
from collections import Counter

'''
    Link: https://leetcode.com/problems/reorganize-string
    Purpose: Rearrange the characters of s so that any two adjacent characters are not the same.
           : Return "" if not possible.
    parameter: str s - a string
    return: str ans - a resulted string
    Pre-Condition: 1 <= s.length <= 500
                 : s consists of lowercase English letters.
    Post-Condition: none
'''
# max heap - runtime: O(nlog26), memory(O(26))
def reorganizeString(s: str) -> str:
    # build rearrangement with max_heap by freqency
    # if there is an adjacent duplicate use the next freqency

    char_to_freq = Counter(s)
    max_heap = []
    ans = ""

    for c, freq in char_to_freq.items():
        heapq.heappush(max_heap, (-freq, c))

    while max_heap:
        first_freq, first_c = heapq.heappop(max_heap)
        if ans == "" or ans[-1] != first_c:
            ans = ans + first_c
            first_freq += 1
        else:
            if not max_heap:
                return ""
            second_freq, second_c = heapq.heappop(max_heap)
            ans = ans + second_c
            second_freq += 1
            if second_freq < 0:
                heapq.heappush(max_heap, (second_freq, second_c))
        if first_freq < 0:
            heapq.heappush(max_heap, (first_freq, first_c))

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reorganizeString("aab")) # "aba"
    print(reorganizeString("aaab")) # ""
    print(reorganizeString("vvvlo")) # "vlvov"
    print(reorganizeString("vvvlov")) # ""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
