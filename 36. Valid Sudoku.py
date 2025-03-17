class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            map_rows = {}
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in map_rows:
                        return False
                    map_rows[board[row][col]] = True
        
        for col in range(9):
            map_column = {}
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in map_column:
                        return False
                    map_column[board[row][col]] = True
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                map_squ = {}
                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num != ".":
                            if num in map_squ:
                                return False
                            map_squ[num] = True
        
        return True

  
