from typing import List
from collections import Counter
'''
    Link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
    Purpose: Find the least number of unique integers after removing exactly k elements.
    parameter: List[int] arr - an array of integer
             : int k - the number of elements to remove from arr
    return: int ans - the least number of unique integers after removing exactly k elements.
    Pre-Condition: 1 <= arr.length <= 10^5
                 : 1 <= arr[i] <= 10^9
                 : 0 <= k <= arr.length
    Post-Condition: none
'''

# runtime: O(nlogn), memory: O(n)
def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    intToFreq = Counter(arr)
    ans = 0

    sortedIntToFreq = dict(sorted(intToFreq.items(), key=lambda x: x[1]))

    for value in sortedIntToFreq.values():
        k = k - value
        if k < 0:
            ans += 1
    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findLeastNumOfUniqueInts([5,5,4], 1)) # 1
    print(findLeastNumOfUniqueInts([5, 5, 4], 0)) # 2
    print(findLeastNumOfUniqueInts([5, 5, 4], 3)) # 0
    print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)) # 2
    print(findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 2)) # 2
    print(findLeastNumOfUniqueInts([1, 1, 1, 1, 1], 3)) # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
