# Project-3-Sudoku-Validator
CSC101 Project 3 Sudoku Solution Checker
Overview
In this project, you will implement a Sudoku solution validator. Your program will determine whether a given 9×9 Sudoku board represents a valid, completed solution.

Problem Description
You will be given a 2D list representing a Sudoku board.

The board contains integers.
Valid digits are 1–9.
The value 0 represents a blank cell.
You must implement the following function:

def checker(puzzle):
This function should return:

True if the board is a valid completed Sudoku solution
False otherwise
Requirements for Returning True
Your function must return True only if all conditions below are satisfied.

1) Correct Dimensions
The input is a 9×9 2D list.
There are exactly 9 rows.
Each row contains exactly 9 elements.
2) Valid Data
Every element is an integer.
Each element is a single digit in the range 1–9.
No zeros are present.
No non-integer values (e.g., strings, floats) are present.
3) Sudoku Rules Are Satisfied
Each of the following must contain exactly the digits 1–9 (no repeats, none missing):

Every row
Every column
Every 3×3 subgrid
Conditions for Returning False
Your function must return False if any of the following occur:

The board is not 9×9.
Any row does not contain 9 elements.
Any element is not an integer.
Any element is not in the range 1–9.
Any zeros are present.
Any row contains duplicates.
Any column contains duplicates.
Any 3×3 subgrid contains duplicates.
Implementation Notes
You may write additional helper functions as needed.
You may use any Python built-in functions for lists.
You should write test cases for any helper functions you create.