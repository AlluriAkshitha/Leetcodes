class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        def is_valid(board, row, col, num):
            
            for i in range(9):
                if board[row][i] == num:
                    return False
            
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def backtrack(board):
           
            min_choices = 10  
            min_cell = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        choices = 0
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                choices += 1
                        if choices < min_choices:
                            min_choices = choices
                            min_cell = (i, j)
            
            if not min_cell:
                return True  
            
            row, col = min_cell
            for num in '123456789':
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    if backtrack(board):
                        return True
                    board[row][col] = '.'  
            
            return False
        
        backtrack(board)
