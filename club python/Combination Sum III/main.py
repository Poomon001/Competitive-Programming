from typing import List

'''
    Link: https://leetcode.com/problems/combination-sum-iii/
    Purpose: Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
           : Only numbers 1 through 9 are used.
           : Each number is used at most once.
           : Not allow swap position of the same combination
    Parameter: int k - an integer
             : int n - an integer
    return: List[List[int]] combinations - all valid combinations of k numbers that sum up to n
    Pre-Condition: 2 <= k <= 9
                 : 1 <= n <= 60
    Post-Condition: runtime under O(n^2)
'''
# backtracking: runtime - O(k digits pick 9 * k), memory - (k digits pick 9 * k) -> from combination
def combinationSum3(k: int, n: int) -> List[List[int]]:
    combinations = []
    nums = [num for num in range(1, 10)]

    def backtrack(n, combination, remain):
        if len(combination) == k and remain == 0:
            combinations.append(combination[:]) # O(k)
            return

        for i in range(n, len(nums)):
            combination.append(nums[i])
            backtrack(i + 1, combination, remain - nums[i])
            combination.pop()

    backtrack(0, [], n)
    return combinations


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(combinationSum3(k=3, n=7)) # [[1, 2, 4]]
    print(combinationSum3(k=3, n=9)) # [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    print(combinationSum3(k=4, n=30)) # [[6, 7, 8, 9]]
    print(combinationSum3(k=7, n=30)) # [[1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 7, 8]]
    print(combinationSum3(k=4, n=1)) # []
    print(combinationSum3(k=1, n=5))  # [[5]]
