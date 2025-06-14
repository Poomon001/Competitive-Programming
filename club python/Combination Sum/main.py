from typing import List

'''
    Link: https://leetcode.com/problems/combination-sum
    Purpose: Find a list of all unique combinations of candidates where the chosen numbers sum to target 
           : and can reuse the same numbers unlimited number of times.
    parameter: List[int] nums - a list of unique numbers
    return: List[List[int]] - all subsets of all unique combinations of candidates.
    Pre-Condition: 1 <= candidates.length <= 30
                 : 2 <= candidates[i] <= 40
                 : All elements of candidates are distinct.
                 : 1 <= target <= 40
    Post-Condition: none
'''
# backtrack - runtime: O(n^t/m), memory: O(t/m) -> we can always branch and reuse candidates but not get target
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    subsets = []

    def backtrack(i, subset, remaining):
        if remaining == 0:
            subsets.append(subset[:])
            return
        elif remaining < 0:
            return

        for j in range(i, len(candidates)):
            subset.append(candidates[j])
            backtrack(j, subset, remaining - candidates[j])
            subset.pop()

    backtrack(0, [], target)
    return subsets


if __name__ == '__main__':
    print(combinationSum([2,3,5], 8)) # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(combinationSum([2, 3, 5], 17)) # [[2, 2, 2, 2, 2, 2, 2, 3], [2, 2, 2, 2, 2, 2, 5], [2, 2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 3, 5], [2, 2, 3, 5, 5], [2, 3, 3, 3, 3, 3], [2, 5, 5, 5], [3, 3, 3, 3, 5]]
    print(combinationSum([2, 3, 5], 10)) # [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5]]
    print(combinationSum([2,3,6,7], 7)) # [[2, 2, 3], [7]]
    print(combinationSum([2, 3, 6, 7], 8)) # [[2, 2, 2, 2], [2, 3, 3], [2, 6]]
    print(combinationSum([2], 1)) # []

