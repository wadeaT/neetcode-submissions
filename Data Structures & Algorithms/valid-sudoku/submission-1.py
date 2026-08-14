class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #brute force
        mat = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(set())
            mat.append(row)
        
        columns = {}
        rows = {}

        n = len(board) # 9 
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    row = (i,0)
                    col = (0,j)
                    if row in rows : 
                        if board[i][j] in rows[row]:
                            return False
                        rows[row].add(board[i][j])
                    else:
                        rows[row] = set()
                        rows[row].add(board[i][j])
                    if col in columns:
                        if board[i][j] in columns[col]:
                            return False
                        columns[col].add(board[i][j])
                    else:
                        columns[col] = set()
                        columns[col].add(board[i][j])
                    if board[i][j] in mat[i//3][j//3]:
                        return False
                    mat[i//3][j//3].add(board[i][j])
        return True