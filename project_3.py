#Checks matrix for correct Dimensions
def check_dimensions(grid):
    #checks that there are 9 rows
    if len(grid) != 9:
        return False
    #checks each row has 9 elements
    for row in grid:
        if len(row) != 9:
            return False
    #Could add an if statement to return false if type(row) != list: #if the row is actually a tuple
    return True

#validates data to be integers 1-9
def validate_data(grid):
    for row in grid:
          for cell in row:
               if type(cell) != int:
                    return False
               if cell > 9 or cell < 1:
                    return False
    return True

#Every row checker
def all_rows_checker(grid):
    for row in grid:
        #insertion sort
        sorted_row = sorted(row)
        if sorted_row != [1,2,3,4,5,6,7,8,9]:
             return False
    return True

#checks every column - by collecting all of the 1st/2nd/3rd...etc element of every row
def all_columns_checker(grid):
    column_list = []
    for i in range(9):
        for j in range(9):
            column_list.append(grid[j][i])
        column_list.sort()
        if column_list != [1,2,3,4,5,6,7,8,9]:
            return False
        column_list = []
    return True

#checks a certain 3x3 given grid
def check_3_square(grid ,min_row_index, min_col_index):
    max_row_index = min_row_index + 2
    max_col_index = min_col_index + 2
    vals_in_square = []
    #gets the row
    for i in range(min_row_index, min_row_index + 3):
        for j in range(min_col_index, min_col_index + 3):
            vals_in_square.append(grid[i][j])
    vals_in_square.sort()
    if vals_in_square != [1,2,3,4,5,6,7,8,9]:
        return False
    return True

#Combined solution validator
def checker(puzzle):
    if not check_dimensions(puzzle):
        return False
    if not validate_data(puzzle):
        return False
    if not all_rows_checker(puzzle):
        return False
    if not all_columns_checker(puzzle):
        return False
    corner_index_list = [0,3,6]
    for row_corner in corner_index_list:
        for col_corner in corner_index_list:
            if not check_3_square(puzzle, row_corner, col_corner):
                return False
    return True

valid_board = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
]
#if not checker(valid_board):
#    print('all good')
