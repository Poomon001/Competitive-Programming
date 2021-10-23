from typing import List

'''     
    Link: https://leetcode.com/problems/group-anagrams/
    Purpose: Group the anagrams together.
    Parameter: List[str] strs - a list of strings
    Returns: List[List[str]] - a list of group of anagrams
    Pre-Condition: 1 <= strs.length <= 104
                 : 0 <= strs[i].length <= 100
                 : strs[i] consists of lowercase English letters.
    Post-Condition: none
'''
# sort + hashmap: runtime: O(n*mlog(m)), memory: O(n); n is a number of word and m is a number of max chars
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # hashmap {str sortedString: str[] result}
    dic = {}
    ans = []

    # Group by finding a matching sorted String
    for i, s in enumerate(strs):
        sort = "".join(sorted(s))

        # if dic at the key(sorted string) is empty, create new group
        if not dic.get(sort):
            dic[sort] = [s]
        # find a matching sorted string, push to the existing group
        else:
            dic[sort].append(s)

    # get the answer
    for block in dic.values():
        ans.append(block)

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(groupAnagrams(["a"])) # [['a']]
    print(groupAnagrams([""])) # [['']]
    print(groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])) # [['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
