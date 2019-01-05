class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            if self.rowValid(board, i):
                if self.columnValid(board, i):
                    if not self.quarterValid(board, i):
                        return False
                else:
                    return False
            else:
                return False
        else:
            return True


    def quarterValid(self, board, n):
        centerX = 1 + (n % 3) * 3
        centerY = 1 + (n // 3) * 3
        subBoard = [board[centerX - 1][centerY - 1], board[centerX][centerY - 1], board[centerX + 1][centerY - 1]
            , board[centerX - 1][centerY], board[centerX][centerY], board[centerX + 1][centerY]
            , board[centerX - 1][centerY + 1], board[centerX][centerY + 1], board[centerX + 1][centerY + 1]]

        for i in range(0, 9):
            if subBoard[i] != '.' and subBoard[i] in subBoard[i + 1 : 9]:
                return False
        else:
            return True

    def rowValid(self, board, n):
        subBoard = [board[n][0], board[n][1], board[n][2]
            , board[n][3], board[n][4], board[n][5]
            , board[n][6], board[n][7], board[n][8]]
        for i in range(0, 9):
            if subBoard[i] != '.' and subBoard[i] in subBoard[i + 1 : 9]:
                return False
        else:
            return True

    def columnValid(self, board, n):
        subBoard = [board[0][n], board[1][n], board[2][n]
            , board[3][n], board[4][n], board[5][n]
            , board[6][n], board[7][n], board[8][n]]
        for i in range(0, 9):
            if subBoard[i] != '.' and subBoard[i] in subBoard[i + 1 : 9]:
                return False
        else:
            return True