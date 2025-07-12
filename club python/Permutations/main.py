from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    #                                []
    #         [1]                    [2]                   [3]
    #   [1, 2]    [1, 3]       [2,1]    [2,3]         [3,1]   [3,2]
    # [1, 2, 3]  [1, 3, 2]   [2,1,3]    [2,3,1]       [3,1,2] [3,2,1]
    permutations = []

    def backtrack(permutation):
        if len(permutation) == len(nums):
            permutations.append(permutation[:])
            return

        for i in range(len(nums)):
            if nums[i] not in permutation:
                permutation.append(nums[i])
                backtrack(permutation)
                permutation.pop()

    backtrack([])
    return permutations


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(permute([1, 2, 3, 4])) # [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    print(permute([1,2,3])) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(permute([1,2])) # [[1, 2], [2, 1]]
    print(permute([1])) # [[1]]
