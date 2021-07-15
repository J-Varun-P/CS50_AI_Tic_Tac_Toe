"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    print(len(board))
    x_turn = 0
    o_turn = 0
    for i in board:
        for j in i:
            if j == "X":
                x_turn += 1
            elif j == "O":
                o_turn += 1
    if terminal(board):
        return X
    if x_turn > o_turn:
        return O
    else:
        return X
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return (1,1)
    print("In actions")
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i,j))
                print(i,j)
    return actions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    whose_turn = player(board)
    print("----")
    print(action)
    print("----")
    board_temp = copy.deepcopy(board)
    board_temp[action[0]][action[1]] = whose_turn
    print("----")
    return board_temp
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal checking
    for i in range(3):
        x_wins = 0
        o_wins = 0
        for j in range(3):
            if board[i][j] == "X":
                x_wins += 1
            elif board[i][j] == "O":
                o_wins += 1
            if x_wins == 1 and o_wins == 1:
                break
        if x_wins == 3:
            return X
        elif o_wins == 3:
            return O
    # Vertical checking
    for i in range(3):
        x_wins = 0
        o_wins = 0
        for j in range(3):
            if board[j][i] == "X":
                x_wins += 1
            elif board[j][i] == "O":
                o_wins += 1
            if x_wins == 1 and o_wins == 1:
                break
        if x_wins == 3:
            return X
        elif o_wins == 3:
            return O
    # diagonal checking
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return X
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return O
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return X
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return O
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    check = winner(board)
    if check == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return False
        return True
    return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    check = winner(board)
    if check == "X":
        return 1
    elif check == "O":
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    whose_turn = player(board)
    if whose_turn == "X":
        v = -100
        a = actions(board)
        for action in a:
            v_temp = min_value(result(board,action))
            if v_temp > v:
                v = v_temp
                action_temp = action
    elif whose_turn == "O":
        v = 100
        a = actions(board)
        for action in a:
            v_temp = max_value(result(board,action))
            if v_temp < v:
                v = v_temp
                action_temp = action
    return action_temp
    #raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -100
    a = actions(board)
    for action in a:
        v = max(v,min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100
    a = actions(board)
    for action in a:
        v = min(v,max_value(result(board,action)))
    return v
