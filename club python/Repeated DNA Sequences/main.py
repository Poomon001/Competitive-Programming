from typing import List

'''
    Link: https://leetcode.com/problems/repeated-dna-sequences
    Purpose: Find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule
           : DNA contains 'A', 'C', 'G', and 'T'
    parameter: str s - a string of DNA
    return: List[str] answer - the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule
    Pre-Condition: 1 <= s.length <= 105
                 : s[i] is either 'A', 'C', 'G', or 'T'.
    Post-Condition: none
'''
# hashmap: runtime: O(n), memnory: O(n)
def findRepeatedDnaSequences(s: str) -> List[str]:
    if len(s) < 10:
        return []

    seen = set()
    answer = set()

    i = 0
    j = 9
    while j < len(s):
        pattern = s[i:j + 1]
        if pattern in seen:
            answer.add(pattern)
        else:
            seen.add(pattern)

        i += 1
        j += 1

    return list(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # ['CCCCCAAAAA', 'AAAAACCCCC']
    print(findRepeatedDnaSequences("ACGAGCATTTT")) # []
    print(findRepeatedDnaSequences("A")) # []
    print(findRepeatedDnaSequences("AAAAAAAAAAAAA")) # ["AAAAAAAAAA"]
