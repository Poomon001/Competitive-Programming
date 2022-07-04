from typing import List

'''
    Link: https://leetcode.com/problems/maximum-units-on-a-truck/
    Purpose: Find the maximum total number of units that can be put on the truck.   : 
    parameter: List[List[int]] boxTypes - [number Of Boxes, number Of Units Per Box]
             : int truckSize - the maximum number of boxes that can be put on the truck   
    return: int maxUnits - the maximum total number of units that can be put on the truck.
    Pre-Condition: 1 <= boxTypes.length <= 1000
                 : 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
                 : 1 <= truckSize <= 106
    Post-Condition: none
'''

# runtime: average - O(nlog(n)), worse - O(nm); where n = len(boxType) and m = sum(numberOfUnitsPerBox)
# memory: O(1)
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    maxUnits = 0
    i = 0

    # addding units to the track
    while i < len(boxTypes) and truckSize > 0:
        numberOfBoxes = boxTypes[i][0]
        numberOfUnitsPerBox = boxTypes[i][1]

        # the box is available, the add it to the truck
        if numberOfBoxes > 0:
            truckSize -= 1
            boxTypes[i][0] = boxTypes[i][0] - 1
            maxUnits += numberOfUnitsPerBox
        else:
            i += 1

    return maxUnits

if __name__ == "__main__":
    print(maximumUnits([[1,3],[2,2],[3,1]], 4)) # 8
    print(maximumUnits([[1, 3], [2, 2], [3, 1]], 3)) # 7
    print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)) # 91
    print(maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 20)) # 115



