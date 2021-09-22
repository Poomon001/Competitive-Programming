import itertools
from typing import List
def maxLength(arr: List) -> int:
    words = []
    maxLength = 0

    # find all possible combination of each arr elements
    print(*itertools.combinations("".join(ar, 2))

    # # find the max length word with all unique char from the list
    # for word in words:
    #     # determine if a word contain a duplicate
    #     currMaxLength = 0
    #     chars = []
    #     for char in word:
    #         if char not in chars:
    #             chars.append(char)
    #             currMaxLength = max(currMaxLength, len(chars))
    #         else:
    #             # not a unique char word
    #             currMaxLength = 0
    #             break
    #         maxLength = max(maxLength, currMaxLength)


    return maxLength

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maxLength(["un","iq","ue"]))
    print(maxLength(["cha","r","act","ers"]))
    print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))

