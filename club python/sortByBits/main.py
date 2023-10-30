from typing import List
'''
    Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2023-10-30
    Purpose: Sort an interger by the number of 1 in its binary representation. Break the even by the value of the original.
    parameter: List[int] - integer list
    return: List[int] - a sorted list by the specifications
    Pre-Condition: 1 <= arr.length <= 500
                 : 0 <= arr[i] <= 10^4
    Post-Condition: none
'''

# note: the counting of binary length is bounded by 14 bits, thus O(1)
# runtime - O(nlogn), memory - O(1)
def sortByBits(arr: List) -> List:
    arr.sort(key=lambda a: (str(bin(a)).count('1'), a))
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sortByBits([0,1,2,3,4,5,6,7,8])) # [0, 1, 2, 4, 8, 3, 5, 6, 7]
    print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1])) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    print(sortByBits([1])) # [1]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
