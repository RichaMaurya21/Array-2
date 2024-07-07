## Problem3 (https://leetcode.com/problems/game-of-life/)
# 
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        
        def count_live_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (board[nr][nc] == 1 or board[nr][nc] == 2):
                    live_neighbors += 1
            return live_neighbors

        # First pass: apply the rules
        for r in range(row):
            for c in range(col):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # mark as dead in next state
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3  # mark as alive in next state

        # Second pass: update the board to the next state
        for r in range(row):
            for c in range(col):
                if board[r][c] == 2:
                    board[r][c] = 0  # now dead
                elif board[r][c] == 3:
                    board[r][c] = 1  # now alive


sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
print(board)