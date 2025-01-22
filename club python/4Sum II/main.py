from collections import Counter
from typing import List

'''
    Link: https://leetcode.com/problems/4sum-ii/
    Purpose: Find the number of tuples that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 
           : (count all duplicates tuples eg. (1, 1, -1, -1), (-1, 1, -1, 1), and (-1, -1, 1, 1) is 3)
    parameter: List[int] nums1 - a list of integer with length n
             : List[int] nums2 - a list of integer with length n
             : List[int] nums3 - a list of integer with length n
             : List[int] nums4 - a list of integer with length n
    return: int ans - the number of tuples that satisfies the above mentioned condition
    Pre-Condition: n == nums1.length    
                 : n == nums2.length
                 : n == nums3.length
                 : n == nums4.length
                 : 1 <= n <= 200
                 : -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
    Post-Condition: none
'''
# brute force - runtime: O(n^4), memory: O(1)
def fourSumCount_M1(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    ans = 0
    for a in nums1:
        for b in nums2:
            for c in nums3:
                for d in nums4:
                    if a + b + c + d == 0:
                        ans += 1

    return ans

'''
    Link: https://leetcode.com/problems/4sum-ii
    Purpose: Find the number of tuples that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 
           : (count all duplicates tuples eg. (1, 1, -1, -1), (-1, 1, -1, 1), and (-1, -1, 1, 1) is 3)
    parameter: List[int] nums1 - a list of integer with length n
             : List[int] nums2 - a list of integer with length n
             : List[int] nums3 - a list of integer with length n
             : List[int] nums4 - a list of integer with length n
    return: int ans - the number of tuples that satisfies the above mentioned condition
    Pre-Condition: n == nums1.length    
                 : n == nums2.length
                 : n == nums3.length
                 : n == nums4.length
                 : 1 <= n <= 200
                 : -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
    Post-Condition: none
'''

'''
    fomular: (a + b) = -(c + d)
    we compute all possible combinations of a and b
    we compare them with all possible combinations of c and d to satisfy the above fomular
'''
# using a fomular - runtime: O(n^2), memory: O(n)
def fourSumCount_M2(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    # {a+b, occurance}
    pair = Counter()
    ans = 0

    # compute a+b to get the 1st element in a pair
    for a in nums1:
        for b in nums4:
            s = a + b
            pair.update({a + b: 1})

    # find corresponding eleemnt -(c+d) of the (a+b)
    for c in nums3:
        for d in nums2:
            if -(c + d) in pair:
                ans += pair[-(c + d)]

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== brute force solution ===+\n")
    print(fourSumCount_M1([1, 2], [-2, -1], [-1, 2], [0, 2]))  # 2
    print(fourSumCount_M1([1, 2, 4], [-2, -1, 10], [-1, 2, 10], [0, 2, -1]))  # 4
    print(fourSumCount_M1([0], [0], [0], [0]))  # 1
    print(fourSumCount_M1([1, 2, 1, 2], [-2, -1, -2, -1], [-1, 2, -1, 2], [0, 2, 0, 2]))  # 32
    print(fourSumCount_M1([0, 1, 9, 8, 7, 6], [0, 3, 4, 5, -1, -10], [-1, -3, -4, -5, 7, 23], [0, 1, 2, 3, 4, 5]))  # 34

    print("\n+=== formula solution ===+\n")
    print(fourSumCount_M2([1,2], [-2,-1], [-1,2], [0,2])) # 2
    print(fourSumCount_M2([1, 2, 4], [-2, -1, 10], [-1, 2, 10], [0, 2, -1]))  # 4
    print(fourSumCount_M2([0], [0], [0], [0])) # 1
    print(fourSumCount_M2([1, 2, 1, 2], [-2, -1, -2, -1], [-1, 2, -1, 2], [0, 2, 0, 2]))  # 32
    print(fourSumCount_M2([0,1,9,8,7,6], [0,3,4,5,-1,-10], [-1,-3,-4,-5, 7, 23], [0,1,2,3,4,5])) # 34

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
