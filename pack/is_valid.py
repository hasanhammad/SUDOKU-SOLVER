import os


def read_from_file (filename, table):
    with open(filename, 'r') as f:  # open file
        for line in f:   # take a file
            number_strings = line.split()  # split the line on runs of whitespace
            numbers = [int(n) for n in number_strings]  # convert to integers
            table.append(numbers)  # add the row (line) to the table.


def in_col(col, num, sudoku):
    for row in range(9):
        if sudoku[row][col] == num:  # if the passed number found in the row (duplicated)
            return True
    return False


def in_row(row, num, sudoku):
    for col in range(9):
        if sudoku[row][col] == num:  # if the passed number found in the column (duplicated)
            return True
    return False


def in_box(row, col, num, sudoku):
    row_range = row - row % 3
    col_range = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + row_range][j + col_range] == num:  # if the passed number found in the 3X3 box (duplicated)
                return True
    return False


def is_safe(row, col, num, sudoku):  # checks if the sudoku table contains duplicate numbers
    return not in_row(row, num, sudoku) and not in_col(col, num, sudoku) and not in_box(row, col, num, sudoku)


def find_empty_cell(row_col, sudoku):  # returns an empty cell
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                row_col[0] = row
                row_col[1] = col
                return True
    return False


def notInRow(arr, row):  # checks whether there is any duplicate in current row or not
    st = set()  # Set to store characters seen so far.
    for i in range(0, 9):
        # If already encountered before, return false
        if arr[row][i] in st:
            return False
        # If it is not an empty cell, insert value at the current cell in the set
        if arr[row][i] != 0:
            st.add(arr[row][i])
    return True


def notInCol(arr, col):  # checks whether there is any duplicate in current column or not
    st = set()
    for i in range(0, 9):
        # If already encountered before, return false
        if arr[i][col] in st:
            return False
        # If it is not an empty cell, insert value at the current cell in the set
        if arr[i][col] != 0:
            st.add(arr[i][col])
    return True


def notInBox(arr, startRow, startCol):  # Checks whether there is any duplicate in current 3x3 box or not.
    st = set()
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
            # If already encountered before, return false
            if curr in st:
                return False
            # If it is not an empty cell, insert value at current cell in set
            if curr != 0:
                st.add(curr)
    return True


# checks whether current row and current column and current 3x3 box is valid or not
def isValid(arr, row, col):
    return notInRow(arr, row) and notInCol(arr, col) and notInBox(arr, row - row % 3, col - col % 3)


def isValidConfig(arr, n):
    for i in range(0, n):
        for j in range(0, n):
            if not isValid(arr, i, j):  # if current row or current column or current 3x3 box is not valid, return false
                return False
    return True
