from typing import List
def combine_M1(m: int, k: int) -> List[List[int]]:
    combinations = []
    nums = [num for num in range(1, m + 1)]
    def backtrack(n, combination):
        if len(combination) == k:
            combinations.append(combination[:])
            return

        for i in range(n, len(nums)):
            if nums[i] not in combination:
                combination.append(nums[i])
                backtrack(i, combination)
                combination.pop()

    backtrack(0, [])
    return combinations

def combine_M2(m: int, k: int) -> List[List[int]]:
    combinations = []

    def backtrack(n, combination):
        if len(combination) == k:
            combinations.append(combination[:])
            return

        for num in range(n, m + 1):
            if num not in combination:
                combination.append(num)
                backtrack(num + 1, combination)
                combination.pop()

    backtrack(1, [])
    return combinations


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(combine_M1(m=5, k=3)) # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    print(combine_M1(m=4, k=2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(combine_M1(m=2, k=2)) # [[1, 2]]
    print(combine_M1(m=2, k=1)) # [[1], [2]]
    print(combine_M1(m=1, k=1)) # [[1]]

    print("\n === Solution 2 === \n")
    print(combine_M2(m=5,k=3))  # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    print(combine_M2(m=4, k=2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(combine_M2(m=2, k=2))  # [[1, 2]]
    print(combine_M2(m=2, k=1))  # [[1], [2]]
    print(combine_M2(m=1, k=1))  # [[1]]
