#Checks matrix for correct Dimensions
def check_dimensions(grid):
    #checks that there are 9 rows
    if len(grid) != 9:
            return False
    #checks each row has 9 elements
    for row in grid:
        if len(row) != 9:
            return False
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

