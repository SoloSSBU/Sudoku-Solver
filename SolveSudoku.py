import copy

def solve(board):
    updatedB = getPossibleNumbers(board)
    n = len(board)
    x, y = 0, 0
    anyConfirms = True
    #Fills in any squares that only have 1 possibility, eliminates possibilities based the new squares,
    #and runs until either game is solved or all empty squares have more than 1 possibility
    while anyConfirms:
        anyConfirms = False
        while x < n:
            while y < n:
                pos = board[x][y]
                if type(pos) == list and len(pos) == 1:
                    board[x][y] = pos[0] 
                    elimPossibilities(board[x][y], x, y, board)
                    anyConfirms = True
                y += 1
            y = 0
            x += 1
        x = 0
    #resort to backtracking if not complete
    board = backtrack(board)
    return board



def backtrack(board):
    n = len(board)
    x, y = 0, 0
    while x < n:
        while y < n:
            pos = board[x][y]
            if type(pos) == list:
                for val in pos:
                    newB = copy.deepcopy(board)
                    newB[x][y] = val
                    newB = elimPossibilities(val, x, y, newB)
                    answer = backtrack(newB)
                    if answer != None:
                        return answer
                return None
            y += 1
        y = 0
        x += 1
    return board




#takes in the current board and returns all possible numbers for every position without backtracking
#eliminates all numbers in same row, column, and box
#maybe also eliminates more using logic
def getPossibleNumbers(board):
    n = len(board)
    x, y = 0, 0
    retBoard = board.copy()
    #Setup retBoard by replacing the 0's in Board with a list from 1-9 representing possible numbers
    while x < n:
        while y < n:
            if retBoard[x][y] == 0:
                retBoard[x][y] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            y += 1
        y = 0
        x += 1
    x, y = 0, 0
    #Remove any possibilities that have overlap with the numbers in the same row, column or box
    while x < n:
        while y < n:
            curNum = retBoard[x][y]
            if type(curNum) == int:
                elimPossibilities(curNum, x, y, retBoard)
            y += 1
        y = 0
        x += 1
    return retBoard
        
#takes a number, position and board. Removes all possibilities of the same number in the same box, column, and row.
def elimPossibilities(curNum, x, y, board):
    #checking columns
    for pos in board[x]:
        if type(pos) == list and curNum in pos:
            pos.remove(curNum)

    #checking rows
    for xs in board:
        if type(xs[y]) == list and curNum in xs[y]:
            xs[y].remove(curNum)

    #checking boxes
    box = 3 * (x//3) + y//3
    yStart = (box % 3) * 3
    xStart = (box//3) * 3
    ys = yStart
    xs = xStart
    while xs < xStart + 3:
        while ys < yStart + 3:
            pos = board[xs][ys]
            if type(pos) == list and curNum in pos:
                pos.remove(curNum)
            ys += 1
        ys = yStart
        xs += 1
    
    return board