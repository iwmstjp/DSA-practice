class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList =[[] for i in range(9)]
        colList =[[] for i in range(9)]
        area = defaultdict(list)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowList[row]:
                    return False
                rowList[row].append(board[row][col])
                if board[row][col] in colList[col]:
                    return False
                colList[col].append(board[row][col])
                if board[row][col] in area[row//3, col//3]:
                    return False
                area[row//3, col//3].append(board[row][col])  
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_check = defaultdict(list)
        block_check = defaultdict(list)
        for i in range(len(board)):
            row_check = {}
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_check or board[i][j] in col_check[j] or board[i][j] in block_check[i//3, j//3]:
                    return False
                row_check[board[i][j]] = 1
                col_check[j].append(board[i][j])
                block_check[i//3, j//3].append(board[i][j])
        return True