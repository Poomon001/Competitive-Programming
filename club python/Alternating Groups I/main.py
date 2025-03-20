from typing import List

'''
    Link: https://leetcode.com/problems/alternating-groups-i
    Purpose: Determine a number of '3 contiguous alternatives'
           : (the middle tile has a different color from its left and right tiles)
           : Note that since colors represents a circle, 
           : the first and the last tiles are considered to be next to each other.
    parameter: List[int] colors - a list of 0 and 1 where they represent different colors
    return: int count - a number of '3 contiguous alternatives'
    Pre-Condition: 3 <= colors.length <= 100
                 : 0 <= colors[i] <= 1
    Post-Condition: none
'''
# real cycle (readable) - runtime: O(n), memory: O(n)
def numberOfAlternatingGroups_M1(colors: List[int]) -> int:
    # 01001 0
    # 01001 01
    colors = [colors[-1]] + colors[:] + [colors[0]]
    count = 0

    for i in range(1, len(colors) - 1):
        if colors[i] != colors[i + 1] and colors[i] != colors[i - 1]:
            count += 1

    return count

'''
    Link: https://leetcode.com/problems/alternating-groups-i
    Purpose: Determine a number of '3 contiguous alternatives'
           : (the middle tile has a different color from its left and right tiles)
           : Note that since colors represents a circle, 
           : the first and the last tiles are considered to be next to each other.
    parameter: List[int] colors - a list of 0 and 1 where they represent different colors
    return: int count - a number of '3 contiguous alternatives'
    Pre-Condition: 3 <= colors.length <= 100
                 : 0 <= colors[i] <= 1
    Post-Condition: none
'''
# psudo cycle (readable) - runtime: O(n), memory: O(1)
def numberOfAlternatingGroups_M2(colors: List[int]) -> int:
    # 01001 0
    # 01001 01
    colors.extend(colors[0:2])
    count = 0

    for i in range(1, len(colors) - 1):
        if colors[i] != colors[i + 1] and colors[i] != colors[i - 1]:
            count += 1

    return count

'''
    Link: https://leetcode.com/problems/alternating-groups-i
    Purpose: Determine a number of '3 contiguous alternatives'
           : (the middle tile has a different color from its left and right tiles)
           : Note that since colors represents a circle, 
           : the first and the last tiles are considered to be next to each other.
    parameter: List[int] colors - a list of 0 and 1 where they represent different colors
    return: int count - a number of '3 contiguous alternatives'
    Pre-Condition: 3 <= colors.length <= 100
                 : 0 <= colors[i] <= 1
    Post-Condition: none
'''
# modulus - runtime: O(n), memory: O(1)
def numberOfAlternatingGroups_M3(colors: List[int]) -> int:
    consideration = len(colors) + 1
    count = 0
    for i in range(consideration + 1):
        # not head or tail
        if i > 0 and i < consideration:
            i = i % len(colors)
            j = (i + 1) % len(colors)
            k = (i - 1) % len(colors)
            if colors[i] != colors[j] and colors[i] != colors[k]:
                count += 1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n=== Solution 1 ===\n")
    print(numberOfAlternatingGroups_M1([1, 1, 1])) # 0
    print(numberOfAlternatingGroups_M1([1, 0, 1])) # 1
    print(numberOfAlternatingGroups_M1([0, 0, 1])) # 1
    print(numberOfAlternatingGroups_M1([0, 0, 0, 1])) # 1
    print(numberOfAlternatingGroups_M1([1, 0, 0, 0])) # 1
    print(numberOfAlternatingGroups_M1([0, 1, 0, 1])) # 4
    print(numberOfAlternatingGroups_M1([0, 1, 0, 0, 1])) # 3

    print("\n=== Solution 2 ===\n")
    print(numberOfAlternatingGroups_M2([1, 1, 1]))  # 0
    print(numberOfAlternatingGroups_M2([1, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M2([0, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M2([0, 0, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M2([1, 0, 0, 0]))  # 1
    print(numberOfAlternatingGroups_M2([0, 1, 0, 1]))  # 4
    print(numberOfAlternatingGroups_M2([0, 1, 0, 0, 1]))  # 3

    print("\n=== Solution 3 ===\n")
    print(numberOfAlternatingGroups_M3([1, 1, 1]))  # 0
    print(numberOfAlternatingGroups_M3([1, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M3([0, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M3([0, 0, 0, 1]))  # 1
    print(numberOfAlternatingGroups_M3([1, 0, 0, 0]))  # 1
    print(numberOfAlternatingGroups_M3([0, 1, 0, 1]))  # 4
    print(numberOfAlternatingGroups_M3([0, 1, 0, 0, 1]))  # 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
