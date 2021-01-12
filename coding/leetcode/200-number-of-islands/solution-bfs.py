class Solution:
    def __init__(self):
        self.islands = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_island(cor_x, cor_y):
            self.islands += 1
            que = [(cor_x, cor_y)]
            for x,y in que:
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                        # print(f"mark {i}, {j}")
                        grid[i][j] = "0"
                        que += (i, j),

        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    mark_island(i, j)
        return self.islands
