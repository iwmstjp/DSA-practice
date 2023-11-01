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