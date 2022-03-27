from typing import List

'''
    Link: https://leetcode.com/problems/boats-to-save-people/
    Purpose: Find the minimum number of boats to carry every given person where each boat can carry a max weight of "limit".
           : Each boat carries at most two people at the same time. The sum of the weight of those people is at most "limit"
    parameter: List[int] people - an integer array where people[i] is the weight of the ith person
             : int - limit - a limit of the boat
    return: int iteration - the minimum number of boats to carry every given person
    Pre-Condition: 1 <= people.length <= 5 * 104
                   : 1 <= people[i] <= limit <= 3 * 104
    Post-Condition: none
'''
# runtime: O(nlog(n)), memory: O(1)
# greedy always want to carry 2 person (use all rooms in the boat)
def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    iteration = 0

    # can the boat carries 2 person
    while i <= j:
        firstPerson = people[i]
        secondPerson = people[j]
        if firstPerson >= limit:
            # cannot carries 2 person
            iteration += 1
        else:
            # may have a space for a second person
            if firstPerson + secondPerson <= limit:
                # can carries 2 person
                iteration += 1
                j -= 1
            else:
                # cannot carries 2 person
                iteration += 1
        i += 1

    return iteration


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(numRescueBoats([1], 1)) # 1
    print(numRescueBoats([1,2], 3)) # 1
    print(numRescueBoats([1,2,2], 3)) # 2
    print(numRescueBoats([3,2,2,1], 3)) # 3
    print(numRescueBoats([3,5,3,4], 5)) # 4
    print(numRescueBoats([5,1,4,2], 6)) # 2

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
