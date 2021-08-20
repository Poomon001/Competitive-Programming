import re

'''
    Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md
    Purpose: Read .txt file and count same words
    Parameter: None
    Print: String - each unique word in the text + a number of each of them
    Pre-Condition : None
    Post-Condition: None
'''

# size of hash
MAX = 100

# create hash
hashArr = [[] for i in range(MAX)]

''' find sum of ascii of a string and mod by hash size to get hash number '''
# define hash function
def get_hash(key):
    index = 0
    for char in key:
        index += ord(char)
    return index % MAX

''' chaining to handle collision '''
# add item to hashmap
def add(key, value):
    index = get_hash(key)

    # duplicate key then we update to the new tuple (cannot only change the key because it is a tuple element)
    if(len(hashArr[index]) > 0):
        for i in range(0, len(hashArr[index])):

            # duplicate key
            if(hashArr[index][i][0] == key):
                hashArr[index][i] = (key, value)
                return

    # duplicate first or index then we append to the next element
    hashArr[index].append((key, value))

# get item in the hashmap
def get(key):
    index = get_hash(key)
    for ele in hashArr[index]:
        if (ele[0] == key):
            return ele[1]

def counter(word):
    if(get(word) == None):
        return 1
    else:
        return get(word)+1

def printAnswer():
    # O(n)
    for element in hashArr:
        # mostly O(1)
        for index in range(0, len(element)):
            print(element[index][0], ":", element[index][1], end=", ")

# Solution 1: write hashmap from scratch
def solution_one():
    # read file, line by line, word by word
    with open("poem.txt", "r") as file:
        for line in file:

            # split by special char
            line = re.split(r'[^\w]', line)

            # add wordcount to hashmap
            for word in line:
                if(word == ''):
                    continue
                add(word, counter(word))

    printAnswer()

# Solution 2: use the build-in dictionary
def solution_two():
    dic = {}
    # read file, line by line, word by word
    with open("poem.txt", "r") as file:
        for line in file:

            # split by special char
            line = re.split(r'[^\w]', line)

            for word in line:
                if (word == ''):
                    continue
                elif(word in dic.keys()):
                    dic[word] += 1
                else:
                    dic[word] = 1

    for element in dic:
        print(element, ":", dic[element], end=", ")

solution_two()
print("\n")
solution_one()

