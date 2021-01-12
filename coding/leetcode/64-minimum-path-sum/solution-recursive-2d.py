class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def find_cost(dp, grid, i, j):
            if dp[i][j] == -1:
                if i == rows -1 and j == cols -1:
                    dp[i][j] = grid[i][j]
                elif i == rows -1 and j < cols -1:
                    dp[i][j] = grid[i][j] + find_cost(dp, grid, i, j+1)
                elif i != rows -1 and j == cols -1:
                    dp[i][j] = grid[i][j] + find_cost(dp, grid, i+1, j)
                else:
                    dp[i][j] = grid[i][j] + min(find_cost(dp, grid, i, j+1), 
                                                find_cost(dp, grid, i+1, j))

            return dp[i][j]

        if grid is None or len(grid) == 0: return []

        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        find_cost(dp, grid, 0, 0)
        return dp[0][0]
