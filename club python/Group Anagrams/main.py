from typing import List
from collections import defaultdict
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
def groupAnagrams_M1(strs: List[str]) -> List[List[str]]:
    # {sorted String, []}
    hash_to_ans = defaultdict(list)
    for s in strs:
        sorted_s = "".join(sorted(s))
        hash_to_ans[sorted_s].append(s)

    return [value for key, value in hash_to_ans.items()]

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
# tuple + hashmap: runtime: O(n*m), memory: O(n); n is a number of word and m is a number of max chars
def groupAnagrams_M2(strs: List[str]) -> List[List[str]]:
    # {tuple, []}
    pattern_to_ans = defaultdict(list)

    for word in strs:
        alph_counter = [0 for _ in range(26)]
        for c in word:
            i = ord(c) - ord('a')
            alph_counter[i] += 1

        tuple_alph_counter = tuple(alph_counter)
        pattern_to_ans[tuple_alph_counter].append(word)

    return [value for key, value in pattern_to_ans.items()]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(groupAnagrams_M1(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(groupAnagrams_M1(["a"])) # [['a']]
    print(groupAnagrams_M1([""])) # [["","",""],["ead","ade","ead"],["qwer"]]
    print(groupAnagrams_M1(["", "", "", "ead", "ade", "ead", "qwer"]))  # [['']]
    print(groupAnagrams_M1(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])) # [['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]

    print("\n === Solution 2 === \n")
    print(groupAnagrams_M2(
        ["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(groupAnagrams_M2(["a"]))  # [['a']]
    print(groupAnagrams_M2([""]))  # [["","",""],["ead","ade","ead"],["qwer"]]
    print(groupAnagrams_M2(["", "", "", "ead", "ade", "ead", "qwer"]))  # [['']]
    print(groupAnagrams_M2(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max",
                            "doc"]))  # [['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
