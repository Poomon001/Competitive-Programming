'''
    Link: https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color
    Purpose: Given an 8 x 8 chessboard with black/white colors and two coordinates, find if both coordinates have the same color.
    Parameter: str coordinate1 - a valid chessboard coordinate ([1-8][a-h])
             : str coordinate2 - a valid chessboard coordinate ([1-8][a-h])
    Returns: bool - True if both coordinates have the same color. Otherwise False.
    Pre-Condition: coordinate1.length == coordinate2.length == 2
                 : 'a' <= coordinate1[0], coordinate2[0] <= 'h'
                 : '1' <= coordinate1[1], coordinate2[1] <= '8'
    Post-Condition: none
'''
# rumtime: O(1), memory: O(1)
def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:
    # first = odd, second = even => white
    # first = odd, second = odd => black
    # first = even, second = even => black
    # first = even, second = odd => white

    # black = True
    # white = False
    def findColor(coordinate: str) -> bool:
        first = ord(coordinate[0]) - ord('a') + 1
        second = int(coordinate[1])

        return first % 2 == second % 2

    return findColor(coordinate1) == findColor(coordinate2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(checkTwoChessboards("a1", "a1")) # True
    print(checkTwoChessboards("a1", "c3")) # True
    print(checkTwoChessboards("a1", "h3")) # False

