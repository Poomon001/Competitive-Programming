from typing import List

'''
    Purpose: Implement pagination of content_list by following requirements:
           : 1. first_content is where we start adding the first content
           : 2. page_size is the number of maximum contents in the page
           : 3. page_num is where we continue off
           : 4. page is empty if we start repeating the first_content
           : 5. need to pick up all content (e.g loop back if necessary) 
    parameter: TreeNode root1 - a root of a binary search tree
             : TreeNode root2 - a root of a binary search tree
    return: List[int] ans - a list containing all the integers from two trees sorted in ascending order
    Pre-Condition: The number of nodes in each tree is in the range [1, 5000].
                 : -10^5 <= Node.val <= 10^5
                 : root1 and root2 are a root of BST
    Post-Condition: none
'''
# array: runtime: O(n), memory: O(1)
def pages(content_list: List[int], first_content: int, page_size: int, page_num: int):
    size = len(content_list)
    page = []
    start_index = 0

    if page_num * page_size >= size:
        return []

    # get the starting point (req 1.)
    for i in range(len(content_list)):
        if content_list[i] == first_content:
            start_index = i

    start_index = (start_index + page_num * page_size) % size # (req 3.)

    # append content the page and stop if the content reach first_content # (req 2.)
    for i in range(page_size):
        index = (start_index + i) % size # (req 5.)
        page.append(content_list[index])
        if content_list[(start_index + i + 1) % size] == first_content:
            break

    return page


if __name__ == '__main__':
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 1, 3, 0)) # [1, 2, 7]
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 1, 3, 1)) # [4, 3, 8]
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 1, 3, 2)) # [9, 6]
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 1, 3, 3)) # []
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 1, 3, 4)) # []

    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 4, 4, 0)) # [4, 3, 8, 9]
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 4, 4, 1)) # [6, 1, 2, 7]
    print(pages([1, 2, 7, 4, 3, 8, 9, 6], 4, 4, 2)) # []

    print(pages([1, 2, 7, 4, 3, 8, 9, 5, 6, 10, 11, 20, 19], 11, 5, 0))  # [11, 20, 19, 1, 2]
    print(pages([1, 2, 7, 4, 3, 8, 9, 5, 6, 10, 11, 20, 19], 11, 5, 1))  # [7, 4, 3, 8, 9]
    print(pages([1, 2, 7, 4, 3, 8, 9, 5, 6, 10, 11, 20, 19], 11, 5, 2))  # [5, 6, 10]

    print(pages([1, 2, 7, 4], 2, 10, 0))  # [2, 7, 4, 1]
    print(pages([1, 2, 7, 4], 2, 10, 1))  # []