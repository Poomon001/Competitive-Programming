from collections import Counter
'''
    Purpose: Find the maximum number of a word from a S word list that can be produce from all chars in string L.
           : S = "AASDFGHJK", L = ["A", "S", "BOX", "ASD"] 
           : answer is 2 b/c "A" can be produced 2 times where "S", "ASD" can be produced 1 times, and "BOX" cannot be produced. 
    parameter: str S - a string contain only uppercase alphabets
             : List[str] L - a list of string
    return: int maximum - the maximum number of a word from a S word list that can be produce from all chars in string L.
    Pre-Condition: L and S only contain uppercase alphabet
                 : S and L cannot be empty 
    Post-Condition: none
'''
# runtime: O(m*n), memory: O(n) where m is len(L) and n is a len(S)
def maximumProducts(S, L):
    maximum = 0

    for word in L:
        # reset S and counter every iteration of word in L
        dic = Counter(S)
        counter = 0

        # loop until S runs out of char to produce L
        while True:
            for c in word:
                # S still have char to produce P. Else is otherwise.
                if dic[c] != 0:
                    dic[c] -= 1
                else:
                    # calculate the max product then exit the while loop
                    break
            else:
                # finish without break then count a complete product
                counter += 1
                continue
            maximum = max(counter, maximum)
            break

    return maximum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maximumProducts("BILLOBILLOLLOBBI", ["BILL", "BOB"])) # 3
    print(maximumProducts("CAT", ["ILOVEMYDOG", "CATS"])) # 0
    print(maximumProducts("ABCDXYZ", ["ABCD", "XYZ"])) # 1
    print(maximumProducts("ZABCZDXYZZ", ["ABCD", "XYZ", "Z"])) # 4
    print(maximumProducts("ZABCZDXZZZZZZYZZYYYYYYYYYABCDAAAAAAAAAAAAAAAAAAAAAAAA", ["ABCD", "Y", "Z"])) # 10

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
