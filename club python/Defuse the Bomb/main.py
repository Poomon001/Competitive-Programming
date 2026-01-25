from typing import List

'''
    Link: https://leetcode.com/problems/defuse-the-bomb/
    Purpose: Given list of number 'code', find the number as following
        - If k > 0, replace the ith number with the sum of the next k numbers.
        - If k < 0, replace the ith number with the sum of the previous k numbers.
        - If k == 0, replace the ith number with 0.
    parameter: List[int] code - a list of number
             : int k - an integer
    return: List[int] ans - a list of results
    Pre-Condition: n == code.length
                 : 1 <= n <= 100
                 : 1 <= code[i] <= 100
                 : -(n - 1) <= k <= n - 1
    Post-Condition: none
'''
def decrypt(code: List[int], k: int) -> List[int]:
    # [5,7,1,4], k = 3
    #    i   j
    # [5,7,1,4], k = -2
    #      i j
    ans = [0] * len(code)
    left = 0
    right = k
    if k < 0:
        left = len(code) + k - 1
        right = len(code) - 1

    total = sum(code[left:right])
    for i in range(len(code)):
        total = total - code[left] + code[right]
        right = (right + 1) % len(code)
        left = (left + 1) % len(code)
        ans[i] = total
        i += 1

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(decrypt([5,7,1,4], k=3)) # [12, 10, 16, 13]
    print(decrypt([5, 7, 1, 4], k=-3))  # [12, 10, 16, 13]
    print(decrypt([5, -7, 1, -4], k=2)) # [-6, -3, 1, -2]
    print(decrypt([5, 7, 1, 4], k=0)) # [0, 0, 0, 0]
    print(decrypt([2, 4, 9, 3], k=-2)) # [12, 5, 6, 13]
    print(decrypt([5, 6, 2, 3, 1, -1], k=1)) # [6, 2, 3, 1, -1, 5]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
