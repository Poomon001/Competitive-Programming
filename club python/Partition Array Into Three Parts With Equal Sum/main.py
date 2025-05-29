from typing import List

'''
    Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
    Purpose: Determine if an int array can be split into 3 parts where:
           : Each part must be non-empty
           : Each part must have equal sum
           : Each part must perform the int sum in their original order (Dont need to consider different order sum) 
    parameter: List[int] - array integer
    return: bool - true if can split into exact 3 partitions and meet all above conditions. Otherwise, false.
    Pre-Condition: 3 <= arr.length <= 5 * 10^4
                 : -10^4 <= arr[i] <= 10^4
    Post-Condition: none
'''
# Two pointers - runtime: O(n), complexity: O(1)
def canThreePartsEqualSum_M1(arr: List[int]) -> bool:
    totalSum = sum(arr)
    partial = totalSum // 3

    i = 0
    j = len(arr) - 1
    xSum = arr[i]
    ySum = arr[j]

    # reserve at least one middle index for third partition
    while i < j - 1:
        zSum = totalSum - (xSum + ySum)
        if xSum == ySum == zSum:
            return True
        if xSum != partial:
            # work on first partition
            i += 1
            xSum += arr[i]
        else:
            # work on second partition
            j -= 1
            ySum += arr[j]
    return False

'''
    Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
    Purpose: Determine if an int array can be split into 3 parts where:
           : Each part must be non-empty
           : Each part must have equal sum
           : Each part must perform the int sum in their original order (Dont need to consider different order sum) 
    parameter: List[int] - array integer
    return: bool - true if can split into exact 3 partitions and meet all above conditions. Otherwise, false.
    Pre-Condition: 3 <= arr.length <= 5 * 10^4
                 : -10^4 <= arr[i] <= 10^4
    Post-Condition: none
'''
# Greedy - runtime: O(n), complexity: O(1)
def canThreePartsEqualSum_M2(arr: List[int]) -> bool:
    partial = sum(arr) / 3  # leave it in decimal
    partitionCount = 0
    currSum = 0
    for num in arr:
        currSum += num
        if currSum == partial:
            currSum = 0
            partitionCount += 1

        if partitionCount == 3:
            return True

    return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(canThreePartsEqualSum_M1([0,2,1,-6,6,-7,9,0,2,0,1])) # False
    print(canThreePartsEqualSum_M1([0,2,1,-6,6,7,9,-1,2,0,1])) # False
    print(canThreePartsEqualSum_M1([3,3,6,5,-2,2,5,1,-9,4])) # True
    print(canThreePartsEqualSum_M1([0,2,1,-6,6,-7,9,1,2,0,1])) # True
    print(canThreePartsEqualSum_M1([18,12,-18,18,-19,-1,10,10])) # True
    print(canThreePartsEqualSum_M1([1,-1,1,-1])) # False
    print(canThreePartsEqualSum_M1([12,10,10,10])) # False
    print(canThreePartsEqualSum_M1([1,1,1,1])) # False

    print("\n === Solution 2 === \n")
    print(canThreePartsEqualSum_M2([0, 2, 1, -6, 6, -7, 9, 0, 2, 0, 1]))  # False
    print(canThreePartsEqualSum_M2([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))  # False
    print(canThreePartsEqualSum_M2([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))  # True
    print(canThreePartsEqualSum_M2([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))  # True
    print(canThreePartsEqualSum_M2([18, 12, -18, 18, -19, -1, 10, 10]))  # True
    print(canThreePartsEqualSum_M2([1, -1, 1, -1]))  # False
    print(canThreePartsEqualSum_M2([12, 10, 10, 10]))  # False
    print(canThreePartsEqualSum_M2([1, 1, 1, 1]))  # False
