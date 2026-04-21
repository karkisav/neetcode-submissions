class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Row_hash, Col_hash = [set() for _ in range(9)], [set() for _ in range(9)]
        Square_hash = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in Row_hash[row]:
                        return False
                    Row_hash[row].add(board[row][col])
                
                if board[col][row].isdigit():
                    if board[col][row] in Col_hash[row]:
                        return False
                    Col_hash[row].add(board[col][row])
                    
                if board[row][col].isdigit():
                    if board[row][col] in Square_hash[row // 3 * 3 + col //3]:
                        return False
                    Square_hash[row // 3 * 3 + col //3].add(board[row][col])
        return True