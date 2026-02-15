import unittest
from project_3 import check_dimensions, validate_data, all_rows_checker, all_columns_checker, check_3_square, checker
#solved board
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
#8x8 board
invalid_size_board = [
  [5,3,4,6,7,8,9,1],
  [6,7,2,1,9,5,3,4],
  [1,9,8,3,4,2,5,6],
  [8,5,6,7,9,1,4,2],
  [4,2,6,8,5,3,7,9],
  [7,1,3,9,2,4,8,5],
  [9,6,1,5,3,7,2,8],
  [2,8,7,4,1,9,6,3],
]
invalid_data_board = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,'a',3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,10,7,9,1],
  [7,0,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,0,4],
  [2,8,7,4,0,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
]
#some number swap
invalid_board = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,9,2,5,6,7],
  [8,5,6,7,4,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
]

class TestChecker(unittest.TestCase):
    #check_dimensions
    def test_valid_dimension(self):
        self.assertTrue(check_dimensions(valid_board))
    def test_invalid_dimension(self):
        self.assertFalse(check_dimensions(invalid_size_board))

    #validate_data
    def test_valid_data(self):
        self.assertTrue(validate_data(valid_board))
    def test_invalid_data(self):
        self.assertFalse(validate_data(invalid_data_board))

    #all_rows_checker
    def test_rows_valid(self):
        self.assertTrue(all_rows_checker(valid_board))
    def test_rows_invalid(self):
        self.assertFalse(all_rows_checker(invalid_board))

    #all_columns_checker
    def test_cols_valid(self):
        self.assertTrue(all_columns_checker(valid_board))
    def test_cols_invalid(self):
        self.assertFalse(all_columns_checker(invalid_board))

    #check_3_square
    def test_3_top_square_valid(self):
        self.assertTrue(check_3_square(valid_board, 0, 0))
    def test_3_middle_square_valid(self):
        self.assertTrue(check_3_square(valid_board, 3, 3))
    def test_3_bottom_square_valid(self):
        self.assertTrue(check_3_square(valid_board, 6, 6))
    def test_3_top_middle_square_invalid(self):
        self.assertFalse(check_3_square(invalid_board, 0, 3))

    #checker
    def test_checker_valid(self):
        self.assertTrue(checker(valid_board))
    def test_checker_invalid_dimension(self):
        self.assertFalse(checker(invalid_size_board))
    def test_checker_invalid_data(self):
        self.assertFalse(checker(invalid_data_board))
    def test_checker_invalid_board(self):
        self.assertFalse(checker(invalid_board))

if __name__ == '__main__':
    unittest.main()



  #  #dimension check
  # def invalid_dim_test(self):
  #   self.assertFalse(check_dimensions(invalid_size_board))
    
  # def valid_dim_test(self):
  #   valid_board = [
  #   [5,3,4,6,7,8,9,1,2],
  #   [6,7,2,1,9,5,3,4,8],
  #   [1,9,8,3,4,2,5,6,7],
  #   [8,5,9,7,6,1,4,2,3],
  #   [4,2,6,8,5,3,7,9,1],
  #   [7,1,3,9,2,4,8,5,6],
  #   [9,6,1,5,3,7,2,8,4],
  #   [2,8,7,4,1,9,6,3,5],
  #   [3,4,5,2,8,6,1,7,9]
  #   ]
  #   self.assertFalse(check_dimensions(valid_board))

  # def test_validate_data(self):
  #   self.assertTrue(validate_data(valid_board))
  #   #def test_valid_check(self):
  #   #    self.assertTrue(checker(valid_board))

  #   #def test_invalid_check(self): 
  #   #    self.assertFalse(checker(invalid_board))
    