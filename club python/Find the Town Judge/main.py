from typing import List

'''
    Link: https://leetcode.com/problems/find-the-town-judge/
    Purpose: Find the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
           : If the town judge exists, then:
                1. The town judge trusts nobody.
                2. Everybody (except for the town judge) trusts the town judge.
                3. There is exactly one person that satisfies properties 1 and 2.
    parameter: List[List[int]] trust - a list of pair [a, b] where "a" person trusts "b" person
             : int n - a town population
    return: int - The label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
    Pre-Condition: 1 <= n <= 1000
                 : 0 <= trust.length <= 10^4
                 : trust[i].length == 2
                 : All the pairs of trust are unique.
                 : a != b
                 : 1 <= a, b <= n
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def findJudge(n: int, trust: List[List[int]]) -> int:
    # {person, numbere of trusts by others}
    trustCounter = {i: 0 for i in range(1, n + 1)}

    # a list of person who trusts someone
    trustSomeone = set()

    # count trust from all person
    for t in trust:
        person = t[0]
        trustedPerson = t[1]
        trustSomeone.add(person)
        trustCounter[trustedPerson] += 1

    # check judge conditions
    for person, trust in trustCounter.items():
        # n - 1 because everyone trust a judge but a judge trust nobody
        if trust == n - 1:
            # check if the judge trusts nobody
            if person in trustSomeone:
                continue
            return person

    return -1


if __name__ == '__main__':
    print(findJudge(n = 2, trust = [[1,2]])) # 2
    print(findJudge(n = 3, trust = [[1,3],[2,3]])) # 3
    print(findJudge(n=3, trust=[[1,3],[2,3],[3,1]])) # -1
    print(findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3
