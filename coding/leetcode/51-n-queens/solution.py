class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col):
            if cols[col] or diag_l[row + col] or diag_r[col - row + n - 1]: 
                return False
            return True
        
        def make_solution(grid):
            res = []
            for row in grid:
                res.append("".join(row))
            return res
        
        def backtrack(row):
            if row == n:
                # print(f"found a result: {grid}")
                result.append(make_solution(grid))
                return
            for col in range(len(grid[row])):
                if is_valid(row, col):
                    cols[col] = True
                    diag_l[row + col] = True
                    diag_r[col - row + n - 1] = True
                    grid[row][col] = "Q"
                    backtrack(row + 1)
                    grid[row][col] = "."
                    cols[col] = False
                    diag_l[row + col] = False
                    diag_r[col - row + n - 1] = False
                
        result = []
        grid = [['.'] * n for _ in range(n)]
        cols = [False] * n
        m = n * 2 - 1
        diag_l = [False] * m
        diag_r = [False] * m
        backtrack(0)
        return result
