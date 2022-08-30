from typing import List

def arrayPairSum_M1(nums: List[int]) -> int:
    ans = 0
    nums.sort()
    i = 0
    j = 1
    while j < len(nums):
        ans += min(nums[i], nums[j])
        i += 2
        j += 2

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(arrayPairSum_M1([1,4,3,2])) # 4
    print(arrayPairSum_M1([6,2,6,5,1,2])) # 9
    print(arrayPairSum_M1([1, 4])) # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
