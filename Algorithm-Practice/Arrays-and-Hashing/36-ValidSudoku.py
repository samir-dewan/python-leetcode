import collections

def ValidSudoku(board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set) #creates a default dictionary for rows, cols, squares
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9): #looks through every list[list] in board as a row
        for c in range(9): #looks through every str in list[list] as a column
            if board[r][c] == ".": #if it's blank carry on
                continue
            if (board[r][c] in rows[r] or #if the number in row, column, is already in a row, column, or square (found by the remainder)
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False #it already is in the row, column, or square
            cols[c].add(board[r][c]) #add the number to the columns, rows, and squares
            rows[r].add(board[r][c])
            squares[((r// 3, c // 3))].add(board[r][c])
    
    return True #if it goes through all that it's valid