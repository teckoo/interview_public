class Solution:
    """
    BFS method is easier to understand, but somehow union-find is faster.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_island(cor_x, cor_y):
            stack = collections.deque([(cor_x, cor_y)])
            while stack:
                x, y = stack.pop()
                grid[x][y] = "0"
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                        # print(f"mark {i}, {j}")
                        stack.append((i, j))

        if not grid or not grid[0]: return 0
        self.islands = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.islands += 1
                    mark_island(i, j)
        return self.islands
