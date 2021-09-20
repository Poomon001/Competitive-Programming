from typing import List

'''
     Link: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3981/
     Purpose: Determine the winner of tic tac toe, Draw, or Pending 
     Parameter: List[List] moves - all moves of player A and B: A always start first
    Returns: string - the winner, Draw or Pending
    Pre-Condition: 1 <= moves.length <= 9
                 : moves[i].length == 2
                 : 0 <= moves[i][j] <= 2
                 : There are no repeated elements on moves.
                 : moves follow the rules of tic tac toe.
    Post-Condition: none
'''


# super brute force: O(nlog(n))
def FindWinnerTicTacToe_M1(moves: List[List[int]]) -> str:
    # there are 8 winning condition
    wins = []
    wins.append([[0, 0], [0, 1], [0, 2]])
    wins.append([[1, 0], [1, 1], [1, 2]])
    wins.append([[2, 0], [2, 1], [2, 2]])
    wins.append([[0, 0], [1, 0], [2, 0]])
    wins.append([[0, 1], [1, 1], [2, 1]])
    wins.append([[0, 2], [1, 2], [2, 2]])
    wins.append([[0, 0], [1, 1], [2, 2]])
    wins.append([[2, 0], [1, 1], [0, 2]])

    playerAMoves = []
    playerBMoves = []

    # get final board (Player A always start first)
    for i in range(len(moves)):
        # player A turn
        if i % 2 == 0:
            playerAMoves.append(moves[i])
        # player B tern
        else:
            playerBMoves.append(moves[i])

    # A win
    for win in wins:
        counter = 0
        for w in win:
            if w in playerAMoves:
                counter += 1
        if counter == 3:
            return "A"

    # B win
    for win in wins:
        counter = 0
        for w in win:
            if w in playerBMoves:
                counter += 1
        if counter == 3:
            return "B"

    # noone wins and board is full
    if (len(moves) == 9):
        return "Draw"

    # noone wins and board isn't full
    return "Pending"


'''
     Link: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3981/
     Purpose: Determine the winner of tic tac toe, Draw, or Pending 
     Parameter: List[List] moves - all moves of player A and B: A always start first
    Returns: string - the winner, Draw or Pending
    Pre-Condition: 1 <= moves.length <= 9
                 : moves[i].length == 2
                 : 0 <= moves[i][j] <= 2
                 : There are no repeated elements on moves.
                 : moves follow the rules of tic tac toe.
    Post-Condition: none
'''


# brute force: O(n)
def FindWinnerTicTacToe_M2(moves: List[List[int]]) -> str:
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    # write final board (Player A always start first)
    for i in range(len(moves)):
        # player A turn
        if i % 2 == 0:
            board[moves[i][0]][moves[i][1]] = "A"
        # player B turn
        else:
            board[moves[i][0]][moves[i][1]] = "B"

    # check row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]

    # check column
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]

    # check Diagonal \
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]

    # check Diagonal /
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    # noone wins and board is full
    if (len(moves) == 9):
        return "Draw"

    # noone wins and board isn't full
    return "Pending"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === method 1 ===\n")
    print(FindWinnerTicTacToe_M1([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # A
    print(FindWinnerTicTacToe_M1([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # B
    print(FindWinnerTicTacToe_M1([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # Draw
    print(FindWinnerTicTacToe_M1([[0, 0], [1, 1]]))  # Pending
    print(FindWinnerTicTacToe_M1([[0, 0], [1, 1], [0, 1], [0, 1], [1, 0], [2, 1]]))  # B
    print(FindWinnerTicTacToe_M1([[0, 0], [1, 1], [0, 1], [2, 1], [0, 2], [2, 0]]))  # A
    print(FindWinnerTicTacToe_M1([[0, 0], [2, 2], [1, 0], [2, 0], [0, 1], [1, 2], [1, 1], [0, 2]]))  # B

    print("\n === method 2 ===\n")

    print(FindWinnerTicTacToe_M2([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # A
    print(FindWinnerTicTacToe_M2([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # B
    print(FindWinnerTicTacToe_M2([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # Draw
    print(FindWinnerTicTacToe_M2([[0, 0], [1, 1]]))  # Pending
    print(FindWinnerTicTacToe_M2([[0, 0], [1, 1], [0, 1], [0, 1], [1, 0], [2, 1]]))  # B
    print(FindWinnerTicTacToe_M2([[0, 0], [1, 1], [0, 1], [2, 1], [0, 2], [2, 0]]))  # A
    print(FindWinnerTicTacToe_M2([[0, 0], [2, 2], [1, 0], [2, 0], [0, 1], [1, 2], [1, 1], [0, 2]]))  # B
