from collections import deque
from typing import List, Union

class NestedInteger:
    def __init__(self, value: Union[int, List['NestedInteger']] = None):
        if value is None:
            self._data = []
            self._is_int = False
        elif isinstance(value, int):
            self._data = value
            self._is_int = True
        else:
            self._data = value
            self._is_int = False

    def isInteger(self) -> bool:
        return self._is_int

    def add(self, elem: 'NestedInteger'):
        if not self._is_int:
            self._data.append(elem)
        else:
            raise ValueError("Cannot add to an integer NestedInteger")

    def setInteger(self, value: int):
        self._data = value
        self._is_int = True

    def getInteger(self) -> int:
        if self._is_int:
            return self._data
        else:
            return None

    def getList(self) -> List['NestedInteger']:
        if not self._is_int:
            return self._data
        else:
            return None

    def __repr__(self):
        if self.isInteger():
            return f"{self._data}"
        else:
            return f"[{', '.join(repr(x) for x in self._data)}]"

'''
    Link: https://leetcode.com/problems/nested-list-weight-sum/
    Purpose: Find the sum of each integer in nestedList multiplied by its depth
    parameter: List[NestedInteger] nestedList - a list of NestedInteger.
    return: int answer - the sum of each integer in nestedList multiplied by its depth
    Pre-Condition: 1 <= nestedList.length <= 50
                 : The values of the integers in the nested list is in the range [-100, 100].
                 : The maximum depth of any integer is less than or equal to 50.
    Post-Condition: none
'''
# queue: runtime: O(n), memnory: O(n)
def depthSum(nestedList: List[NestedInteger]) -> int:
    queue = deque(nestedList)

    answer = 0
    multi = 1

    while queue:
        temp = deque()
        while queue:
            element = queue.popleft()  # element is NestedInteger, not iterable
            if element.isInteger():
                answer += element.getInteger() * multi
            else:
                temp.extend(element.getList())  # add entire NestedInteger to deque
        multi += 1
        queue = temp
    return answer


if __name__ == "__main__":
    # Example 1: [1,[4,[6]]]
    n1 = NestedInteger(1)
    n6 = NestedInteger(6)
    n4 = NestedInteger(4)
    n_inner = NestedInteger()
    n_inner.add(n6)
    n_list = NestedInteger()
    n_list.add(n4)
    n_list.add(n_inner)
    nestedList = [n1, n_list]

    print("Nested List:", nestedList)
    print("Depth Sum:", depthSum(nestedList))  # Expected: 1*1 + 4*2 + 6*3 = 27

    # Example 2: [ [1,1], 2, [1,1] ]
    n_1a = NestedInteger(1)
    n_1b = NestedInteger(1)
    n_inner1 = NestedInteger()
    n_inner1.add(n_1a)
    n_inner1.add(n_1b)

    n_2 = NestedInteger(2)

    n_1c = NestedInteger(1)
    n_1d = NestedInteger(1)
    n_inner2 = NestedInteger()
    n_inner2.add(n_1c)
    n_inner2.add(n_1d)

    nestedList2 = [n_inner1, n_2, n_inner2]

    print("Nested List 2:", nestedList2)
    print("Depth Sum 2:", depthSum(nestedList2))  # Expected: (1+1)*2 + 2*1 + (1+1)*2 = 10
